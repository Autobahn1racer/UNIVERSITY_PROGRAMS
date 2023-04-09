import scipy.misc as spm

# Define the function to differentiate
def f(x):
    return x**2 + 2*x + 1

# Use the derivative function to compute the derivative
dfdx = spm.derivative(f, 3.0, dx=1e-6)

# Print the result
print("The derivative of f(x) at x = 3.0 is:", dfdx)
