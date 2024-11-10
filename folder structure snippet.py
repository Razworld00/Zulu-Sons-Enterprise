import os

# Define the root directory for your project
project_root = "Zulu_Sons_Enterprise"

# Define the folder structure
folder_structure = {
    "": ["index.html", "about.html", "services.html", "contact.html"],
    "css": ["styles.css"],
    "css/images": ["construction.jpg", "road_building.jpg", "infrastructure.jpg"],
    "js": ["main.js"],
    "assets/fonts": [],
    "assets/icons": [],
    "images": ["director1.jpg", "director2.jpg"],
    "images/projects": ["project1.jpg", "project2.jpg"],
}

# Create folders and files
for folder, files in folder_structure.items():
    folder_path = os.path.join(project_root, folder)
    os.makedirs(folder_path, exist_ok=True)  # Create folders
    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, "w") as f:
            f.write("")  # Create empty files

print(f"Folder structure for '{project_root}' created successfully.")
