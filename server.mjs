/* import mongoose, { Schema, model } from 'mongoose';
import express, { json } from 'express';
import cors from 'cors';

const port = 5000; //Fixed port
const url = 'mongodb://127.0.0.1:27017/'; //DB connection url

//Establishing the DB connection
mongoose.connect( url, {
    dbname:'tinymce-db',
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => {
    console.log('Connected to the database');
})
.catch((error) => {
    console.error('Error connecting to database:', error);
});

/* // To check is mongo is getting connected
const checkDBConnection = () => {
    switch(mongoose.connection.readyState) {
        case 0:
            return "MongoDB connection is disconnected.";
        case 1:
            return "MongoDB connection is connected.";
        case 2:
            return "MongoDB connection is connecting.";
        case 3:
            return "MongoDB connection is disconnecting.";
        default:
            return "Unknown MongoDB connection state.";
    }
}

console.log(checkDBConnection());
  

//Mongoose schema and model for SaveToDB
const ContentSchema = new Schema({
    id: String,
    name: String,
    date: String,
    content: String,
    group: String,
});
const Content = model('Content', ContentSchema);

//Mongoose schema and model for ImageDB
const ImageSchema = new Schema({
    data: Buffer, // Image data
    contentType: String, // Image MIME type
});
const Image = model('Image', ImageSchema);

//Middlewares
const app = express(); 
app.use(cors()); 
app.use(express.json());

/* 
//Use if there is an error
app.use(cors({
    origin: 'http://localhost:5000', // replace with your client's origin
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
    credentials: true,
}));


// POST route to save TinyMCE content to DB - SaveToDB
app.post('/api/saveContent', async (req, res) => {
    const { id, name, date, content, group } = req.body;

    try {
        const existingContent = await Content.findOne({ id: id });

        if (existingContent) {
            // If the document already exists, update it
            existingContent.name = name;
            existingContent.date = date;
            existingContent.content = content;
            existingContent.group = group;
            await existingContent.save();
            res.status(200).json({ message: 'Content updated successfully' });
        } else {
            // If the document doesn't exist, create a new one
            const newContent = new Content({ id, name, date, content, group });
            await newContent.save();
            res.status(200).json({ message: 'Content saved successfully' });
        }
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

//GET route to fetch symbol from DB - ImageDB
app.get('/api/images', async (req, res) => {
    try {
        const images = await Image.find({}).lean();
        res.status(200).json(images);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// GET route to fetch DB contents
app.get('/api/contents', async (req, res) => {
    try {
      const contents = await Content.find({}).lean();
      res.status(200).json(contents);
    } catch (err) {
      res.status(500).json({ message: err.message });
    }
  });
  
 
// Server listening
app.listen(port,() => {
    console.log(`Server started at http://127.0.0.1:${port}`)
}); */

import mongoose, { Schema, model } from 'mongoose';
import express, { json } from 'express';
import cors from 'cors';

const port = process.env.PORT || 5000; // Use environment variable or default to 5000
const url = process.env.MONGODB_URI || 'mongodb://127.0.0.1:27017/'; // Use environment variable or default to local MongoDB

//Establishing the DB connection
mongoose.connect( url, {
    dbname:'tinymce-db',
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => {
    console.log('Connected to the database');
})
.catch((error) => {
    console.error('Error connecting to database:', error);
});

//Middlewares
const app = express(); 
app.use(cors()); 
app.use(express.json());

// Error Handling Middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

//Mongoose schema and model for ImageDB
const ImageSchema = new Schema({
    data: { type: Buffer, required: true }, // Image data
    contentType: { type: String, required: true }, // Image MIME type
});
const Image = model('Image', ImageSchema);

// Define the schemas for ContentDB
const GroupSchema = new mongoose.Schema({ name: String });
const Group = mongoose.model('Group', GroupSchema);

const ContentSchema = new mongoose.Schema({
  id: String,
  name: String,
  date: Date,
  content: String,
  groupID: { type: mongoose.Schema.Types.ObjectId, ref: 'GroupID' },
});
const Content = mongoose.model('Content', ContentSchema);

app.post('/api/saveContent', async (req, res, next) => {
    const { id, name, date, content, groupID } = req.body;
  
    console.log(req.body);
  
    try {
      console.log('inside try');
      // Validate request body
      console.log(name + date + content + groupID);
      if (!id || !name || !date || !content || !groupName) {
        console.log('inside if');
        return res.status(400).json({ message: 'All fields are required' });
      }
  
      // Find or create the group
      let group = await Group.findOne({ name: groupName });
      console.log(group);
      if (!group) {
        console.log('inside group');
        group = new Group({ name: groupName });
        console.log(group);
        await group.save();
      }
  
      const newContent = new Content({ id, name, date, content, groupID: group._id });
      await newContent.save();
      res.status(200).json({ message: 'Content saved successfully' });
    } catch (err) {
      next(err); // Pass error to error handling middleware
    }
  });
  
/* // API endpoint to save or update data
app.post('/api/saveContent', async (req, res, next) => {
    const { id, name, date, content, groupName } = req.body;
  
    console.log(req.body); // Add this line to log the request body
  
    try {
        console.log('inside try');
      // Validate request body
      console.log(name + date + content +groupName);
      if (!id || !name || !date || !content || !groupName) {
        console.log('inside if');
        return res.status(400).json({ message: 'All fields are required' });
      }
      // Find or create the group
      let group = await Group.findOne({ name: groupName });
      console.log(group);
      if (!group) {
        console.log('inside group');
        group = new Group({ name: groupName });
        console.log(group);
        await group.save();
      }
  
    //   const existingContent = await Content.findOne({ name: name });
  
    //   if (existingContent) {
    //     // If the document already exists, update it
    //     existingContent.name = name;
    //     existingContent.date = date;
    //     existingContent.content = content;
    //     existingContent.group = group._id;
    //     await existingContent.save();
    //     res.status(200).json({ message: 'Content updated successfully' });
    //   } else {
        // If the document doesn't exist, create a new one
        const newContent = new Content({ id, name, date, content, groupId: group._id });
        await newContent.save();
        res.status(200).json({ message: 'Content saved successfully' });
    //   }
    } catch (err) {
      next(err); // Pass error to error handling middleware
    }
  }); */


app.get('/api/checkContent/:name', async (req, res, next) => {
    const { name } = req.params;
  
    try {
      const existingContent = await Content.findOne({ name: name }).populate('group');
  
      if (existingContent) {
        // If a document with the given name exists, send a positive response along with the group name
        res.status(200).json({ exists: true, groupName: existingContent.group.name });
      } else {
        console.log('here');
        // If no such document exists, send a negative response
        res.status(200).json({ exists: false });
      }
    } catch (err) {
      next(err); // Pass error to error handling middleware
    }
  });
  
  app.put('/api/updateContent/:name', async (req, res, next) => {
    const { name } = req.params;
    const { id, date, content, groupName } = req.body;
  
    try {
      // Validate request body
      if (!id || !date || !content || !groupName) {
        return res.status(400).json({ message: 'All fields are required' });
      }
  
      // Find the group by name
      const group = await Group.findOne({ name: groupName });
  
      // If the group does not exist, return an error
      if (!group) {
        return res.status(404).json({ message: 'Group not found' });
      }
  
      const existingContent = await Content.findOne({ name: name });
  
      if (existingContent) {
        // If the document already exists, update it
        existingContent.id = id;
        existingContent.date = date;
        existingContent.content = content;
        existingContent.group = group._id; // Set the group field to the ID of the group
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
  

//GET route to fetch symbol from DB - ImageDB
app.get('/api/images', async (req, res, next) => {
    try {
        const images = await Image.find({}).lean();
        res.status(200).json(images);
    } catch (err) {
        next(err); // Pass error to error handling middleware
    }
});

// GET route to fetch DB contents
app.get('/api/contents', async (req, res, next) => {
    try {
      const contents = await Content.find({}).lean();
      res.status(200).json(contents);
    } catch (err) {  
        next(err); // Pass error to error handling middleware
    }
  });
  
  app.listen(port, () => console.log(`Server running on port ${port}`));

  