open System

// 50.2.1
let fac_seq =
    seq {
        let mutable i = 0
        let mutable result = 1
        while true do
            result <- result * (if i = 0 then 1 else i)
            i <- i + 1
            yield result
    }

// 50.2.2
let seq_seq =
    seq {
        let mutable x = 0
        while true do
            yield ((x + 1) / 2 * -1 * (if x % 2 = 0 then -1 else 1))
            x <- x + 1
    }
