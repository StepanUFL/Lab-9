def encode_password(password):
    encoded = ''
    for i in password:

        if int(i) < 7:
            j = int(i) + 3
            encoded += str(j)
        else:
            j = int(i) - 7
            encoded += str(j)
    return encoded


if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        decode = ""
        option = int(input("Please enter an option: "))
        if option == 1:
            decode = input("Please enter your password to encode: ")
            encode = encode_password(decode)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print("The encoded password is ", decode, ", and the original password is ", encode, ".", sep="")
        elif option == 3:
            break
