open System

let rec upto = 
    let rec helper i n =
        if i <= n then (i :: helper (i + 1) n) else []
    helper 1

let rec dnto = function
 | n when n > 0 -> n :: dnto (n - 1)
 | _ -> []

let rec evenn = 
    let rec helper i n =
        if n > 0 then (i :: helper (i + 2) (n - 1)) else []
    helper 0
