#circalc.py -- simplistic LCR calculator for TPRG 2131 Week 2 Asmt 1
#Assignment 1 for Tprg 2131 intro week 1-2
#Carson Vanderheyden,100882481 and TPRG-2131-01
#Wednesday, September 20
#This program is strictly my own work. Any material
#beyond course learning materials that is taken from  
#the Web or other souces is properly cited, giving
#credit to the origonal author(s).
#In the previous challenge, you modified the program to offer the added option to calculate the resonant frequency
#of a series RLC circuit. Today's task is to expand the program a bit more to give the user the Q (quality factor)
#of the series RLC circuit. No additional inputs are required, the bandwidth and Q
#are just additional results to be calculated and printed.
#Depending on the user's choices, ask for the necessary input values, then calculate and print the expected result.
#The program quits gracefully when the user enters "q" or "Q".


# Imports the math module to do calculations
import math

# Defines the function that calculates resonant frequency
def calculate_series_resonance(l, c, r):
    resonant_frequency = 1 / (2 * math.pi * ((l / 1000) * (c / 1000000)) ** 0.5)
    bandwidth = r / (l / 1000)
    q_factor = 1 / (2 * math.pi * resonant_frequency * r * (c / 1000000))  
    # Returns the values calculated
    return resonant_frequency, bandwidth, q_factor

# Defines the function that calculates the RC time constant
def calculate_rc_time_constant(r, c):
    rc_time_constant = r * c / 1000000  # Convert capacitance to Farads  

    # Returns the values calculated
    return rc_time_constant

# Prints the first message to the user
print("Resonant circuit and resistor calculator")

while True:
    # Asks the user what option they want to choose
    print("Choose an option:")
    print("1. Calculate series resonant circuit parameters")
    print("2. Calculate total resistance in series")
    print("3. Calculate total resistance in parallel")
    print("4. Calculate RC time constant")
    print("5. Calculate resonant frequency of a series RLC circuit (with Q factor)")
   
    choice = input("Enter your choice (1/2/3/4/5 or q/Q to quit): ")

    if choice in ['q', 'Q']:
        print("Exiting the program.")
        break
    elif choice == '1':
        # Asks user for resistance in ohms if choice one is chosen
        resistance = float(input("What is the resistance in ohms? "))
        while resistance <= 0.0:
            resistance = float(input("The value must be greater than zero\n"
                                    "What is the resistance in ohms? "))
        # Asks user for capacitance in uF if choice one is chosen
        capacitance = float(input("What is the capacitance in uF? "))
        while capacitance <= 0.0:
            capacitance = float(input("The value must be greater than zero\n"
                                    "What is the capacitance in uF? "))
        # Asks user for inductance in mH if choice one is chosen
        inductance = float(input("What is the inductance in mH? "))
        while inductance <= 0.0:
            inductance = float(input("The value must be greater than zero\n"
                                    "What is the inductance in mH? "))

        # Calculates the Resonant Frequency, Q Factor, and Bandwidth
        resonant_frequency, bandwidth, q_factor = calculate_series_resonance(inductance, capacitance, resistance)

        # Prints the Resonant Frequency, Bandwidth, and Q Factor
        print(f"Resonant Frequency: {resonant_frequency:.2f} Hz")
        print(f"Bandwidth: {bandwidth:.2f} Hz")
        print(f"Q Factor: {q_factor:.2f}\n")
    # Calculates the total resistance in series choice 2 is picked
    elif choice == '2':
        r1 = float(input("Enter the value of the first resistor (in ohms): "))
        r2 = float(input("Enter the value of the second resistor (in ohms): "))
        result = r1 + r2
        print(f"Total resistance in series: {result} ohms")
    # Calculates the total resistance in parallel if choice 3 is picked
    elif choice == '3':
        r1 = float(input("Enter the value of the first resistor (in ohms): "))
        r2 = float(input("Enter the value of the second resistor (in ohms): "))
        result = 1 / (1 / r1 + 1 / r2)
        print(f"Total resistance in parallel: {result} ohms")
    elif choice == '4':
        # Asks user for resistance in ohms and capacitance in uF
        resistance = float(input("Enter the resistance in ohms: "))
        while resistance <= 0.0:
            resistance = float(input("The resistance must be greater than zero.\nEnter the resistance in ohms: "))
        capacitance = float(input("Enter the capacitance in uF: "))
        while capacitance <= 0.0:
            capacitance = float(input("The capacitance must be greater than zero.\nEnter the capacitance in uF: "))

        # Calculates and prints the RC time constant
        rc_time_constant = calculate_rc_time_constant(resistance, capacitance)
        print(f"RC Time Constant: {rc_time_constant} seconds\n")
    elif choice == '5':
        # Asks user for resistance in ohms, capacitance in uF, and inductance in mH
        resistance = float(input("Enter the resistance in ohms: "))
        while resistance <= 0.0:
            resistance = float(input("The resistance must be greater than zero.\nEnter the resistance in ohms: "))
        capacitance = float(input("Enter the capacitance in uF: "))
        while capacitance <= 0.0:
            capacitance = float(input("The capacitance must be greater than zero.\nEnter the capacitance in uF: "))
        inductance = float(input("Enter the inductance in mH: "))
        while inductance <= 0.0:
            inductance = float(input("The inductance must be greater than zero.\nEnter the inductance in mH: "))

        # Calculates the Resonant Frequency and Q for series RLC circuit
        resonant_frequency, bandwidth, q_factor = calculate_series_resonance(inductance, capacitance, resistance)

        # Prints the Resonant Frequency, Bandwidth, and Q Factor
        print(f"Resonant Frequency for series RLC circuit: {resonant_frequency:.2f} Hz")
        print(f"Bandwidth: {bandwidth:.2f} Hz")
        print(f"Q Factor: {q_factor:.2f}\n")
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, q, or Q.")