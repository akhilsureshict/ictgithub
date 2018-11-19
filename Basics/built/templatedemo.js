const os=require('os')
var totMem=os.totalmem();
var freemem=os.freemem();
//using a template string for functions to print the memory avaliable and total memeory//
console.log(`total memory:${totMem}`);
console.log(`free memory:${freemem}`);