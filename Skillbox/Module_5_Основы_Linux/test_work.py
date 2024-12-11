import shlex
from sys import stdout


def main():
    command = 'curl -i -H "Accept: application/json" -X GET https://api.ipify.org?format=json'
    print(command)



if __name__ == "__main__":
    main()
