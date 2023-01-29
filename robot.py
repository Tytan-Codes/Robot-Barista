import os
import time
os.system('cls')
# making the def
def done():
    os.system('cls')
    print('Thank you for ording',askName + ', your coffee with be ready within 4 minutes.')

#Asking name
askName = str(input('Whats your name: '))
os.system('cls')
#Listing all the coffies
coffies = ['Americano', 'Cortado', 'Mocha', 'Macchiato']

#getting rid of '[]' around the names
coffee = str(coffies)[1:-1]

#Listing the coffies

print('Hi', askName + ' the coffies we have avalable today: ',coffee)

#asking what coffee they want

askCoffee = str(input('What would you like? '))
os.system('cls')
if askCoffee == 'Americano':
    done()
    input()
if askCoffee == 'Cortado':
    done()
    input()
if askCoffee == 'Mocha':
    done()
    input()
if askCoffee == 'Macchiato':
    done()
    input()
    
else:
    print('Thats not a coffee :(')
    time.sleep(5)
    os.system('py robot.py')
 
 
 
