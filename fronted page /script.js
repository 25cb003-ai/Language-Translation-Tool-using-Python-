function copyText(){

var copy=document.getElementById("output");

copy.select();

document.execCommand("copy");

alert("Copied Successfully");

}
