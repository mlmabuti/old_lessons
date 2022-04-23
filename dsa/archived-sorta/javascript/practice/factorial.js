function findFactorialRecursive(number) {
  if(number === 2) {
    return 2;
  }
  return number * findFactorialRecursive(number - 1)
}

function findFactorialIterative(number){
  let total = 1;
  for (let i = 2; i <= number; i++) {
    total *= i;
  }
  return total;
}

let a = findFactorialIterative(5);
let b = findFactorialRecursive(5);
console.log(a,b);