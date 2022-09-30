
# todo: make it so chars print depending on where in the wave.  ie peak = ^, trough = v, etc
# prints a sin wave of amp and length to term
def sinPrint(amp, length):
    innerSpace = 1 
    outerSpace = 2

    for i in range(1, amp + 1):

        for j in range(1, length + 1):

            for k in range(1, outerSpace + 1):
                print(end = " ")

            print("-", end = "")

            for k in range(1, innerSpace + 1):
                print(end = " ")

            print("-", end = "")

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

# drive
amp, length = 5, 20

sinPrint(amp,length)


