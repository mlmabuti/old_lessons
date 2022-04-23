function binarySearch(arr, val) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const middle = Math.floor((left + right) / 2);

    if (arr[middle] === val) return middle;

    if (arr[middle] > val) right = middle - 1;
    else left = middle + 1;
  }

  return -1;
}
