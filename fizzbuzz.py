import sys

def fizzbuzz(n):
    for i in range(1, n):
        if i % 6 == 0:
            print "FizzBuzz"
        elif i % 2 == 0:
            print "Fizz"
        elif i % 3 == 0:
            print "Buzz"
        else:
            print i
if len(sys.argv) > 1:
    fizzbuzz(int(sys.argv[1]))
