function fibonacciRecursive(n) {
  if (n < 2) return n;
  return fibonacciRecursive(n - 1) + fibonacciRecursive (n - 2);
}
