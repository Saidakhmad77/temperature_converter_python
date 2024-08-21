import time

now = time.strftime("\t\t%b %d, %Y %H:%M:%S\n\n")
print("\t\tCurrent time is: \n\n", now)

def tepm_converter(temp, to_scale):
    
    if to_scale == "F":
        return(temp * 9/5) + 32
    
    elif to_scale == "C":
        return(temp - 32) * 5/9
    
    else:
        return None
    
    
while True:
    ask_user = input("Do you want to convert to Fahrenheit (F) or Celsius (C)? ").strip().upper()
    if ask_user in ["F", "C"]:
        break
    else:
        print("Invalid input. Please enter 'F' to convert to Fahrenheit or 'C' to convert to Celsius.")

user_input = float(input(f"Enter temperature in {'Celsius' if ask_user == "F" else 'Farhenheit'}: "))


converted_temp = tepm_converter(user_input, ask_user)


if ask_user == 'F':
    print(f"Temperature in Fahrenheit: {converted_temp:.2f}")
elif ask_user == 'C':
    print(f"Temperature in Celsius: {converted_temp:.2f}")
else:
    print("Invalid input type!!!")