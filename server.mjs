import mongoose, { Schema, model } from "mongoose";
import express, { json } from "express";
import cors from "cors";

const port = 5000; // Default to 5000
const url = "mongodb://127.0.0.1:27017/"; // Default to local MongoDB

// Establishing the DB connection
mongoose
  .connect(url, {
    dbname: "tinymce-db",
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log("Connected to the database");
  })
  .catch((error) => {
    console.error("Error connecting to database:", error);
  });

// Middlewares
const app = express();
app.use(cors());
app.use(express.json());

// Mongoose schema and model for ImageDB
const PiktogrammSchema = new Schema({
  _id: String,
  description: String,
  symbol: String,
});
const Piktogramm = mongoose.model("Piktogramm", PiktogrammSchema);

// Define the schemas for Experiment Group
const GroupSchema = new Schema({ name: String });
const Group = model("Group", GroupSchema);

//Define the schemas for ContentDB
const ContentSchema = new Schema({
  name: String,
  date: Date,
  content: String,
  groupID: { type: Schema.Types.ObjectId, ref: "Group" },
});
const Content = model("Content", ContentSchema);

const HsatzSchema = new Schema({
  _id: String,
  description: String,
  pharsen_reference_id: {
    type: String,
    default: null,
  },
  ghs_reference_id: String,
  psätze_id: {
    type: [String],
    default: null,
  },
});
const Hsatz = model("Hsatz", HsatzSchema);

const PsatzSchema = new Schema({
  _id: String,
  description: String,
});
const Psatz = model("Psatz", PsatzSchema);

const EuhsatzSchema = new Schema({
  _id: String,
  description: String,
});
const Euhsatz = model("Euhsatz", PsatzSchema);

async function findGroupByName(groupName) {
  const group = await Group.findOne({ name: groupName });

  if (!group) {
    throw new Error("Group not found");
  }

  return group;
}

// POST route to save DB contents - ContentDB
app.post("/api/saveContent", async (req, res, next) => {
  const { name, date, content, groupID } = req.body;

  try {
    // Validate request body
    if (!name || !date || !content || !groupID) {
      return res.status(400).json({ message: "All fields are required" });
    }

    // Find or create the group
    let group = await Group.findOne({ name: groupID });
    if (!group) {
      group = new Group({ name: groupID });
      await group.save();
    }

    const newContent = new Content({ name, date, content, groupID: group._id });
    await newContent.save();
    res.status(200).json({ message: "Content saved successfully" });
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});

// UPDATE route to updat DB contents - ContentDB
app.put("/api/updateContent/:name", async (req, res, next) => {
  const { name } = req.params;
  const { date, content, groupID } = req.body;

  try {
    // Validate request body
    if (!date || !content || !groupID) {
      return res.status(400).json({ message: "All fields are required" });
    }

    const group = await findGroupByName(req.body.groupID);
    console.log("update group" + group);

    const existingContent = await Content.findOne({ name: name }).populate(
      "groupID"
    );
    console.log("updategroupis" + groupID);

    if (existingContent) {
      // If the document already exists, update it
      existingContent.date = date;
      existingContent.content = content;
      existingContent.groupID = group._id; // Set the group field to the ID of the group
      await existingContent.save();

      res.status(200).json({ message: "Content updated successfully" });
    } else {
      // If no such document exists, send an error response
      res.status(404).json({ message: "Content not found" });
    }
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});

// GET route to fetch DB contents - ContentDB
app.get("/api/contents", async (req, res, next) => {
  try {
    const contents = await Content.find({}).populate("groupID").lean();
    res.status(200).json(contents);
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});

// CHECK route to check DB contents (exprement group and document name) - ContentDB
app.get("/api/checkContent/:name/:groupName", async (req, res, next) => {
  const { name, groupName } = req.params;

  try {
    // Find the groupID using the groupName
    const group = await Group.findOne({ name: groupName });

    if (!group) {
      return res.status(400).json({ error: "Group not found" });
    }

    // Use the groupID to find the content
    const existingContent = await Content.findOne({
      name: name,
      groupID: group._id,
    });

    if (existingContent) {
      res.status(200).json({ exists: true });
    } else {
      res.status(200).json({ exists: false });
    }
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});

// GET route to fetch all groups - ContentDB
app.get("/api/groups", async (req, res, next) => {
  try {
    const groups = await Group.find({}).lean(); // Fetch all groups from the database
    res.status(200).json(groups); // Send the fetched groups as a JSON response
  } catch (err) {
    next(err); // Pass the error to the error handling middleware
  }
});

// DELETE route to delete DB contents - ContentDB
// DELETE route to delete group and/or document - ContentDB
app.delete("/api/delete", async (req, res, next) => {
  const { groupName, docName } = req.body;

  try {
    // Validate request body
    if (!groupName) {
      return res.status(400).json({ message: "Group name is required" });
    }

    // Find the group
    const group = await Group.findOne({ name: groupName });

    if (!group) {
      return res.status(404).json({ message: "Group not found" });
    }

    if (docName) {
      // If a document name is provided, delete the specific document in the group
      const result = await Content.deleteOne({
        name: docName,
        groupID: group._id,
      });

      if (result.deletedCount === 0) {
        return res
          .status(404)
          .json({ message: "Document not found in the group" });
      }
    } else {
      // If no document name is provided, delete the group and all documents in the group
      await Group.deleteOne({ _id: group._id });
      await Content.deleteMany({ groupID: group._id });
    }

    res.status(200).json({ message: "Delete operation successful" });
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});

// GET route to fetch symbol from DB - ImageDB
app.get("/api/piktogramm", async (req, res, next) => {
  try {
    const images = await Piktogramm.find({}).lean();
    res.status(200).json(images);
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});

app.get("/api/hsatz", async (req, res, next) => {
  try {
    const hsatz = await Hsatz.find({}).lean();
    res.status(200).json(hsatz);
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});

app.get("/api/psatz", async (req, res, next) => {
  try {
    const psatz = await Psatz.find({}).lean();
    res.status(200).json(psatz);
  } catch (err) {
    next(err);
  }
});

app.get("/api/euhsatz", async (req, res, next) => {
  try {
    const euhsatz = await Euhsatz.find({}).lean();
    res.status(200).json(euhsatz);
  } catch (err) {
    next(err);
  }
});

app.get("/api/hsatz/:ghs_reference_id", async (req, res, next) => {
  try {
    const hsatz = await Hsatz.find({
      ghs_reference_id: req.params.ghs_reference_id,
    }).lean();
    console.log("Here" + hsatz);
    if (hsatz && hsatz.length > 0) {
      res.status(200).json(hsatz);
    } else {
      res.status(404).json({ message: "No matching Hsatz found." });
    }
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});

app.get("/api/psatz/:p_id", async (req, res, next) => {
  try {
    const psatz = await Psatz.findById(req.params.p_id).lean();
    console.log("Here" + psatz);
    if (psatz) {
      res.status(200).json(psatz);
    } else {
      res.status(404).json({ message: "No matching Psatz found." });
    }
  } catch (err) {
    next(err); // Pass error to error handling middleware
  }
});

// Error Handling Middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  // in a development environment, sending the detailed error
  if (process.env.NODE_ENV === "development") {
    res.status(500).send(err.message);
  } else {
    // in a production environment, a generic error message
    res.status(500).send("Internal Server Error");
  }
});

app.listen(port, () => console.log(`Server running on port ${port}`));
