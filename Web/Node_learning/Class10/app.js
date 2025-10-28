const express = require("express");
const serveIndex = require("serve-index");   

const userRoutes = require("./routes/userRoutes");
const hostRoutes = require("./routes/hostRoutes");
const path = require("path");

const app=express();

app.use(userRoutes);
app.use(hostRoutes);

app.use('/public', express.static(path.join(__dirname, '../../Node_learning')));
app.use(express.static(path.join(__dirname, './public')));
app.use('/public', serveIndex(path.join(__dirname, '../../Node_learning'), { icons: true }));


app.listen(3000,()=>{console.log("app is live on http://localhost:3000 and also at Local_ip:3000")});