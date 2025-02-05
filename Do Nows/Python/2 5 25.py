message = input("Enter message: ")

shift = int(input("Enter amount of pos to shift"))


encrypted_message = ""

for i in message:
    shifted = (ord(i) - ord("A") + shift) % 26

    encrypted_message += chr(shifted + ord("A"))

print(encrypted_message)
