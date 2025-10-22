//learning the sync and async operation 

const fs= require('fs');
console.log('1. start of the script');

console.log('2. reading file sunchronously');
const dataSync=fs.readFileSync('user-detail.txt','utf8');
console.log('3. Synchronous read complete');

console.log('4. Reading the file asynchronouslly');
fs.readFile('user-detail.txt','utf8',(err,dataAsync)=>{
    if (err) throw err;
    console.log('6. Asynchronous read complete');
});

console.log('5.End of script');