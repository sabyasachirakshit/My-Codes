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
const Data = new mongoose.model("mymongoosecollection",dataSchema);

