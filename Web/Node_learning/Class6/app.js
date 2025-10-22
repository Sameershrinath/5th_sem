//core module
//local module if any 
//external module

const express=require('express')

const app=express();

app.use("/",(req,res,next)=>{
    console.log("came in the first middleware",req.url,req.method);
    next();
});

app.use("/product",(req,res,next)=>{
    console.log("came in the second middleware",req.url,req.method);
    res.send(`<h1>This is my product page.</h1>`);
});

app.listen(3000,()=>{
    console.log("Server started on the http://localhost:3000")
})