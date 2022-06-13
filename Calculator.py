##########################################################

# calculating ration for the day

def ration(weight, height, age, activity):
    w = weight * 10
    h = height * 6.25
    a = age * 5
    dci = (w + h - a - 161) * activity
    return print("Your daily ration is: " + str(int(dci)))

# activity 1.47
ration(58, 166, 24, 1.4)
