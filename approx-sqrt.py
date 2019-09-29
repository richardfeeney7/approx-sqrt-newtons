# Adopted from golang.org

def sqrt(x):
    # Initial guess.
    z=1.0
    # Keep getting a better square root of x until you are within two decimal places
    while abs(z*z - x) >= 0.01 : # Abs will change negative values to corressponding positive (ie -1 will turn to 1) 
        z-= (z*z -x) / (2*z) 
    return z

#Calculate and print square root of 8
z=(sqrt(8.0))
print(z)

# Print square of the square to check calculation
print(z*z)
