function countdown(n){
    if (n === 0){
        console.log(0);
        return null;
    }
    console.log(n);
    return countdown(n-1)
}
countdown(3)