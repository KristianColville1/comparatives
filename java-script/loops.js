let a = 23;
let b = 34;
let c = 43534;

// above are three simple integer variables

// below is a for loop

for(let i = 1; i < a; i++){
    console.log('printing..');
}

// below is a while loop

while(a < c){
    a += b;
    b += a;
    console.log('printing: ' + a)
}