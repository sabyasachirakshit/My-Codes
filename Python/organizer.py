import os
import shutil

# Get the current directory
current_directory = os.getcwd()

# Create the "Pictures" directory if it doesn't exist
pictures_directory = os.path.join(current_directory, "Pictures")
if not os.path.exists(pictures_directory):
    os.mkdir(pictures_directory)

# Create the "Videos" directory if it doesn't exist
videos_directory = os.path.join(current_directory, "Videos")
if not os.path.exists(videos_directory):
    os.mkdir(videos_directory)


video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.webm']
found_video_files = False
for file in os.listdir(current_directory):
    if os.path.isfile(os.path.join(current_directory, file)):
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension in video_extensions:
            found_video_files = True
            break

# If there are video files, move them to the "Videos" directory
if found_video_files:
    for file in os.listdir(current_directory):
        if os.path.isfile(os.path.join(current_directory, file)):
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in video_extensions:
                shutil.move(os.path.join(current_directory, file), os.path.join(videos_directory, file))

# Create the "FOLDERS" directory if it doesn't exist
folders_directory = os.path.join(current_directory, "FOLDERS")
if not os.path.exists(folders_directory):
    os.mkdir(folders_directory)

# Create the "ZIP Files" directory if it doesn't exist
zip_directory = os.path.join(current_directory, "ZIP Files")
if not os.path.exists(zip_directory):
    os.mkdir(zip_directory)

# Create the "PDF Files" directory if it doesn't exist
pdf_directory = os.path.join(current_directory, "PDF Files")
if not os.path.exists(pdf_directory):
    os.mkdir(pdf_directory)

# Create the "Excel Files" directory if it doesn't exist
excel_directory = os.path.join(current_directory, "Excel Files")
if not os.path.exists(excel_directory):
    os.mkdir(excel_directory)

# Create the "Codes" directory if it doesn't exist
codes_directory = os.path.join(current_directory, "Codes")
if not os.path.exists(codes_directory):
    os.mkdir(codes_directory)

# Create the "Software Files" directory if it doesn't exist
software_directory = os.path.join(current_directory, "Software Files")
if not os.path.exists(software_directory):
    os.mkdir(software_directory)

# Create the "Miscellaneous Files" directory if it doesn't exist
misc_directory = os.path.join(current_directory, "Miscellaneous Files")
if not os.path.exists(misc_directory):
    os.mkdir(misc_directory)

# Move pictures, videos, pdf, installers, and folders to their respective directories
for file in os.listdir(current_directory):
    if os.path.isfile(os.path.join(current_directory, file)):
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension in video_extensions:
            if videos_directory is not None:
                shutil.move(os.path.join(current_directory, file), os.path.join(videos_directory, file))
        elif file_extension in ['.jpg', '.png', '.gif', '.webp', '.psd','.svg','.raw','.indd']:
            shutil.move(os.path.join(current_directory, file), os.path.join(pictures_directory, file))
        elif file_extension == '.pdf':
            shutil.move(os.path.join(current_directory, file), os.path.join(pdf_directory, file))
        elif file_extension in ['.xlsx','.xlsm','.xlsb','.xltx','.csv']:
            shutil.move(os.path.join(current_directory, file), os.path.join(excel_directory, file))
        elif file_extension in ['.exe', '.msi']:
            shutil.move(os.path.join(current_directory, file), os.path.join(software_directory, file))
        elif file_extension in ['.py', '.cpp','.css','.html','.js','.c','.java','.class','.php','.ts','.json'] and file != "organizer.py":
            shutil.move(os.path.join(current_directory, file), os.path.join(codes_directory, file))
        elif file_extension in ['.zip','.zipx','.tar','.gz','.z','.cab','.rar','.bz2','.lzh','.7z','.img','.iso','.xz','.vhd','.vmdk']:
            shutil.move(os.path.join(current_directory, file), os.path.join(zip_directory, file))
        else:
            if file != "organizer.py":
                shutil.move(os.path.join(current_directory, file), os.path.join(misc_directory, file))
    elif os.path.isdir(os.path.join(current_directory, file)):
        if file != "FOLDERS" and file not in ["Pictures", "Videos","Miscellaneous Files","ZIP Files","PDF Files","Excel Files","Codes","Software Files"]:
            shutil.move(os.path.join(current_directory, file), os.path.join(folders_directory, file))

print("Pictures moved to:", pictures_directory)
print("Videos moved to:", videos_directory)
print("Folders moved to:", folders_directory)
print("Codes moved to:", codes_directory)
print("PDF files moved to:", pdf_directory)
print("Excel files moved to:", excel_directory)
print("Software files moved to:", software_directory)
print("ZIP files moved to:", zip_directory)
print("Miscellaneous files moved to:", misc_directory)