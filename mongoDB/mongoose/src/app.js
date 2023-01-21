const mongoose = require("mongoose");

//Connection creation and creating a new database if not present
mongoose
  .connect("mongodb://localhost:27017/mydatabase")
  .then(() => console.log("Connection successfull"))
  .catch((err) => console.log(err));

// What is Schema?
//A Mongoose schema defines the structure of the document, default values, validators, etc.

const dataSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  ctype: String,
  rating: Number,
  author: String,
  active: Boolean,
  date: {
    type: Date,
    default: Date.now,
  },
});

//A mongoose model is a wrapper on mongoose schema.
//Collection Creation
const Data = new mongoose.model("mymongoosecollection", dataSchema);

//Creating/Inserting document in collection
const createDocs = async () => {
  try {
    const JS = new Data({
      name: "JS",
      ctype: "FrontEnd+Backend",
      rating: 100,
      author: "Sabyasachi Rakshit",
      active: true,
    });
    const expressJS = new Data({
      name: "Express JS",
      ctype: "Backend",
      rating: 100,
      author: "Ezio Auditore",
      active: true,
    });
    const mongoDB = new Data({
      name: "Mongo DB",
      ctype: "Backend Storage",
      rating: 95,
      author: "Aiden Pearce",
      active: true,
    });
    const mongooseData = new Data({
      name: "Mongoose Package",
      ctype: "Bridge Module between Node JS & Mongo DB",
      rating: 99,
      author: "Shay Cormac",
      active: true,
    });
    const result = await Data.insertMany([
      JS,
      expressJS,
      mongoDB,
      mongooseData,
    ]);
    console.log(result);
  } catch (err) {
    console.log(err);
  }
};
// createDocs();

//Reading Documents from collection

const getDocs = async () => {
  try {
    const result = await Data.find();
    // const result = await Data.find({ ctype: "Backend" }).select({ name: 1, _id: 0 });
    //   const result = await Data.find({active:true}).select({name:1}).limit(1);

    /* Running Queries
    const result = await Data.find({rating:{$gt:80}});
    const result = await Data.find({ ctype: { $in: ["Backend","Backend Storage"] } }).select({
      name: 1,
      _id: 0,
    });
    const result = await Data.find({
      ctype: { $nin: ["Backend", "Backend Storage"] },
    }).select({
      name: 1,
      _id: 0,
    });
    */

    /* Running Logical Operators
    const result = await Data.find({$or:[{ctype:"Backend"},{author:"SR"}]}).select({name:1,_id:0});
    const result = await Data.find({$and: [{ ctype: "Backend" }, { author: "SR" }],}).select({ name: 1, _id: 0 });
    const result = await Data.find({ author: { $not: /SR/ } }).select({
      name: 1,
      _id: 0,
    });
    const result = await Data.find({
      $nor: [{ ctype: "Frontend" }, { author: "SR" }],
    }).select({ name: 1, _id: 0 });
    */

    /* Counting and Sorting 
    const result = await Data.find().count();
    const result = await Data.find()
      .sort({name:-1}) 1 or -1 represents ascending or descending respectively
      .select({ name: 1, _id: 0 });
    console.log(result);
    */

    console.log(typeof result);
  } catch (err) {
    console.log(err);
  }
};

// getDocs();

// Updating documents

const updateDocs = async (objectId) => {
  try {
    const res = await Data.findByIdAndUpdate(
      { _id: objectId },
      { $set: { ctype: "Frontend & Backend" } },
      { new: true }
    );
    console.log(res);
  } catch (err) {
    console.log(err);
  }
};

// updateDocs("62f5e442ec3cccc6f8c7a89e");

// Deleting Documents

const deleteDocs = async () => {
  try {
    const res = await Data.deleteOne({ name: "Node JS" });
    console.log(res);
  } catch (err) {
    console.log(err);
  }
};

deleteDocs();