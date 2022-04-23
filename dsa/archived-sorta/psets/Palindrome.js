
let n = "racecar"

function isPalindrome(n){
    let arr = n.toString(10).split("");
    let c = 0;
    let stringComparator = ""
    for(let j = arr.length-1; j >= 0; j--)
        stringComparator += arr[j]
    if (n == stringComparator)
        return true
    return false
}

console.log(isPalindrome(n))