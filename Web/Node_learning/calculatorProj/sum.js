const sumRequesthandler=(req,res)=>{
console.log("in sum request handler")
const body=[];
req.on('data',chunk=>{body.push(chunk)});
req.on('end',()=>{
    const bodystr=Buffer.concat(body).toString();
    const params=new URLSearchParams(bodystr);
    const bodyObj=Object.fromEntries(params);
    const result=Number(bodyObj.first)+Number(bodyObj.second);
    res.setHeader('Content-Type','text/html');
    res.write(`<html><title>${result}</title><body>The response is ${result}</body></html>`)
})
}
module.exports=sumRequesthandler;