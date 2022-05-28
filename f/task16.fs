open System

// 42.3
let rec allSubsets n k =
    let rec helper = function
      | (_, 0, ans) -> set[ans]
      | (number, cnt, ans) when number = cnt -> helper(number - 1, cnt - 1, Set.add number ans)
      | (number, cnt, ans) when number > cnt ->
          let res1 = helper(number - 1, cnt - 1, Set.add number ans)
          let res2 = helper(number - 1, cnt, ans)
          Set.union res1 res2
      | _ -> set[set[]]
    helper (n, k, set[])
