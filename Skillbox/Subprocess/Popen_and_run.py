import subprocess


cmd = ''

# 1. Выполнение git --version
output = subprocess.run(['git', '--version'], capture_output=True, text=True)
print(output.stdout)








