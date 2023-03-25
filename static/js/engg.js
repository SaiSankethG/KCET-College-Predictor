const spawner =require(child_process).spwan;
//string
const data_to_pass_in='send this to python script';
console.log('Data sent to python script' , data_to_pass_in);
const python_process=spawner('python' , ['./python.py' , data_to_pass_in]);
python_process.stdout.on('data', (data)=>{
    console.log('Data received from python script:' , data.toString());
});

window.addEventListener("load", function() {
alert(
"Note:\nThese results are purely based on KCET 2021 2nd EXTENDED ROUND CUTTOFF\nCuttoff's may vary due to change in the number of seats and newly added branches like - Artificial intelligence,  Cyber security, Data science </b>in some colleges");
});

