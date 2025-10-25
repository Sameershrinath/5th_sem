const express = require("express");


const app=express();

app.use(express.urlencoded());

app.use((req,res,next)=>{
console.log("authentication done");
next();})

app.use((req,res,next)=>{
console.log("database connected...");
next();})

app.use((req,res,next)=>{
if (req){
    console.log(`redirecting to ${req.url}`)
}
next();})


app.get("/",(req,res,next)=>{
    res.send(`
        <h1>This is the Home page</h1>
        `)
})

app.get("/contact",(req,res,next)=>{
    res.send(`
        <h1>This is the contact page</h1> <br>
        <form action="/contact" method="POST">
        <input type="text" name="userName" placeholder="Enter your Name"><br>
        <input type="number" name="userNumber" placeholder="Enter your Number"><br>
        <button type="submit">Submit</button>
        </form>
        `)
})


app.post("/contact",(req,res,next)=>{
    const {userName,userNumber}=req.body;
    console.log(userName,userNumber);
    res.send('<h1>submitted data</h1>')
})


app.listen(3000,()=>{
    console.log("This app is running on the http://localhost:3000")
})