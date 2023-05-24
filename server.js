import express, { json } from 'express';
import { connect, Schema, model } from 'mongoose';
import cors from 'cors';

// Connect to MongoDB
connect('mongodb://localhost/tinymce-db', { useNewUrlParser: true, useUnifiedTopology: true });

// Define Mongoose schema for TinyMCE content
const ContentSchema = new Schema({
  content: String
});

// Create Mongoose model
const Content = model('Content', ContentSchema);

const app = express();

// Middlewares
app.use(cors());
app.use(json());

// POST route to save TinyMCE content
app.post('/api/saveContent', async (req, res) => {
  const { content } = req.body;

  const newContent = new Content({ content });

  try {
    await newContent.save();
    res.status(200).json({ message: 'Content saved successfully' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Server listening
app.listen(3000, () => console.log('Server started on port 3000'));
