"""
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
"""

NUM_OF_FROGS  = 100
NUM_OF_LAMPS = 100
LAMP_STATES = {x:0 for x in range(1, NUM_OF_LAMPS+1)}

def press(i):
    if LAMP_STATES[i] == 0:
        LAMP_STATES[i] = 1
    else:
        LAMP_STATES[i] = 0


def frogs_jumping (NUM_OF_FROGS , NUM_OF_LAMPS ):
    for  frog_number in range(1, NUM_OF_FROGS  + 1):
        for  lamp_number in range( frog_number, NUM_OF_LAMPS  + 1,  frog_number):
            press(lamp_number)


def get_hex_number_of_lamp_status(LAMP_STATES):
    return format(int(''.join(str(x) for x in LAMP_STATES.values())), 'X')


if __name__ == '__main__':
    frogs_jumping(NUM_OF_FROGS, NUM_OF_LAMPS )
    binary_num = get_hex_number_of_lamp_status(LAMP_STATES)
    print(binary_num)
