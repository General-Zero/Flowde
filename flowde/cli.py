import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='store_true', help='Display Flowde version')
    parser.add_argument('--dependencies', action='store_true', help='Dependencies installed')
    parser.add_argument('--syntax', action='store_true', help='Shows Flowde syntax')
    args = parser.parse_args()

    if args.version:
        version()
    elif args.dependencies:
        dependencies()
    elif args.syntax:
        syntax()
    else:
        print("Flowde has successfully been installed")
def version():
    print("Flowde 0.0.6")
def dependencies():
    print('Dependencies installed for Flowde are: [colorama, requests, flask]')
def syntax():
    print('The following are Flowde syntax:\nflowde.text(\'text\') • A simple print command\nflowde.num(5 + 5) • A basic calculator\nflowde.ttkn(\'your text\') • Stands for \'Text-Token\', gets the\nnumber of words and turns it into an integer (token)\nflowde.capi(\'https://example.com\', indents=4) • `flowde.capi` stands for call-api or extract websites, the `indents=4`\nmeans how many indents the json dictionary will have\nflowde.h() • Provides some help for Flowde syntax.\n\nMore info will be added in 0.0.7')
syntax()