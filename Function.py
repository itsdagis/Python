def checknumber(q, p): 
    if q == p:
        return q, p
    else:
        return 0, 0  # Ensure it always returns a tuple

def add(num1, num2):
    e, f = checknumber(num1, num2)
    z = e + f
    return z

def main(x, y):
   a = add(x, y)
   return a

x = main(10, 20)
print(x)  # Output should be 40

