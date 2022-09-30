import sys
import argparse 

# todo: make it so chars print depending on where in the wave.  ie peak = ^, trough = v, etc
# todo: could use these unicode Geometric Shapes 
# todo ◟◜◝◞
# https://unicode-explorer.com/c/25DE
# wild  
# python sinprint.py --amp 10 --length 20 --verbose --char '◟◜◝◞'
# python sinprint.py --amp 10 --length 20 --verbose --char '◾'

# * sinPrint: prints a sin wave 
def sinPrint(amp, length, char):
    innerSpace = 1 
    outerSpace = 2

    for i in range(1, amp + 1):

        for j in range(1, length + 1):

            for k in range(1, outerSpace + 1):
                print(end = " ")

            print(char, end = "")

            for k in range(1, innerSpace + 1):
                print(end = " ")

            print(char, end = "")

            for k in range( 1, outerSpace + 1):
                print(end = " ")

            print(end = " ") 

        if (i + 1 != amp):
            outerSpace = 1
        else:
            outerSpace = 0

        if (i + 1 != amp):
            innerSpace = 3
        else: 
            innerSpace = 5

        print()

parser = argparse.ArgumentParser()
parser.add_argument("--amp", help="sin wave amplitude", type=int, default=4) 
parser.add_argument("--length", help="length of wave to print", type=int, default=10)
parser.add_argument("--verbose", help="print verbosely", action="store_true")
parser.add_argument("--char", help="char to use", default="*")

args = parser.parse_args()
if args.verbose:
    print("parsed args: ")
    for arg in args._get_kwargs():
        print(f"{arg[0]}={arg[1]}")

sinPrint(args.amp, args.length, args.char)

