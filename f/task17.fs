open System

// 43.3
let try_find key m =
    let lst = Map.toList m
    let rec helper xs =
        if xs = [] then
            None
        else
            let h :: t = xs
            let a, b = h
            if a = key then
                Some(b)
            else
                helper t
    helper lst
