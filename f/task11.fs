open System

type F = 
  | AM
  | PM

type TimeOfDay = { hours : int; minutes : int; f: F }

let minutes (x: TimeOfDay) =
   ((if x.f = PM then (x.hours + 12) else x.hours) * 60 + x.minutes) % (24 * 60)

let (.>.) x y = minutes(x) > minutes(y)
