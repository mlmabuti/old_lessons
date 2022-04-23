//reverse a string.

var string = "Hello world.";

function reverseString(string){
	let newString = "";
	for(let i = string.length-1; i >= 0; i--){
		newString += string[i];
	}
	return newString;
}

console.log(reverseString(string));


//not mine
function reverse1(str){
  if(!str || typeof str != 'string' || str.length < 2 ) return str;
  
  const backwards = [];
  const totalItems = str.length - 1;
  for(let i = totalItems; i >= 0; i--){
    backwards.push(str[i]);
  }
  return backwards.join('');
}

function reverse2(str){
  //check for valid input
  return str.split('').reverse().join('');
}

const reverse3 = str => [...str].reverse().join('');