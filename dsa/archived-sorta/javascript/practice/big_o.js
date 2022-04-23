var array = [5,4,3,2,1];


//Big O of n, Linear time
let x = 3;
for (let i = 0; i < 9; i++) //O(n)
	if ( i === x){
		console.log("i is equal to x");
	}

array.shift(1); //O(n)
array.unshift(2); //O(n)

//Big O of 1, Constant time.	
array[4]; //O(1)
array.length //O(1)
array.pop(); //O(1)

//Big O of n^2, Quadratic time.
var array2 = [[1,2,3],[4,5,6],[7,8,9]]

for(let i = 0 ; i < array2.length; i++){
	for(let j = 0; j < array2[i].length; j++){
		console.log(array2[j][i]);
	}
}


