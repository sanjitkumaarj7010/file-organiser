import os
import shutil

# Folder to organize
folder = input("Enter folder path: ")

# File type folders
types = {
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".pdf": "PDFs",
    ".docx": "Documents",
    ".txt": "TextFiles",
    ".mp3": "Music",
    ".mp4": "Videos"
}

# Check if folder exists
if not os.path.exists(folder):
    print("Folder not found!")
    exit()

# Organize files
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)

    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()

        if ext in types:
            new_folder = os.path.join(folder, types[ext])

            if not os.path.exists(new_folder):
                os.mkdir(new_folder)

            shutil.move(file_path, os.path.join(new_folder, file))
            print(file, "moved to", types[ext])

print("Files organized successfully!")
