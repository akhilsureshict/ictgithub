//exports.myDateTime=function(){
   // return Date();//

//}//defining function within export function.another methord of exporting//
function myDate(){
    return Date();  
}
module.exports.date=myDate//value in myDate() is moved to date//