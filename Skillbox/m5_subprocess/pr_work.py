

def main():
    cmd = "curl -i -H 'Accept: application/json' -X GET https://api.ipify.org?format=json"
    print(cmd)


if __name__ == "__main__":
    main()