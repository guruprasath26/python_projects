from cryptography.fernet import Fernet
#Modern cryptography is the one used widely among computer science projects to secure the data messages.
'''

def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)
write_key()        

'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet(key)

def view():
    with open("passwords.txt",'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print("User:", user, "| password:", fer.decrypt(pwd.encode()).decode())

def add():
    name = input("account name: ")
    pwd = input("password: ")
    with open("passwords.txt","a") as f:
        f.write(name+"|"+ fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode=input("would you like to add a new password or view existing ones (view , add),q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode =='add':
        add()

    else:
        print("invalid mode.")
        continue

