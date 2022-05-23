open System

// 40.1
let rec sum (p, xs) = 
    match xs with
      | [] -> 0
      | h :: t -> (if p h then h else 0) + sum (p, t)

// 40.2.1
let rec count (xs, n) =
    match xs with
      | [] -> 0
      | h :: t when h < n -> count (t, n)
      | h :: t when h = n -> 1 + count (t, n)
      | h :: t when h > n -> 0
      | _ -> 0

// 40.2.2
let rec insert (xs, n) =
    match xs with
      | [] -> [n]
      | h :: t when h < n -> h :: insert (t, n)
      | h :: t when h >= n -> n :: xs
      | _ -> [n]

// 40.2.3
let rec intersect (xs1, xs2) = 
    match (xs1, xs2) with
      | ([], _) | (_, []) -> []
      | (h1 :: t1, h2 :: t2) when h1 < h2 -> intersect (t1, h2 :: t2)
      | (h1 :: t1, h2 :: t2) when h1 = h2 -> h1 :: intersect (t1, t2)
      | (h1 :: t1, h2 :: t2) when h1 > h2 -> intersect (h1 :: t1, t2)
      | _ -> []

// 40.2.4
let rec plus (xs1, xs2) =
    match (xs1, xs2) with
      | ([], []) -> []
      | ([], h2 :: t2) -> h2 :: t2
      | (h1 :: t1, []) -> h1 :: t1
      | (h1 :: t1, h2 :: t2) when h1 < h2 -> h1 :: plus (t1, h2 :: t2)
      | (h1 :: t1, h2 :: t2) when h1 = h2 -> h1 :: h2 :: plus (t1, t2)
      | (h1 :: t1, h2 :: t2) when h1 > h2 -> h2 :: plus (h1 :: t1, t2)
      | _ -> []

// 40.2.5
let rec minus (xs1, xs2) =
    match (xs1, xs2) with
      | ([], _) -> []
      | (h1 :: t1, []) -> h1 :: t1
      | (h1 :: t1, h2 :: t2) when h1 < h2 -> h1 :: minus (t1, h2 :: t2)
      | (h1 :: t1, h2 :: t2) when h1 = h2 -> minus (t1, t2)
      | (h1 :: t1, h2 :: t2) when h1 > h2 -> minus (h1 :: t1, t2)
      | _ -> []

// 40.3.1
let rec smallest = function
    | [] -> 999999
    | h :: t when t = [] -> h
    | h :: t ->
        let other = smallest t
        if h > other then other else h

// 40.3.2
let rec delete (n, xs) =
    match (n, xs) with
      | (n, []) -> []
      | (n, h :: t) when h = n -> t
      | (n, h :: t) -> h :: delete (n, t)
      | _ -> []

// 40.3.3
let rec sort = function
    | [] -> []
    | xs ->
        let minVal = smallest xs
        minVal :: sort (delete(minVal, xs))

// 40.4
let rec revrev xs =
    let rec helper = function
      | [] -> []
      | h :: t -> (List.rev h) :: (helper t)
    List.rev (helper xs)
