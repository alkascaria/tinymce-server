import mongoose, { Schema, model } from 'mongoose';
import express, { json } from 'express';
import cors from 'cors';

const port = 5000; //Fixed port
const url = 'mongodb://127.0.0.1:27017/'; //DB connection url

mongoose.connect( url, {
    dbname:'tinymce-db',
    useNewUrlParser: true,
    useUnifiedTopology: true
})
  .then(() => {
    console.log('Connected to yourDB-name database');
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
 */ 

// Define Mongoose schema for TinyMCE content
const ContentSchema = new Schema({
    content: String
});

// Create Mongoose model
const Content = model('Content', ContentSchema);

const app = express(); 

// Middlewares
app.use(cors());
/* 
//Use if there is an error
app.use(cors({
    origin: 'http://localhost:5000', // replace with your client's origin
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
    credentials: true,
}));
 */
app.use(express.json());

// POST route to save TinyMCE content
app.post('/api/saveContent', async (req, res) => {
    const { content } = req.body;
    const newContent = new Content({ 'content' : content });

    try {
        await newContent.save();
        res.status(200).json({ message: 'Content saved successfully' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});
 
// Server listening
app.listen(port,() => {
    console.log(`Server started at http://127.0.0.1:${port}`)
});