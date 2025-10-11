const sumRequesthandler=require('./sum')

const requesthandler= (req,res)=>{
    console.log(req.url);
    if (req.url==='/'){
        res.setHeader('Content-Type','text/html');
        res.write('<html><title>Calculator</title><body><h1>Welcome to the calculator</h1><a href="http://localhost:3000/calculator">Enter to open Calc</a></body></html>')
    }
    if (req.url.toLowerCase() ==='/calculator'){
        res.setHeader('Content-Type','text/html');
        res.write(`<html><title>Calculator</title><body><h1>This is the calculator page.</h1>
            <form action="/calculate-result" method="POST">
            <input type="text" placeholder="First number" name="first" />
            <input type="text" placeholder="Second number" name="second" />
            <input type="submit" value="sum">
            </form>
            </body></html>`)
        return res.end();
    }
    else if (req.url==='/calculate-result' && req.method=="POST"){
        sumRequesthandler(req,res);
    }

}
module.exports=requesthandler;