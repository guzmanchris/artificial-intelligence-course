"""
This file is used to calculate iterations using the gradient ascent algorithm applied to a function f(x).

Example of use:
Enter the function f(x) for which to apply the gradient ascent algorithm: -0.2 + x + x**2 - 5.5*x**3 + 4*x**4
Enter the first derrivative f'(x) of the function: 16*x**3 - 16.5*x**2 + 2*x + 1
Enter the alpha value to use: 0.1
Enter the initial value x_0: 0.11
Enter the number of iterations to calculate: 3
x0    = 0.11
f(x0) = -0.08463486
x1    = 0.2141646
f(x1) = 0.0144196453
x2    = 0.2970345955
f(x2) = 0.0722622017
x3    = 0.3527943219
f(x3) = 0.0977174032
"""

# Ask for necessary information from user
f = eval("lambda x: " + input("Enter the function f(x) for which to apply the gradient ascent algorithm: "))
f_prime = eval("lambda x: " + input("Enter the first derrivative f'(x) of the function: "))
alpha = float(input("Enter the alpha value to use: "))
x = float(input("Enter the initial value x_0: "))
n = int(input("Enter the number of iterations to calculate: "))

# Run and print n iterations of the algorithm. (The +1 is added to include the initial state/iteration).
for i in range(n + 1):
    print(f'x{i}    =', round(x, 10))
    print(f'f(x{i}) =',round(f(x), 10))
    x = x + alpha*f_prime(x)