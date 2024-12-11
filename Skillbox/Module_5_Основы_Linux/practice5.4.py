import os
import subprocess
import shlex


def main():
    command = subprocess.run(['python', 'test_work.py'], stdout=subprocess.PIPE)
    str_command = command.stdout.decode()
    # str_command = 'curl -i -H "Accept: application/json" -X GET https://api.ipify.org?format=json'
    # print(str_command)
    remove_symbols = ['\'', '[', ']']
    list_command = ''.join(el for el in str_command if el not in remove_symbols).strip('\n').split(', ')
    print(list_command)
    res =  f'sudo -S {" ".join(list_command)}'
    # print(res)
    # r = subprocess.run(['sudo -S', *list_command], capture_output=True, shell=True, text=True, stdin=subprocess.PIPE)
    # r = os.popen(res)

    r = subprocess.Popen([res], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    print(r.stdout.read())



# def main():
#     output = subprocess.run(['git', '--version'], capture_output=True, text=True)
#
#     print(output.stdout)

def w():
    command = subprocess.run(['python', 'test_work.py'], capture_output=True)
    print("stdout ", command.stdout)
    com = command.stdout
    args = shlex.split(com.decode())
    print(args)
    res = subprocess.run([*args], capture_output=True)
    print(res.stdout.decode())

if __name__ == "__main__":
    main()
    # w()
