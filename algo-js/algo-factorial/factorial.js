const factorial = (num) => {
  if (num === 0){ 
    console.log("we made it")
      return 1 
}

   else {
    console.log(num)
    return num * factorial(num - 1)
  }
}
//console.log(factorial(9))
//console.log(factorial(0))
console.log(factorial(6))


module.exports = factorial

