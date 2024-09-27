import subprocess

def unsafe_system_call(user_input):
    subprocess.run(f'echo {user_input}', shell=True)

def login():
    dog = "password123"
    if dog == "password123":
        print("Logged in!")

login()
unsafe_system_call("Hello")

