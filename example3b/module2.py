

print('running module2.py')

import module1

def hello():
    print('module2 says hello!\nand...')
    module1.hello()
