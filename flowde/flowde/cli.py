import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='store_true', help='Display Flowde version')
    parser.add_argument('--phase', action="store_true", help="Displays Dev stage Of Flowde")

    args = parser.parse_args()

    if args.version:
        version()
    elif args.phase:
        phase()
    else:
        print("Flowde has successfully been installed")
def version():
    print("Flowde 0.0.1")
def phase():
    print("Alpha")