open System

let curry f: int -> int ->int =
    let g x =
        let h y =
            f (x, y)
        h
    g

let uncurry g: int * int -> int = 
    let f (x, y) =
        let h = g x
        h y
    f
