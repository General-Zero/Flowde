from colorama import Fore, Style, init
def text(textinput):
    print(textinput)
def num(numinput):
    print(int(numinput))
def ttkn(text):
    ttkn = text
    amount = text.split()
    ttkn = len(amount)
    print(ttkn)
def help(syntax=None):
    help_syntax = {
        'print()': 'The print() snippet outputs text or the value of a variable.',
        'def func():': 'The "def" snippet defines a function which is similar to "function fname() {}" in JavaScript if you are a JavaScript developer',
    }
    
    if syntax in help_syntax:
    	print(Fore.CYAN + help_syntax[syntax])
    elif syntax is None:
    	print(Fore.GREEN + f'Visit https://github.com/General-Zero/flowde-documentation for more info about Flowde or Functions.')
    	print()
    	print(Fore.GREEN + f'Visit the official python beginner\'s guide for more info: https://www.python.org/about/gettingstarted/')
    else:
    	print(Fore.RED + f'The syntax "{syntax}" is undefined or does not exist in Python.')
    	print()
    	print(Fore.YELLOW + f'Perhaps the syntax is missing something?')
    print(Style.RESET_ALL)
