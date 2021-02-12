import os

try:
    import string
except ImportError:
    os.system('pip install string')
    import string
try:
    import secrets
except ImportError:
    os.system('pip install secrets')
try:
    import random
except ImportError:
    import random
try:
    import autopy # Works Only in Python 3.8
except ImportError:
    os.system('pip install autopy')
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
clear = lambda: os.system('cls')

white = fg("white")
green = fg("green")
red = fg("red")

clear()

def letter():

    length = int(input("- [" + green + " $ " + white + "] length : ")) # like 4 = 'aaaa' , 5 = 'aaaaa' ...
    count = int(input("- [" + green + " $ " + white + "] Count : ")) # The Amount of it 100 word ..
    file_name = str(input("- [" + green + " $ " + white + "] Name Of The File You Want To Save in : "))

    with open(file_name + '.txt', 'a') as file:
        for i in range(count):
            word = ''.join(random.choice(string.ascii_letters) for x in range(length))
            if i == range(count)[-1]:
                file.write(word)
                autopy.alert.alert("- Done Making list\n \nCoded By @2vj6 Enjoy ;)", 'Task Done !')
            else:
                file.write(word + "\n")

def nump():

    length = int(input("- [" + red + " $ " + white + "] length : ")) # like 4 = '6666' , 5 = '66666' ...
    count = int(input("- [" + red + " $ " + white + "] Count : ")) # The Amount of it 100 word ..
    file_name = str(input("- [" + red + " $ " + white + "] Name Of The File You Want To Save in : "))

    with open(file_name + '.txt', 'a') as file:
        for i in range(count):
            word = ''.join(random.choice(string.digits) for x in range(length))
            if i == range(count)[-1]:
                file.write(word)
                autopy.alert.alert("- Done Making list\n \nCoded By @2vj6 Enjoy ;)", 'Task Done !')
            else:
                file.write(word + "\n")

def mix():

    length = int(input("- [" + red + " $ " + white + "] length : ")) # like 4 = '6666' , 5 = '66666' ...
    count = int(input("- [" + red + " $ " + white + "] Count : ")) # The Amount of it 100 word ..
    file_name = str(input("- [" + red + " $ " + white + "] Name Of The File You Want To Save in : "))

    with open(file_name + '.txt', 'a') as file:
        for i in range(count):
            word = ''.join(random.choice(secrets.token_urlsafe()) for x in range(length))
            if i == range(count)[-1]:
                file.write(word)
                autopy.alert.alert("- Done Making list\n \nCoded By @2vj6 Enjoy ;)", 'Task Done !')
            else:
                file.write(word + "\n")

print(white + """
   ____    ____        _  __     _                     __  
  / __ \  |___ \__   _(_)/ /_   | |__   ___ _ __ ___   \ \ 
 / / _` |   __) \ \ / / | '_ \  | '_ \ / _ \ '__/ _ \ (_) |
| | (_| |  / __/ \ V /| | (_) | | | | |  __/ | |  __/  _| |
 \ \__,_| |_____| \_/_/ |\___/  |_| |_|\___|_|  \___| (_) |
  \____/            |__/                               /_/ 
""")

print("\n                 - List Maker .")

print("- [" + red + " 1 " + white + "] Just letters , [" + red + " 2 " + white + "] Just Numbers , [" + red + " 3 " + white + "] Mixed up ?")

ask = int(input("- [" + green + " ! " + white + "] Choce Your Mode : "))

if ask == 1:
    letter()
elif ask == 2:
    nump()
elif ask == 3:
    mix()
else:
    autopy.alert.alert("Bad input it's just 1-3 !", 'Bad input !')