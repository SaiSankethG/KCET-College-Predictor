// var sumbmit=document.getElementById("submit")

// sumbmit.onclick =function(){
//     var name=document.getElementById("firstname").value;
//     var rank=document.getElementById("rank").value;
//     console.log(name)
//     console.log(rank)
//     document.getElementById("output").innerText=name;
//     document.getElementById("output").innerText=rank;

// }
const spawner =require(child_process).spwan;
//string
const data_to_pass_in='send this to python script';
console.log('Data sent to python script' , data_to_pass_in);
const python_process=spawner('python' , ['./python.py' , data_to_pass_in]);
python_process.stdout.on('data', (data)=>{
    console.log('Data received from python script:' , data.toString());
});