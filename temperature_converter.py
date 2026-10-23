######################################################################################
#                   Temperature Converter                                            #
#               -------------------------------                                      #
# - Takes input of a value representing temperature in celsius and converts to       #
#   fareinheit, and displays the result.                                             #
# - Uses strip and split to extract and and conditonals validate the input           #
# - Raises ValueError for invalid input, main() will catch and output errors         #
# - Valid input can be: 25 c or 25 C, 25 Celsius or 25 celsius, or 25. Otherwise the #
#   the program will catch anything that doesn't match that format.                  #
#   Extra spaces around a valid input will also be parsed correctly                  #
#------------------------------------------------------------------------------------#
# - INFO-U762-Interoperability - Module 2 - Assignment 1                             #
# - GitHub: @rshensley (https://github.com/rshensley)                                #
# - Repo: python_fundamentals                                                        #
######################################################################################


def parse_temp(user_input):
    """Extract and validate a temperature in celcius from user"""

    # strip spaces and if user entered C, c, celsius or Celsius split it from the numeric value
    # into list that contains 2 strings (number, temperature unit)
    str_input = user_input.strip().split()

    # check whether input contains either a number, or number and Celsisus/celsius/c/C
    # if input contains additional elements in list from temperature and the unit (celsius,c)
    # ex: 25 celsius farehheit
    # then raise an error there.
    if len(str_input) not in (1, 2):
        raise ValueError("Enter a number, optionally with c, C, or Celsius.")

    # check the second part of the input, and accept c or celsius as possible inclusions
    # regardless of the case used (using casefold)
    if len(str_input) == 2 and str_input[1].casefold() not in ("c", "celsius"):
        raise ValueError("Only Celsius temperatures are valid.")

    # convert the numeric string to a float and return it
    # invalid numeric input automatically raises an error here.
    return float(str_input[0])


def celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    return (celsius * 9 / 5) + 32


def main():
    print("Celsius to Farenheit Converter")

    while True:
        try:
            user_input = input("Enter celsius temperature: ")
            celsius = parse_temp(user_input)
            fahrenheit = celsius_to_fahrenheit(celsius)

            print(f"{celsius:.2f} °C = {fahrenheit:.2f} °F")
            break

        except ValueError as error:
            print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
