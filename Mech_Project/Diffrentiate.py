import sympy as sp

x = sp.Symbol('x')
f=x**2 + sp.sin(x)

f_prime = sp.diff(f,x)

f_prime_val = f_prime.subs(x,1)

print(f_prime)  # derivative of function f
print(f_prime_val) # derivative at x = some value