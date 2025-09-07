import shutil
# shutil module provides a way to handle high-level file operations
# such as copying and removing files and directories.
# Copy a file
# with open("Web_Automation/file.txt", "w") as f:  # Create a sample file with some content
# 	f.write("Sample content")

# shutil.copy("Web_Automation/file.txt", "Web_Automation/copy_file.txt")  # Copy file.txt to copy_file.txt
# shutil.copy2("Web_Automation/file.txt", "Web_Automation/copy2_file.txt")  # Copy file.txt to copy2_file.txt with metadata
# print("file copied successfully.")
import os
os.makedirs("Web_Automation/project_folder", exist_ok=True)
print("file copied successfully")
shutil.make_archive("project","zip","Web_Automation/project_folder") # Create a zip archive of the 'project_folder' directory
shutil.unpack_archive("project.zip","extracted_folder","zip") # Extract the contents of 'project.zip' into 'extracted_folder'


