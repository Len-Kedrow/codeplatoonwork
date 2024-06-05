const factorial = (num) => {
  if (num === 0) {
    return 1
  } else {
    return num * factorial(num - 1)
  }
}

console.log(factorial(9))
console.log(factorial(0))
console.log(factorial(3))


module.exports = factorial
