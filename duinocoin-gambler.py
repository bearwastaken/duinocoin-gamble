import ducoapi
import random
guess = 0
api_connection = ducoapi.api_actions() #creates the api connection instance
username = ""
password = ""
print("""      +----------------------------+
      |                            |
      |   welcome to DUCO gambler  |
      |                            |
      +----------------------------+""")
username = input("what is your duino-coin username?")
password = input("what is your duino-coin password?")
api_connection.login(username=username, password=password)
if input("there will be a fee of 1 DUCO, enter [y] to continue").lower() == "y":
    api_connection.transfer(recipient_username="jerrbearisawsome", amount=(1))
    pass
else:
    exit()
guess = input("choose your gamble amount (1 DUCO to 5 DUCO)")
guess = int(guess)
if guess > 0 and guess < 6:
    pass
else:
    exit()
if random.randint(1,2) == 1:
    print("you lose!")
    api_connection.transfer(recipient_username='DUCOpool', amount=(guess))
else:
    print("you win!")
    api_connection.login(username="DUCOpool", password="DOG12345")
    api_connection.transfer(recipient_username=username, amount=(guess))
