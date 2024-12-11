from sys import stderr

def main():
    print('Print to stdout')
    print("Print to stderr", file=stderr)
    user_input = input()
    print(f"user_input: {user_input}")

if __name__ == "__main__":
    main()