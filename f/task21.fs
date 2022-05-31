open System

let rec factorial = function
    | (n, p) when n < 2 -> p
    | (n, p) -> factorial (n - 1, p * n)

// 50.2.1
let fac_seq = function
    | n -> seq { for i in 1..(n + 1) do yield factorial (i - 1, 1) }

// 50.2.2
let seq_seq = function
    | n -> seq { for i in 1..(n + 1) do yield (i / 2 * -1 * (if i % 2 = 1 then -1 else 1)) }
