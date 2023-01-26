# Call an external command in Python.

# Program-

import os
import subprocess
os.system("echo Hello World!")
subprocess.Popen("echo Hello there", shell=True,
                 stdout=subprocess.PIPE).stdout.read()
subprocess.call("echo Hello Python", shell=True)
print(subprocess.run("echo External Command Running", shell=True))
subprocess.call(["dir"], shell=True)
