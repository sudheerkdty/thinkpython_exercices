import math

def estimate_pi():
    
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        nume = math.factorial(4*k) * (1103 + 26390*k)
        deno = math.factorial(k)**4 * 396**(4*k)
        term = factor * nume / deno
        total += term
        
        if abs(term) < 1e-15: break
        k += 1

    return 1 / total
print """Value of pi using\nFormula\t\tmath.pi\t\tDifference\n%f\t%f\t%f\t"""%(estimate_pi(),math.pi,(estimate_pi()-math.pi))
