# DateNine - a Grammar of Dates

## What's datenine and how is it different?

I needed a simple way to describe recurring times, so I looked into different approaches.
Schedule is a nice enough python package, but it actually *schedules* events - I only need to describe a date that may be months or years away
and calculate its future timestamp from the description.

The simplest case is, I have a birthdate I need to remember and I want to say "give me the timestamp that corresponds to 2 days before the next birthday"
Which is remarkably difficult in other approaches for a simple task like this.

So, what would this usecase look like in datenine?
Date(1992,5,25) * year() - day(2)

This means: the fixed Date * every year - two days before the next date
Multiplication means "every", - or + shifts the date from the next occurrence and you can add modifiers or constraints to each part.

