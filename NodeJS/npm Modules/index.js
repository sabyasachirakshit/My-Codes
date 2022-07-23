import chalk from "chalk";
import validator from "validator";

console.log(chalk.red.underline.inverse("Hello world!"));
const res = validator.isEmail("sabyasachirakshitacs19@gmail.com");
console.log(res ? chalk.green.inverse(res) : chalk.red.inverse(res));
