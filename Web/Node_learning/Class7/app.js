const express = require("express");

const app = express();
app.use(express.urlencoded({ extended: true })); // parses form data


//first middle-ware
app.use((req,res,next)=>{
    console.log(req.url);
    console.log("THis is the first middleware");
    next();
})

//second middle-ware
app.get("/",(req,res,next)=>{
    console.log(req.method);
    console.log("THis is the second middleware");
    next();
})

//third middle-ware
app.get("/",(req,res,next)=>{
    console.log("This is the third middleware");
    res.send(`<h1>Welcome to the home page.</h1><br>
        <a href="/contact">Contact us</a>
        `);
})

app.get("/contact",(req,res,next)=>{
    res.send(`
        <h2>Contact Us</h2>
  <form action="/contactus" method="post">
    <label for="name">Name:</label><br>
    <input type="text" id="name" name="name" required><br><br>

    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email" required><br><br>

    <button type="submit">Submit</button>
  </form>
        `)
});


app.post("/contactus",(req,res,next)=>{
    console.log("details posted",req.body);

})



app.listen(3000,()=>{
    console.log("Server started on the http://localhost:3000");
})