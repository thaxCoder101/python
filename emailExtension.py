def main():
    print("welcome to the email slicer ")
    print("")

    emailInput = input("Input your email address: \n")

    (username, domain) =  emailInput.split("@")
    (domain, extension) = domain.split(".")

    print("Username : ", username)
    print("Domain : ", domain)
    print("Extension : ", extension)

main()