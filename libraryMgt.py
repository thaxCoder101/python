from sys import argv

script,filename = argv

txt = open(filename)
print(f"here is ur file {filename}")
print(txt.read())

print("type the filename again")
fileAgain = input(">")

txtAgain = open(fileAgain)

print(txtAgain.read())