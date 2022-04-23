//IN PROGRESS
//IN PROGRESS
//IN PROGRESS
//IN PROGRESS
function pop(arr, index){
    let newArr = new Array(arr.length-1);
    for(let i = 0, j = 0; i < newArr.length;i++,j++){
        newArr[i] = arr[j];
        if(i === index) newArr[i] = arr[++j];
    }return newArr;
}

function findDuplicates(arr){
    for(var i = 0; i < arr.length; i++){
        for(var j = i+1; j < arr.length; j++){
            if(arr[i] === arr[j]){
                console.log("found duplicate")
                arr = pop(arr,j);
            }
        }
    } 
}

let arr = [5,2,1,2,3,4,5,6,1];
console.log(arr)