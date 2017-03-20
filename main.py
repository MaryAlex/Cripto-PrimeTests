from TestMapping import TestMapping
from PrimeTests import PrimeTests

n = 5
r = 3
while True:
    n += 1
    r += 1
    test = int(input('Please choose test:\n 1. Fermat \n 2. Miller–Rabin \n 3. Solovay–Strassen\n 4. Exit \n'))
    if test == TestMapping.Fermat.value:
        print(n, r, PrimeTests.Fermat(n, r))
    elif test == TestMapping.MillerRabin.value:
        print(n, r, PrimeTests.Miller_Rabin(n, r))
    elif test == TestMapping.SolovayStrassen.value:
        print(n, r, PrimeTests.Solovay_Strassen(n, r))
    elif test == TestMapping.Exit.value:
        break
    else:
        print('Wrong input')
