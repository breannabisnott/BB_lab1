#Write a function, parallel(), that, when called, outputs the effective resistance of 
#a network of 2 or more resistors connected in parallel. The function should be able to 
#accept a list of numbers of any length.

def parallel(resistances):
    if (len(resistances) > 2):
        r_sum = 0
        for resistance in resistances:
            r_sum = r_sum + (1/resistance)
    else:
        print("Please enter at least 2 values")
    return(1/r_sum)

print(parallel([2, 5, 3, 5]))