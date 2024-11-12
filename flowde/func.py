from colorama import Fore, Back, init
import requests
from flask import Flask, jsonify, request
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
def h(option=None):
    options = {
        'py3mtp': 'Let\'s get to the basic syntax of python:\nprint() prints text or the value of a variable.\n\ndef your_func_name(parameters as needed):\n# your_codecode\nchange \'your_func_name\' and \'parameters as needed\'\nwith you\'re function and parameters name. Parameters will be\nexplained shortly.\nParameters - Parameters is you\'re value or input from a\nfunction, for example:\ndef add(a, b):\nprint(a + b) - You can also use \`return\` instead of \`print\` to return that\noutput instead of printing it.'
    }
    if option in options:
    	print(Fore.CYAN + options[option])
    elif option is None:
      print(Fore.GREEN + 'No options provided, try:\npy3mtp')
    else:
      print(Fore.RED + f'{option} option does not exist, perhaps you misspelled it?')
def capi(url, indents=None):
    r = requests.get(url)
    x = r.status_code
    try:
        jsonda = r.json()
        data = json.dumps(jsonda, indent=indents)
        print(data)
    except ValueError:
        print('Encoding: ', r.encoding)
        print(r.text)
    except requests.RequestException as Rex:
        print(f'An error occured during requesting {url}: ', Rex)
    except requests.HTTPError as herror:
        print('HTTP error: ', herror)
    except requests.ConnectionError as wifi:
        print('Please check your internet connection\nError: ', wifi)
def tempapi(port=None, template=None):
    port = port or 5000
    flaskcode = """
from flask import Flask, jsonify, request
import json
app = Flask(__name__)
storage = [{{\'name\': \'Dog\', \'description\': \'My friendly dog\'}}]
@app.route(\'/api\', methods=[\'GET\']) # change the /api to your endpoint. for example: http://localhost:5000/your-endpoint
def get_storage(): # You can change the fname
    return jsonify(storage)
if __name__ == \'__main__\':
    app.run(port={}) # port can be set to your liking, don't use an already used port
    """.format(port)
    templates = {
    'time12': """
from flask import Flask, jsonify, request
import json
import datetime
app = Flask(__name__)
def timecall():
    unftime = datetime.now()
    ftime = unftime.strftime(\'%I:%M %P\')
    return ftime
@app.route(\'/time\', methods=[\'GET\'])
def get_clock():
    jsonclock = {{\'time\': timecall()}}
    return jsonify(jsonclock)
if __name__ == \'__main__\':
    app.run(port={})
    """.format(port)
    }
    if template in templates:
    	print(templates[template])
    else:
    	print(flaskcode)