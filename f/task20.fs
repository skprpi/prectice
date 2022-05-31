open System

// 49.5.1
let even_seq = Seq.initInfinite (fun n -> 2 * n + 2)

let rec factorial = function
    | (n, p) when n < 2 -> p
    | (n, p) -> factorial (n - 1, p * n)

// 49.5.2
let fac_seq = Seq.initInfinite (fun n -> factorial (n, 1))

// 49.5.3
let seq_seq = Seq.initInfinite (fun n -> (n + 1) / 2 * (-1 * (if n % 2 = 1 then 1 else -1)))
