import zipfile
with zipfile.ZipFile("E:\My Codes\Z.zip", 'r') as zip_ref:
    zip_ref.extractall("E:\My Codes\giles_zip")