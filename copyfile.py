import shutil
import os

def copy_file(source_dir, dest_dir, filename):
    # Construct full paths for source and destination files
    source_file = os.path.join(source_dir, filename)
    dest_file = os.path.join(dest_dir, filename)
    print(source_file)
    print(dest_file)

    # Check if source file exists
    if os.path.exists(source_file):
        # Copy file from source to destination
        shutil.copy(source_file, dest_file)
        print(f"File '{filename}' copied successfully.")
    else:
        print(f"Error: Source file '{filename}' does not exist.")

# Directory containing the Python script (root folder)
root_folder = os.path.dirname(os.path.realpath(__file__))

# Source and destination directories
source_directory = os.path.join(root_folder, "artifacts", "training")
destination_directory = os.path.join(root_folder, "model")

# Source and destination directories
#source_directory = r"\artifacts\training"  # Note the 'r' before the string to treat it as a raw string
#destination_directory = r"\model"         # Note the 'r' before the string to treat it as a raw string

# Filename to be copied
file_to_copy = "model.h5"

# Call the function to copy the file
copy_file(source_directory, destination_directory, file_to_copy)