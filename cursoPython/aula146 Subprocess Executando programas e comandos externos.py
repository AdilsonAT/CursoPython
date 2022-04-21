
import subprocess

proc = subprocess.run(['ping', '127.0.0.1'], capture_output=True, text=True)

print(proc)
print(proc.stdout)
print(proc.returncode)
print(proc.args)

