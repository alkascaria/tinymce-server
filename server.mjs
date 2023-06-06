import mongoose, { Schema, model } from 'mongoose';
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
 */ 

//Mongoose schema and model for SaveToDB
const ContentSchema = new Schema({
    id: String,
    name: String,
    date: Date,
    content: String,
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
*/

// POST route to save TinyMCE content to DB - SaveToDB
app.post('/api/saveContent', async (req, res) => {
    const { id, name,date, content } = req.body;
    const newContent = new Content({ id,name,date,content });

    try {
        await newContent.save();
        res.status(200).json({ message: 'Content saved successfully' });
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
 
// Server listening
app.listen(port,() => {
    console.log(`Server started at http://127.0.0.1:${port}`)
});