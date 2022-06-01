open System

// 50.2.1
let fac_seq =
    let rec helper i res n =
        match i with
            | x when x = n -> seq {yield res}
            | x -> seq { yield res; yield! (helper (x + 1) (res * (x + 1)) n ) }
    helper 0 1

// 50.2.2
let seq_seq =
    let rec helper i n =
        match i with
            | x when x = n -> seq {yield ((x + 1) / 2 * -1 * (if x % 2 = 0 then -1 else 1))}
            | x -> seq {
                yield ((x + 1) / 2 * -1 * (if x % 2 = 0 then -1 else 1))
                yield! (helper (x + 1) n) 
            }
    helper 0
