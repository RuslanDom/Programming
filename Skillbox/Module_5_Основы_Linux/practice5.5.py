import time
import subprocess, shlex


def cmd_popen_two_command():
    cmd = 'sleep 5 && echo "My mission is done here!"'
    res_cmd = []
    cmd_1, cmd_2 = cmd.split('&&')
    res_cmd.append(shlex.split(cmd_1))
    res_cmd.append(shlex.split(cmd_2))
    start = time.time()
    for i in range(len(res_cmd)):
        r = subprocess.Popen(
            args=res_cmd[i],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        r.wait()
        print(f'Результат выполнения: {r.stdout.read()}\nВремя затрачено: {time.time() - start}')


if __name__ == "__main__":
    cmd_popen_two_command()