function pow(n,x){
    if (x < 2) return n;
    x--;
    return n * pow(n,x);
}

console.log(pow(3,3));