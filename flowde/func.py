from colorama import Fore, Back, init
import requests
from flask import Flask
import datetime
import json
init(autoreset=True)
def text(textinput):
    print(textinput)
def num(numinput):
    print(int(numinput))
def ttkn(text):
    ttkn = text
    amount = text.split()
    ttkn = len(amount)
    print(ttkn)
def help(option=None):
    options = {
        'py3mtp': 'Let\'s get to the basic syntax of python:\nprint() prints text or the value of a variable.\n\ndef your_func_name(parameters as needed):\n# your_codecode\nchange \'your_func_name\' and \'parameters as needed\'\nwith you\'re function and parameters name. Parameters will be\nexplained shortly.\nParameters - Parameters is you\'re value or input from a\nfunction, for example:\ndef add(a, b):\nprint(a + b) - You can also use \`return\` instead of \`print\` to return that\noutput instead of printing it.'
    }
    if option in options:
    	print(Fore.CYAN + options[option])
    elif option is None:
      print(Fore.GREEN + 'No options provided, try:\npy3mtp')
    else:
      print(Fore.RED + f'{option} option does not exist, perhaps you misspelled it?')
def capi(url):
    r = requests.get(url):
    x = r.status_code
    try:
        json = r.json()
        data = json.dumps(json)
        print(data)
    except ValueError:
        print('Encoding: ' r.encoding)
        print(r.text)
    except requests.RequestException as Rex:
        print(f'An error occured during requesting {url}: ', Rex)
    except requests.HTTPError as herror:
        print('HTTP error: ', herror)
