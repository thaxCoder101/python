from sys import argv

script,username = argv
prompt = '>'

print(f"hi, {username}, im the {script} script")
print(f"do u like me {username}")
likes = input(prompt)

print(f"where do u live {username}")
lives = input(prompt)

print(f"u said {likes} ablut liking me. u live in {lives}")