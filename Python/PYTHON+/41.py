# Determine wether a Python shell is executing in 32bit or64bit mode on OS??

# Program-

import platform
print("Python shell is executing in",
      platform.architecture()[0], "mode on OS.")
