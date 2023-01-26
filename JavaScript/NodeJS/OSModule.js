const os = require("os");

console.log(os.arch());

const freeMemory = os.freemem();
console.log(`FreeMemory=${freeMemory / 1024 / 1024 / 1024}`);

const totMemory = os.totalmem();
console.log(`TotalMemory=${totMemory / 1024 / 1024 / 1024}`);

console.log(`HostName: ${os.hostname()}`);

console.log(`Working on platform: ${os.platform()}`);

console.log("Temporary Files stored in location - " + os.tmpdir());
console.log("Working on System -" + os.type());
