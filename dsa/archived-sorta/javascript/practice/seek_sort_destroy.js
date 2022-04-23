function sort(arr){
    for(let i = 0; i < arr.length; i++){
        for(let j = 1; j < arr.length-i;j++){
            if(arr[j] < arr[j-1]){
                arr = swap(arr,j,j-1);
            }
        }
    }
    return arr;
}

function swap(arr,j,j1){
    temp = arr[j];
    arr[j] = arr[j-1];
    arr[j-1] = temp;
    return arr;
}

function seek_destroy(arr, e){
    for(let i = 0; i < arr.length; i++){
        if(arr[i] === e){
            arr.pop(i);
        }
    }
    return arr;
}

function main(){
    arr = [6,7,3,1,2,4,5,6,8,0,-1,6];
    arr = sort(arr);
    arr = seek_destroy(arr, 6);
    console.log(arr);
}

main();