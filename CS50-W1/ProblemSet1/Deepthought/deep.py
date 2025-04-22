def main():
    # prompt the user for the answer
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    # Call function
    check(answer)

def check(a):
    # Case- and space-insensitively.
    a = a.lower().strip()
    # Conditions of deep thuoght
    if a == "42" or a == "forty-two" or a == "forty two":
        print("Yes")
    else:
        print("No")

main()
