open System

type TimeOfDay = { hours: int; minutes: int; f: string }

let (.>.) x y =
    let m1 = (if x.f = "PM" then (x.hours + 12) else x.hours) * 60 + x.minutes
    let m2 = (if y.f = "PM" then (y.hours + 12) else y.hours) * 60 + y.minutes
    m1 % (24 * 60) > m2 % (24 * 60)
