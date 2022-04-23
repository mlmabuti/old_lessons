//does not work when there are 3 identical integers.

let arr = [1,2,3,1,2,5,5,3]
function findNumberOfDuplicates(){
    ctr = 0;
    for(let i = 0; i < arr.length; i++){
        for(let j = i+1; j < arr.length; j++){
            if (arr[i] == arr[j]){
                ctr++;
            }
        }
    }
    return ctr;
}
console.log(findNumberOfDuplicates(arr));