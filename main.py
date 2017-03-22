from PrimeTests import PrimeTests
from Utils import get_number

while True:
    test = int(input('Please choose test:\n 1. Fermat \n 2. Miller–Rabin \n 3. Solovay–Strassen\n 4. Exit \n'))
    l = int(input('Please input number of bits: \n'))
    r = int(input('And rounds: \n'))
    n = get_number(l)
    print(n, r, PrimeTests.run(n, r, test), '\n')
