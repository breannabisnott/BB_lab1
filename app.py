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

#print(parallel([2, 5, 3, 5]))


#Write a function, `potential_divider()`, that takes two values as argument, a number that 
#represents a voltage supply value and a list of numbers that represent resistance values of 
#resistors connected in series. The function should output the voltage drop across each resistor 
#in your resistor list. The function should be able to accept a list of numbers of any length.

def potential_divider(v_supply, s_resistances):
    res_sum = 0
    for r in s_resistances:
        res_sum = res_sum + r

    current = v_supply/res_sum

    v_res = []
    for r in s_resistances:
        v_res.append(current*r)

    print(v_res)

#potential_divider(9, [3000, 1000])

#Write a function, `temperature_check()`, that accepts a single number, a patient's body temperature, 
#and a single character, the unit of temperature. The function should output whether the patient is 
#hypothermic, hyperthermic or has normal body temperature based on the number passed to the function. 
    
#The second value passed as argument should tell the function whether the condition should calculated in 
#degrees celcius or degrees fahrenheit.
    
#An appropriate message should be written to the screen with the result. You’re free to use what ever 
#reasonable temperature limits you feel will adequately act as boundaries for these conditions.

def temperature_check(temp, temp_type):
    temp_type = temp_type.lower()
    if temp_type == 'f':
        temp = (5/9)*(temp - 32)
    
    if temp > 40:
        print("You are hyperthermic!")
    elif temp < 36:
        print("You are hypothermic!")
    else:
        print("You are normal :/")

#temperature_check(37, "c")