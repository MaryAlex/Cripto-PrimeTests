from TestMapping import TestMapping
from PrimeTests import PrimeTests

n = 5
r = 3
while True:
    n += 1
    r += 1
    test = int(input('Please choose test:\n 1. Fermat \n 2. Miller–Rabin \n 3. Solovay–Strassen\n 4. Exit \n'))
    print(n, r, PrimeTests.run(n, r, test))
