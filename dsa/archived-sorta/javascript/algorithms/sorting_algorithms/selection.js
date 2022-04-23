function selectionSort(arr){
  for(var i =0; i < arr.length; i++){
    let lowest = i;
    for(var j = i +1; j < arr.length;j++){
      if (arr[i] > arr[j]){
        lowest = j;
        let temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
    }
  }
  return arr;
}

console.log(selectionSort([10,2,3,5,6,1,2,4,6,-2,-1,-2]));

//function selectionSort(array) {
//  const length = array.length;
//  for(let i = 0; i < length; i++){
//    // set current index as minimum
//    let min = i;
//    let temp = array[i];
//    for(let j = i+1; j < length; j++){
//      if (array[j] < array[min]){
//        //update minimum if current is lower that what we had previously
//        min = j;
//      }
//    }
//    array[i] = array[min];
//    array[min] = temp;
//  }
//  return array;
//}
