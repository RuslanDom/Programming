import  subprocess




def run_program():
    print('---***---' * 10)
    # Если input() вызывается в 'test_program_run.py' 1 раз то stdin прочитает код до '\n' input=b'Hello world\n'
    res = subprocess.run(['python', 'test_program_run.py'], input=b'Hello world\ncontinue_text')
    print(res)
    print('---***---' * 10)
    res = subprocess.run(['python', 'test_program_run.py'], capture_output=True, input=b'Code 2\n')
    print(res)
    # Result of the code:
    # CompletedProcess(args=['python', 'test_program_run.py'], returncode=0, stdout=b'Print to stdout\n', stderr=b'Print to stderr\n')
    print('---***---' * 10)
    res = subprocess.run(['python', 'test_program_run.py'], stderr=subprocess.STDOUT, input=b'Code 3\n')
    print(res)

if __name__ == "__main__":
    run_program()