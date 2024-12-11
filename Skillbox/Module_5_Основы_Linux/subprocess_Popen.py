import subprocess
import os
import time


# def simple_popen():
#     print('Start code')
#     result = os.popen(cmd='python3 test_program_popen.py')
#     result = subprocess.Popen(['python3', 'Flask/Skillbox/Module_5_Основы_Linux/test_program_popen.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
#     performance = subprocess.Popen(['echo', 'Браво!'])
#     print(performance.returncode)
#     return result

# if __name__ == "__main__":
#     res = simple_popen()


def light_popen():
    with subprocess.Popen('uptime', stdout=subprocess.PIPE) as process:
        print(process.stdout.read())
    print('return code:', process.returncode)


def hard_popen():
    print('Start')
    start = time.time()
    procs = []
    for pnum in range(1, 6):
        p = subprocess.Popen(
            ['python', 'test_program_popen.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f'Process number {pnum} started. PID: {p.pid}')
        procs.append(p)

    for proc in procs:
        proc.wait()
        # print(proc.stdout.read())
        if b'Done' in proc.stdout.read() and proc.returncode == 0:
            print(f'Process with PID: {proc.pid} ended successfully')

    print(f'Done in {time.time() - start}')
    return 'End'

if __name__ == "__main__":
    print('---***---' * 10)
    light_popen()
    print('---***---' * 10)
    r = hard_popen()

# ____________________________ТРЕНИРОВКА____________________________
# def main():
#     start = time.time()
#     processes = []
#     for i in range(1, 6):
#         r = subprocess.Popen(
#             ['python', 'test_program_popen.py'],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE
#         )
#         print(f"Процесс номер {i} запущен, PID: {r.pid}")
#         processes.append(r)
#
#     for i_proc in range(len(processes)):
#         processes[i_proc].wait()
#         if b"Done" in processes[i_proc].stdout.read() and processes[i_proc].returncode == 0:
#             print(f"Процесс номер {i_proc + 1} (PID: {processes[i_proc].pid}) успешно выполнен")
#         else:
#             print('ОШИБКА')
#     print(f'Время выполнения: {round(time.time() - start, 5)} c')
#
# if __name__ == "__main__":
#     main()