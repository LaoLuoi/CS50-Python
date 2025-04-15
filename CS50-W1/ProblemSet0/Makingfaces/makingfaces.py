def convert(user_input):    # function convert
    modified_input = user_input.replace(":)", "🙂").replace(":(", "🙁") # convert emoticons to emoji
    return modified_input

def main():   # function main
    user_input = input("Please enter a smiley or frowney face: ")    # prompts the user for input
    convert(user_input)    # call function convert
    print(user_input)    # print result

if __name__ == "__main__":
    main()  # call function main
