const http= require('http');

// function requestListener(req,res){
//     console.log(req);
// }

const server=http.createServer((req,res)=>{console.log(req.method)});

server.listen(3000);

// you have to run this by node app.js and open the local host in the browser.