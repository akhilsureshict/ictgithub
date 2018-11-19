const http=require("http");
const server=http.createServer(function(req,res){
    res.write("hello world");//write response to client
    res.end();//end the response
});
server.listen(3000);
console.log('listening on 3000');