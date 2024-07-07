import subprocess
command = 'ping 10.42.1.155'
result = subprocess.run(command,shell=True,stdout=subprocess.PIPE,text=True)
print("output:",result.stdout)