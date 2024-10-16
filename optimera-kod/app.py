from msvcrt import getwch
import os

def convert():
    print("Press C - celsius to fahrenheit, F - fahrenheit to celsius, k - kelvin to celsius, T - celsius to kelvin ")
    
    match getwch().upper():
        case "C":
            # celsius to fahrenheit
            celsius = float(input("Enter temprature in Celcius: "))
            return f"{celsius}°C is equal to {(celsius * 9/5) + 32}°F"
        case "F":
            # fahrenheit to celsius
            fahrenheit = float(input("Enter temprature in Fahrenheit: "))
            return f"{fahrenheit}°F is equal to {(fahrenheit - 32) * 5/9}°C"
        case "K":
            # kelvin to celsius
            kelvin = float(input("Enter temprature in Kelvin: "))
            return f"{kelvin}K is equal to {kelvin - 273.15}°C"
        case "T":
            # celsius to kelvin 
            celsius = float(input("Enter temprature in Celcius: "))
            return f"{celsius}°C is equal to {celsius + 273.15}K"


while True:
    os.system("cls")
    print(convert())
    input() # press enter to continue
