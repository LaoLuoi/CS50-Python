def main():     # Funciton main
    dollars = dollars_to_float(input("How much was the meal? "))        # Call funtion dollars_to_float
    percent = percent_to_float(input("What percentage would you like to tip? "))        # Call funtion percent_to_float
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d_without_dollar_sign = d.replace("$", "")      # Remove the leading $
    return float(d_without_dollar_sign)     # Return the amount as a float

def percent_to_float(p):
    # TODO
    p_without_percent = p.replace("%", "")      # Remove the trailing %
    p_converted = float(p_without_percent) / 100        # Return the percentage as a float
    return p_converted

if __name__ == "__main__":
    main()  # call function main

