def convert_temp(temp,scale):
    
    if scale == "C":
       result = int(round(9*temp) / 5 + 32)
       o_scale = "Fahrenheight"
    elif scale == "F":
       result = int(round((temp - 32) * 5/9))
       o_scale == "Celsuis"
    else:
       print("Input proper conversion")
       sys.exit()
    return result,o_scale

def print_temp(result,o_scale):
    print("The temperature in",o_scale,"is", result,"degree")

def get_temp():
    print("get temp")

def main():
    print("Hello")

main()
