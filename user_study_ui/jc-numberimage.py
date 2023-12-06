import os
import shutil

# Paths to the input and output directories
input_folder_path = '/home/jc/exposure/user_study_ui/test'
output_folder_path = '/home/jc/exposure/user_study_ui/data/inputs/outputs'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Fetch all files in the input directory
files = os.listdir(input_folder_path)

# Counter for file names
counter = 1

for file in files:
    # Get the file extension
    file_extension = file.split('.')[-1]

    # Construct new file name without "last image"
    new_file_name = f"{str(counter).zfill(3)}.{file_extension}"

    # Construct full file paths
    old_file = os.path.join(input_folder_path, file)
    new_file = os.path.join(output_folder_path, new_file_name)

    # Copy and rename the file to the output folder
    shutil.copy2(old_file, new_file)

    # Increment the counter
    counter += 1
