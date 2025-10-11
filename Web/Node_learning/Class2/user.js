const fs=require('fs');


const userRequestHandler=(req,res)=>{
    if(req.url==='/'){
        res.setHeader('Content-Type','text/html');
        res.write('<html>');
        res.write('<head><title>Complete coding</title><head>');
        res.write('<body>');
        res.write('<form action="/submit-details" method="POST">');
        res.write('<label for="username">Username:</label>');
        res.write('<input type="text" id="username" name="username" required><br>');
        res.write('<label for="gender">Gender:</label>');
        res.write('<select id="gender" name="gender" required>');
        res.write('<option value="">Select</option>');
        res.write('<option value="male">Male</option>');
        res.write('<option value="female">Female</option>');
        res.write('<option value="other">Other</option>');
        res.write('</select><br>');
        res.write('<button type="submit">Submit</button>');
        res.write('</form>');
        res.write('</body>');
        res.write('</html>');
    }
    else if (req.url.toLowerCase()==='/submit-details'&& req.method=='POST'){
        const body=[];
        req.on('data',chunk=>{
            console.log(chunk);
            body.push(chunk);
        });
        req.on('end',()=>{
        const fullBody=Buffer.concat(body).toString();
        console.log(fullBody);
        const params=new URLSearchParams(fullBody);
        // const bodyObject={};
        // for (const[key,val] of params.entries()){
        //     bodyObject[key]=val;
        // }
        const bodyObject=Object.fromEntries(params) // same way of doing the above things
        console.log(bodyObject);
        fs.writeFileSync('user.txt',JSON.stringify(bodyObject));
    })
    }
}

module.exports=userRequestHandler;