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
createDocs();

//Reading Documents from collection

const getDocs = async () => {
  try {
    const result = await Data.find();
    //   const result = await Data.find({active:true}).select({name:1}).limit(1);
    console.log(result);
    console.log(typeof result);
  } catch (err) {
    console.log(err);
  }
};

getDocs();
