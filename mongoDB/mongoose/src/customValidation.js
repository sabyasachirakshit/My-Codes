const mongoose = require("mongoose");
mongoose
  .connect("mongodb://localhost:27017/mydatabase")
  .then(() => console.log("Connection successfull"))
  .catch((err) => console.log(err));

const dataSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    trim: true, //removes all leading and trailing spaces
    minlength: [2, "Minimum two letters should be present"],
    maxlength: 30,
  },
  ctype: {
    type: String,
    enum: ["Frontend", "Backend", "Database"],
  },
  rating: Number,
  author: String,
  active: Boolean,
  date: {
    type: Date,
    default: Date.now,
  },
});

const Data = new mongoose.model("mytestcollection", dataSchema);

//Creating/Inserting document in collection
const createDocs = async () => {
  try {
    // const expressJS = new Data({
    //   name: "Express JS",
    //   ctype: "Backend",
    //   rating: 100,
    //   author: "Ezio Auditore",
    //   active: true,
    // });
    const mongoDB = new Data({
      name: "Mongo DB",
      ctype: "Database",
      rating: 95,
      author: "Aiden Pearce",
      active: true,
    });
    const mongooseData = new Data({
      name: "Mongoose Package",
      ctype: "Database",
      rating: 99,
      author: "Shay Cormac",
      active: true,
    });
    const JS = new Data({
      name: "Js",
      ctype: "Frontend",
      rating: 100,
      author: "Sabyasachi Rakshit",
      active: true,
    });
    const result = await Data.insertMany([mongoDB, mongooseData, JS]);
    console.log(result);
  } catch (err) {
    console.log(err);
  }
};

createDocs();
