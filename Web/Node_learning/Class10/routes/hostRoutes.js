const express=require('express')
const path =require("path")

const hostRoutes=express.Router()

hostRoutes.get("/contact",(req,res,next)=>{
    res.sendFile(path.join(__dirname,"../views","contact.html"));
})

module.exports=hostRoutes;