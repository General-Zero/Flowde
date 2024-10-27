import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='store_true', help='Display Flowde version')
    parser.add_argument('--devst', action="store_true", help="Displays the development stage of Flowde")
    parser.add_argument('--dependencies', action='store_true', help='Dependencies installed')
    parser.add_argument('--syntax', action='store_true', help='Shows Flowde syntax')
    args = parser.parse_args()

    if args.version:
        version()
    elif args.devst:
        devst()
    elif args.dependencies:
        dependencies()
    elif args.syntax:
        syntax()
    else:
        print("Flowde has successfully been installed")
def version():
    print("Flowde 0.0.4")
def devst():
    print("Alpha version 0.0.4")
def dependencies():
    print('Dependencies installed for Flowde are: [colorama]')
def syntax():
    print('The following are Flowde syntax:\nflowde.text(\'text\') • A simple print command\nflowde.num(5 + 5) • A basic calculator\nflowde.ttkn(\'your text\') • Stands for \'Text-Token\', gets the number of words and turns it into an integer (token)\nflowde.flowdehelp() • Provides some help for python syntax.\n\n', 'More info will be added in 0.0.5')
