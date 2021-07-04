# ! /usr/bin/env python
# Just a very basic script to convert given text into Leet Speak

import sys
import random


def apply_leet(string):
    string = string.strip()
    for char in string:
        if char == 'a' and random.uniform(0, 1) > 0.5:
            string = string.replace('a', '4')
        elif char == 'b' and random.uniform(0, 1) > 0.5:
            string = string.replace('b', '8')
        elif char == 'e' and random.uniform(0, 1) > 0.5:
            string = string.replace('e', '3')
        elif char == 'l' and random.uniform(0, 1) > 0.5:
            string = string.replace('l', '1')
        elif char == 'o' and random.uniform(0, 1) > 0.5:
            string = string.replace('o', '0')
        elif char == 's' and random.uniform(0, 1) > 0.5:
            string = string.replace('s', '5')
        elif char == 't' and random.uniform(0, 1) > 0.5:
            string = string.replace('t', '7')
        else:
            pass

    return string


def main(args):

    if len(args) < 3:
        print("The script needs a number as the first and file path as the second parameter")
        exit(1)

    filename = args[2]

    lines_num = int(args[1])

    f = open(filename, "r")
    # end_file = open(filename + ".l33t", "w")

    lines = f.readlines()
    output = ""

    for number in range(lines_num):
        line = random.choice(lines)
        leet_line = apply_leet(line)

        # end_file.write(leet_line)
        output += leet_line

    f.close()
    # end_file.close()
    print(output)

if __name__ == '__main__':
    main(sys.argv)
