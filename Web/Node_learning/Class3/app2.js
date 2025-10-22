console.log('1. start of the script');

Promise.resolve().then(() => console.log('2. Microtask 1'));

setTimeout(()=> console.log('3. Timer 1'),0);


setImmediate(()=>console.log('5. Immediate 1'));

const fs = require('fs');
fs.readFile('user-details.txt',()=>console.log('4. I.O operation'));


process.on('exit', (code)=>{
    console.log('6. Exit event');
});

console.log('7 end of the script')


// 1. start of the script
// 7 end of the script
// 2. Microtask 1
// 3. Timer 1
// 4. I.O operation
// 5. Immediate 1
// 6. Exit event