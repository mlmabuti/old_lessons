function quickSort(array, left, right){
  let pivot;
  let partitionIndex;
  if(left < right) {
    pivot = right;
    partitionIndex = partition(array, pivot, left, right);
    
    //sort left and right
    quickSort(array, left, partitionIndex - 1);
    quickSort(array, partitionIndex + 1, right);
  }
  return array;
}
   
function partition(array, pivot, left, right){
  let pivotValue = array[pivot];
  let partitionIndex = left;

  for(let i = left; i < right; i++) {
    if(array[i] < pivotValue){
      swap(array, i, partitionIndex);
      partitionIndex++;
    }
  }
  swap(array, right, partitionIndex);
  return partitionIndex;
}

function swap(array, firstIndex, secondIndex){
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
}

//Select first and last index as 2nd and 3rd parameters
let numbers = [9,4,2,3,6,8,1,0,-4];
quickSort(numbers, 0, numbers.length - 1);
console.log(numbers);

//USING ARRAY METHODS
//function quick_Sort(origArray) {
//	if (origArray.length <= 1) { 
//		return origArray;
//	} else {
//
//		var left = [];
//		var right = [];
//		var newArray = [];
//		var pivot = origArray.pop();
//		var length = origArray.length;
//
//		for (var i = 0; i < length; i++) {
//			if (origArray[i] <= pivot) {
//				left.push(origArray[i]);
//			} else {
//				right.push(origArray[i]);
//			}
//		}
//
//		return newArray.concat(quick_Sort(left), pivot, quick_Sort(right));
//	}
//}
//
//var myArray = [3, 0, 2, 5, -1, 4, 1 ];
//
//console.log("Original array: " + myArray);
//var sortedArray = quick_Sort(myArray);
//console.log("Sorted array: " + sortedArray);