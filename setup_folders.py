# run this to setup the folders before ever running anything else
import os

# Folder and file structure to be created
structure = {
    'mobile_app': ['main.py'],
    'server': ['app.py'],
    'database': ['init_db.py'],
    'docs': ['README.md']
}

# Function to create folders and files
def create_project_structure(structure):
    for folder, files in structure.items():
        # Create folder if it doesn't exist
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Create files in the folder
        for file in files:
            file_path = os.path.join(folder, file)
            with open(file_path, 'w') as f:
                f.write('')  # Create an empty file

# Create the project structure
create_project_structure(structure)
print("Project structure created successfully.")
