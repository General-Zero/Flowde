import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='store_true', help='Display Flowde version')
    parser.add_argument('--devst', action="store_true", help="Displays the development stage of Flowde")
    parser.add_argument('--dependencies', action='store_true', help='Dependencies installed')

    args = parser.parse_args()

    if args.version:
        version()
    elif args.devst:
        devst()
    elif args.dependencies:
        dependencies()
    else:
        print("Flowde has successfully been installed")
def version():
    print("Flowde 0.0.4")
def devst():
    print("Alpha version 0.0.4")
def dependencies():
    print('Dependencies installed for Flowde are: [colorama]')
