const express=require('express')
const path =require("path")

const userRoutes=express.Router()

userRoutes.get("/",(req,res,next)=>{
    res.sendFile(path.join(__dirname,"../views","index.html"));
})

module.exports=userRoutes;

