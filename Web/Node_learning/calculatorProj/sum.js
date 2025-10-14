const sumRequesthandler=(req,res)=>{

const body=[];
req.on('data',chunk=>{
    body.push(chunk);
    console.log(chunk);
});
req.on('end',()=>{
    console.log(`THis is body : ${body} ${typeof(body)}`);


    const bodystr=Buffer.concat(body).toString();
    console.log(`THis is bufferrstr : ${bodystr} ${typeof(bodystr)}`);


    const params=new URLSearchParams(bodystr);
    console.log(`THis is params : ${params} ${typeof(para)}`);


    const bodyObj=Object.fromEntries(params);
    console.log(`THis is bodyObj : ${bodyObj}`);


    const result=Number(bodyObj.first)+Number(bodyObj.second);

    res.setHeader('Content-Type','text/html');
    res.write(`<html>
        <title>${result}</title>
        <body>
        <h1>The response is ${result}</h1>
        </body>
        </html>`)
})
}
module.exports=sumRequesthandler;