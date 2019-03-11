import random
def get_secret_word():
    file = open('words.txt' ,'r')
    data = file.read()
    data = data.split()
    return random.choice(data)