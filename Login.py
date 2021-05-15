import pickle
import os
os.system("close")
print("Enter your name")
name = input()
print("Enter your password")
password = input()
password_system = name + password
print(password_system)
pickle.dump(password_system, open("Login.txt", "wb"))
password_system = pickle.load(open("Login.txt", "rb"))