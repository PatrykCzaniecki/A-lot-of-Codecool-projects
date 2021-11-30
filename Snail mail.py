email = input("Your email address: ")
ilosc_malp = int(email.count("@"))
username = email.split("@")[0]
username_length = len(username)
domain = email.split("@")[1]
domain_length = len(domain)
dot_in_email = int(email.count("."))
dot_in_domain = int(domain.count("."))
TLD = domain.split(".")[1]

while True:
    if ilosc_malp == 1:
        print("OK")
    elif ilosc_malp == 0:
        print("An email address has to contain a '@' character!")
    elif ilosc_malp > 1:
        print("An email address cannot contain more than one '@' characters!") 

    if username_length == 0:
        print("The username before the '@' character cannot be empty!")
    else:
        print("OK") 
        
    if domain_length == 0:
        print("The domain after the '@' character cannot be empty!")
    else:
        print("OK")

    if dot_in_email == 0:
        print("An email address has to contain at least one '.' character!")
    else:
        print("OK")

    if dot_in_domain != 0:
        print("OK")
    else:    
        print("The domain has to contain at least one '.' character!")

    if domain.endswith("."):
        print("The top-level domain cannot be empty!")
    else:
        print("OK")

    if len(TLD) <= 1:
        print("The top-level domain has to be at least two characters long!")
    else:
        print("OK") 

    if username.startswith("."):
        print("The username cannot start with a '.' character!")
    else:
        print("OK")

    if domain.startswith("."):
        print("The domain cannot start with a '.' character!")
    else:
        print("OK") 
    
    print("Valid email address :)")
   #break 