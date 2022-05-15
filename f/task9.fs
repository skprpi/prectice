open System

// 23.4.1
let (.+.) x y =
    let x1, x2, x3 = x
    let y1, y2, y3 = y
    let z3 = x3 + y3
    let z2 = (x2 + y2) + z3 / 12
    let z1 = (x1 + y1) + z2 / 20
    (z1, z2 % 20, z3 % 12)

let (.-.) x y = 
    let x1, x2, x3 = x
    let y1, y2, y3 = y
    let r = (x1 - y1) * 20 * 12 + (x2 - y2) * 12 + (x3 - y3)
    let z1 = r / 20 / 12
    let r1 = r - z1 * 12 * 20
    let z2 = r1 / 12
    let z3 = r1 % 12
    (z1, z2, z3)

// 23.4.2
let (.+) x y =
    let a, b = x
    let c, d = y
    (a + c, b + d)

let (.-) x y =
    let a, b = x
    let c, d = y
    (a, b) .+ (-c, -d)

let (.*) x y =
    let a, b = x
    let c, d = y
    (a * c - b * d, b * c + a * d)

let (./) x y =
    let a, b = x
    let c, d = y
    (a, b) .* (c / (c * c + d * d), -d / (c * c + d * d))
