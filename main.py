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


def decoder_function(encoded_str):
    #Written by James Cross
    plain_text = ""
    for i in encoded_str: #loop through all characters
        i = int(i) #cast to int
        i -= 3 #subtract 3
        if i < 0: #check if negative
            i += 10 #"rollback" to positive
        i = str(i) #cast back to string
        plain_text += i #append to decoded string
    return plain_text


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
            print("The encoded password is ", encode, ", and the original password is ", decoder_function(encode), ".", sep="")
        elif option == 3:
            break
