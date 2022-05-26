open System

// 41.4.1
let list_filter f xs =
    List.foldBack (fun a b -> if f(a) then a :: b else b) xs []

// 41.4.2
let sum (p, xs) =
    let data = list_filter p xs
    List.fold (fun a b -> a + b) 0 data

// 41.4.3
let revrev = function
  | [] -> []
  | xs -> List.fold (fun a b -> [List.rev b] @ a) [] xs
