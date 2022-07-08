import os
root=r"E:\\My Codes"

for entry in os.scandir(root):
    if entry.is_dir():
        typ='dir'
    elif entry.is_file():
        typ='file'
    elif entry.is_symlink():
        typ='link'
    else:
        typ='unknown'
    print('{name} {typ}'.format(name=entry.name,typ=typ,))
