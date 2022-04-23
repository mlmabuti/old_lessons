//imaginary main
f(3);
equality();


/**
 * "\'escape sequences'"
 */

/**
 * var = function scoped, changeable
 * let = block scoped, changeable
 * const = constant, unchangeable
 */
function f(x){

  const a = 2; // this value cannot be altered.
  var c = 1;

  for ( i = 0; i < 3 ; i++){
    let c = 2;
    console.log(c + i + a); // 4, 5, 6 (let c in block)
  }
  console.log(c); // 1 (var c in function)
}


/**
 * === : strict comparison, two values must be the exact same values.
 * 
 * == : abstract comparison, different data type values can be equal.
 */
function equality(){
  let a = 2;
  let b = "2";

  if( a === b) // false using strict comparison.
    console.log(true);
  else
    console.log(false);

  if( a == b) // true using abstract comparison.
    console.log(true);
  else
    console.log(false);
}

/**
 * forEach
 */
var someArray = [1,2,3,4,5,6];
someArray.forEach(i =>{
	if(i == 2 || i == 3){
		console.log(i*i);
	}
	console.log(i);	
})

//same thing
var someArray = [1,2,3,4,5,6];
for(let i of someArray){
	if(i == 2 || i == 3){
		console.log(i*i);
	}
	console.log(i);	
}

/**
 * stack: LIFO
 * push()
 * pop()
 * 
 * queue: FIFO
 * shift()
 * unshift()
 */

/**Objects (dictionaries) 
 * 
 */

/**
 * Math.random = random includes fraction
 * Math.floor = round off
 * Math.floor(Math.random * 10) = whole numbers
 */

/**
 * parseInt
 */

/**
 * Ternary operator
 */

/**Classes
 * 
 */
class Player{
	constructor(username){
		this.username = username;
		this.baseStrength = 2;
		this.baseAgility = 3;
		this.baseIntelligence = 2;
	}

	getStats(){
		console.log("Username",this.username);
		console.log("str",this.baseStrength);
		console.log("agt",this.baseAgility);
		console.log("int",this.baseIntelligence);
	}
}

const player1 = new Player("Kite");
player1.getStats();


/**Import export, require
 * 
 */
