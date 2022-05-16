# Python program to demonstrate
# sys.argv
  
import sys

def to_int(arg):
    try:
        return int(arg)
    except ValueError: 
        print(f'{arg} is not an integer')
        exit(0)
  
def to_real(arg):
    try:
        return float(arg)
    except ValueError: 
        print(f'{arg} is not a real number')
        exit(0)
  
if len(sys.argv) < 3:
    print(f'usage: {sys.argv[0]} no iter')
else:   
    no_arg = sys.argv[1]
    iter_arg = sys.argv[2]
    print(f'square root of {no_arg} with {iter_arg} iterations')
    no = to_real(no_arg)
    iter = to_int(iter_arg)
    guess = no / 2
    for i in range(iter):
        print(f'iter {i} guess {guess}')
        guess = (guess + no / guess) / 2
    print(f'final  guess {guess}')
