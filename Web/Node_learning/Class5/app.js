const http =require("http");
const myfunction=require("./syntax")
const runtime=require("./runtime")

var name="sameer shrinath";
const server= http.createServer((req,res)=>{
    // runtime(); This will cause runtime error
    // myfunction(); this will cause syntax error

    if (req.url==='/check'){
        console.log("inside check");
        res.setHeader("Content-Type","text/html");
        res.write(`
            <html>
            <body><h1>hello ${name}</h1>
            <p>The result of the calculation is ${result}</p>
            </body>
            </html>
            `)
        res.end();

    }
});

server.listen(3000,()=>{
    console.log("listening on the port of http://localhost:3000");
});
//syntax errors
