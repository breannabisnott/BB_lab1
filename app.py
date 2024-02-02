#Question 1

def parallel(resistances):
    if (len(resistances) > 2):
        r_sum = 0
        for resistance in resistances:
            r_sum = r_sum + (1/resistance)

        print("{:.3f}".format(1/r_sum), "ohms")
    else:
        print("Please enter at least 2 values")


#Question 2

def potential_divider(v_supply, s_resistances):
    res_sum = 0
    for r in s_resistances:
        res_sum = res_sum + r

    current = v_supply/res_sum

    v_res = []
    for r in s_resistances:
        v_res.append(current*r)

    for x in v_res:
        print("{:.2f}".format(x), "v")

#Question 3

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