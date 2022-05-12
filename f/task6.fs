open System

// 17.1
let rec pow = function
 | (s, 0) -> ""
 | (s, n) -> s + pow (s, n - 1)

// 17.2
let rec isIthChar = function
 | (s, n, c) when n >= String.length s -> false
 | (s, n, c) -> (string s).[n] = c

// 17.3
let rec occFromIth = function
 | (s, n, c) when n >= String.length s -> 0
 | (s, n, c) when (string s).[n] = c -> 1 + occFromIth(s, n + 1, c)
 | (s, n, c) -> occFromIth(s, n + 1, c)
