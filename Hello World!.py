print("Hello, World!")



def say_hello():
    print("Hello, World!")

say_hello() 


def get_hello_message():
    return 'Hello, World!'



def say_hello():
    message = get_hello_message()
    print(message)

say_hello()



def helloreturn ():
    name = input("What's your name? ")
    if not name:
        print("Hello, Word!")
    else:
        print("Hello, " + name + "!")

helloreturn() 
