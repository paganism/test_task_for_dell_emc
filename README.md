# This is a solution of Dell EMC test task

## What to do:

You are given with 100 lamps in array [1,2,3,4,5…..99,100].
And also given 100 trained frogs.
Each lamp has an on\off switch.

Each frog jumps on a lamp and turns its switch on/off, in this order:

1.       First frog jumps on each lamp
2.       Second frog jumps directly to the second lamp and then to the 4th lamp, 6th , 8th …
3.       Third frog jumps directly to the third lamp and then to the 6th lamp, 9th , 12th …
4.       Forth frog jumps directly to the forth lamp and then to the 8th lamp, 12th , 16th …
…
100.  The 100th frog jumps directly to the 100th lamp and then gets out

Also you are given a supplied function that presses a lamp number (i): press(i)
Please write an algorithm or code that will imitate the jumping frogs, using the given function press(i).
After that, take all lamps status as a binary number of 100 bits and return the hex value of it.


# How to run on linux

```
(.venv) user@server: $ python3 frogs.py
```

# Project Goals
The code is written for educational purposes.
