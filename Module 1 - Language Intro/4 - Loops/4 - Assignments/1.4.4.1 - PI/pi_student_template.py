import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""
'''**4.4.1 - Estimating PI**

Use the [Gauss–Legendre_algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm) to estimate the value of PI. 
The program should generally follow the steps in the Wikipedia article.

Step 1: Declare/set the initial values for a0, b0, t0, and p0

Step 2: Loop and re-calculate those variables for 10 iterations

Step 3: Once the loop is completed, save the result to variable "pi_estimate" '''


# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a = 1
b = 1/math.sqrt(2)
t = 0.25
p = 1

# perform 10 iterations of this loop
for i in range(1, 10):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """
    a0=a
    a=(a+b)/2
    b=math.sqrt(a0*b)
    t=t-p*(a-a0)**2
    p=2*p

    print(((a+b)**2)/(4*t))
    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
pi_estimate = ((a+b)**2)/(4*t)

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
