def generateKey(password, message):
    password = str(password)
    message = str(message)
    while len(password) < len(message):
        for char in password:
            password+=char
            if len(password) >= len(message):
                break

    return password

def encrypt(password, message):
    key = generateKey(password, message)
    passOrd = [ord(i) for i in key]
    messOrd = [ord(i) for i in message]

    finalOrd = [passOrd[i] + messOrd[i] for i in range(len(key)) if i<len(messOrd)]

    word = ''.join([chr(i) for i in finalOrd])
    return word

def decrypt(password, message):
    key = generateKey(password, message)
    passOrd = [ord(i) for i in key]
    messOrd = [ord(i) for i in message]

    finalOrd = [messOrd[i] - passOrd[i] for i in range(len(key))]

    word = ''.join([chr(i) for i in finalOrd])
    return word


# Client program
import socket


print("Please set a password.")
password = input("Answer:")
print()
print("What is your Team Name?")
name = input("Answer:")
print()
print("Group size?")
size = input("Answer:")
print()

encry_key = password

items = [password,size,name]
for i in range(len(items)):
    items[i] = encrypt(encry_key, items[i])

message = "/".join(items)

print("Establishing connection...")
s = socket.socket()
s.connect(('127.0.0.1', 9999))
print("Connection established!")

data = b''

s.sendall(message.encode() + b'\n')
print("Data sent!")

print()
print("Waiting for the server to confirm your request...")
print()
data=s.recv(1024)

decrypted_data = data
decrypted_data = decrypted_data.decode()

decrypted_data = decrypt(password,decrypted_data)      

if decrypted_data=="cancelled":
    print("""Pickup cancelled. 
Wrong password or request rejected.
Please try again.""")

if decrypted_data=="confirmed":
    print("""Pickup confirmed! Please wait for pickup to arrive.""")

s.close()
print()
print("Connection disconnected.")
