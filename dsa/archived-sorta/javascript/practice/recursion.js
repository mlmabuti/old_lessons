function countdown(num){
    if(num === 0) return 0; //base case
    console.log(num);
    num--;
    return countdown(num); 
}
console.log(countdown(5));