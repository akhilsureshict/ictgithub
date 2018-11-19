const fs=require('fs');
//using synchronous//
const files=fs.readdirSync('/');
console.log(files);