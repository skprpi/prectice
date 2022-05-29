open System

// 47.4.1
let f n =
    let mutable fact = 1
    let mutable k = 2
    while k <= n do
        fact <- fact * k
        k <- k + 1
    fact

// 47.4.2
let fibo n =
    let mutable fib1 = 0
    let mutable fib2 = 1
    let mutable i = 1
    if n = 0 then
        fib2 <- 0
    while i < n do
        let tmp = fib2 + fib1
        fib1 <- fib2
        fib2 <- tmp
        i <- i + 1
    fib2
