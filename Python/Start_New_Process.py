import os
import sys
program="Python"
arguments=["E:\My Codes\Python\Cat_Voice.py"]
print(os.execvp(program,(program,)+tuple(arguments)))
print("goodbye!")