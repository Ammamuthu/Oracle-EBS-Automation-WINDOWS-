import subprocess

command = 'echo Hello, World!'
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

print("Output:", result.stdout)
# ========================================================================
