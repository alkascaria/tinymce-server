import mongoose, { Schema, model } from 'mongoose';
import express, { json } from 'express';
import cors from 'cors';

const port = 5000; // Default to 5000
const url = 'mongodb://127.0.0.1:27017/'; // Default to local MongoDB

// Establishing the DB connection
mongoose.connect( url, {

  dbname:'tinymce-db',
  useNewUrlParser: true,
  useUnifiedTopology: true

}).then(() => {
  console.log('Connected to the database');
}).catch((error) => {
  console.error('Error connecting to database:', error);
});

// Middlewares
const app = express(); 
app.use(cors()); 
app.use(express.json());

// Error Handling Middleware
app.use((err, req, res, next) => {

  console.error(err.stack);
  // in a development environment, sending the detailed error
  if (process.env.NODE_ENV === 'development') {
      res.status(500).send(err.message);
  } else {
      // in a production environment, a generic error message
      res.status(500).send('Internal Server Error');
  }
});

// Mongoose schema and model for ImageDB
const ImageSchema = new Schema({

    data: { type: Buffer, required: true }, // Image data
    contentType: { type: String, required: true }, // Image MIME type
});
const Image = model('Image', ImageSchema);

// Define the schemas for ContentDB
const GroupSchema = new mongoose.Schema({ name: String });
const Group = mongoose.model('Group', GroupSchema);

const ContentSchema = new mongoose.Schema({

  name: String,
  date: Date,
  content: String,
  groupID: { type: mongoose.Schema.Types.ObjectId, ref: 'Group' },

});
const Content = mongoose.model('Content', ContentSchema);

// POST route to save DB contents - ContentDB
app.post('/api/saveContent', async (req, res, next) => {

  const { name, date, content, groupID } = req.body;
  
  try {
    
    // Validate request body
    if (!name || !date || !content || !groupID) {
      return res.status(400).json({ message: 'All fields are required' });
    }
  
    // Find or create the group
    let group = await Group.findOne({ name: groupID });
    if (!group) {
      group = new Group({ name: groupID });
      await group.save();
    }
  
    const newContent = new Content({ name, date, content, groupID: group._id });
    await newContent.save();
    res.status(200).json({ message: 'Content saved successfully' });
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});

// UPDATE route to updat DB contents - ContentDB
app.put('/api/updateContent/:name', async (req, res, next) => {

  const { name } = req.params;
  const { date, content, groupID } = req.body;
  
  try {
    // Validate request body
    if (!date || !content || !groupID) {
      return res.status(400).json({ message: 'All fields are required' });
    }
  
    // Find the group by name
    const group = await Group.findOne({ name: groupID });
  
    // If the group does not exist, return an error
    if (!group) {
      return res.status(404).json({ message: 'Group not found' });
    }
  
    const existingContent = await Content.findOne({ name: name }).populate('groupID');
  
    if (existingContent) {

      // If the document already exists, update it
      existingContent.date = date;
      existingContent.content = content;
      existingContent.groupID = group._id; // Set the group field to the ID of the group
      await existingContent.save();

      res.status(200).json({ message: 'Content updated successfully' });
    } else {
      // If no such document exists, send an error response
      res.status(404).json({ message: 'Content not found' });
    }
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});

// GET route to fetch DB contents - ContentDB
app.get('/api/contents', async (req, res, next) => {

  try {

    const contents = await Content.find({}).populate('groupID').lean();
    res.status(200).json(contents);
  } catch (err) {  
    next(err); // Pass error to error handling middleware
  }
});

// CHECK route to check DB contents (exprement group and document name) - ContentDB
app.get('/api/checkContent/:name/:groupName', async (req, res, next) => {
  const { name, groupName } = req.params;

  try {
    // Find the groupID using the groupName
    const group = await Group.findOne({ name: groupName });

    if (!group) {
      return res.status(400).json({ error: 'Group not found' });
    }

    // Use the groupID to find the content
    const existingContent = await Content.findOne({ name: name, groupID: group._id });

    if (existingContent) {
      res.status(200).json({ exists: true });
    } else {
      res.status(200).json({ exists: false });
    }
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});
  
// GET route to fetch symbol from DB - ImageDB
app.get('/api/images', async (req, res, next) => {

  try {

    const images = await Image.find({}).lean();
    res.status(200).json(images);
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});

app.listen(port, () => console.log(`Server running on port ${port}`));