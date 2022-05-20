open System

// 39.1
let rec rmodd = function
 | [] -> []
 | h1 :: h2 :: t -> h2 :: rmodd t
 | h1 :: t -> []

// 39.2
let rec del_even = function
 | [] -> []
 | h :: t when (not (h % 2 = 0)) -> h :: del_even t
 | h :: t -> del_even t

// 39.3
let rec multiplicity x xs =
 match xs with
 | [] -> 0
 | h :: t -> (if x = h then 1 else 0) + (multiplicity x t)

// 39.4
let rec split = function
 | [] -> ([], [])
 | h1 :: h2 :: t ->
     let res = split t
     let r1, r2 = res
     (h1 :: r1, h2 :: r2)
 | h1 :: t -> ([h1], [])

exception NotEaqualLength

// 39.5
let rec zip (xs1, xs2) =
 match [xs1; xs2] with
 | [[]; []] -> []
 | [h1 :: t1; h2 :: t2] -> (h1, h2) :: zip (t1, t2)
 | _ -> raise NotEaqualLength
