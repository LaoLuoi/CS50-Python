def main():     # Funtion main
    mass = int(input("Enter a mass in kilograms: "))      # Input mass (in kilograms)
    c = 300000000       # c: speed of light (meters per second)
    e = mass * (c ** 2)     # Energy formula (in Joules)
    print(int(e))       # Print integer e

if __name__ == "__main__":
    main()      # Call function main
