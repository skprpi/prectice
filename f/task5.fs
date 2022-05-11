// 16.1
let notDivisible = fun (n, m) -> m % n = 0

let rec primeHelper = function
 | (a, b) when b <= 1 -> true
 | (a, b) when a % b = 0 -> false
 | (a, b) -> primeHelper(a, b - 1)

// 16.2
let prime = function
 | n when n <= 1 -> false
 | n -> primeHelper(n, n - 1)
