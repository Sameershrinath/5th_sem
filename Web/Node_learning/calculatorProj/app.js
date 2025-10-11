const http=require('http');
const requesthandler=require('./handler')
const server=http.createServer(requesthandler);

server.listen(3000);