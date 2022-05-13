open System

// 20.3.1
let vat n x: float = x + ((float n ) / 100.0 * x)

// 20.3.2
let unvat n x: float = x / (1.0 + (float n) / 100.0)

// 20.3.3
let rec min f =
    let rec minHelper = function
     | (f, n) when f n = 0 -> n
     | (f, n) -> minHelper (f, (n + 1))
    minHelper (f, 1)
