# main.py

import os
import shutil
import fnmatch

class FileManager:
    def __init__(self, base_directory="."):
        self.base_directory = base_directory

    # Insert File/Folder
    def insert(self, name, is_folder=False):
        path = os.path.join(self.base_directory, name)
        if is_folder:
            os.makedirs(path, exist_ok=True)
            print(f"Folder '{name}' created.")
        else:
            with open(path, 'w') as file:
                file.write("")
            print(f"File '{name}' created.")

    # Delete File/Folder
    def delete(self, name):
        path = os.path.join(self.base_directory, name)
        if os.path.isfile(path):
            os.remove(path)
            print(f"File '{name}' deleted.")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Folder '{name}' deleted.")
        else:
            print(f"'{name}' does not exist.")

    # Move File/Folder
    def move(self, src_name, dest_name):
        src_path = os.path.join(self.base_directory, src_name)
        dest_path = os.path.join(self.base_directory, dest_name)
        if os.path.exists(src_path):
            shutil.move(src_path, dest_path)
            print(f"'{src_name}' moved to '{dest_name}'.")
        else:
            print(f"'{src_name}' does not exist.")

    # Search by Exact Name
    def search_by_exact(self, name):
        results = []
        for root, dirs, files in os.walk(self.base_directory):
            if name in dirs or name in files:
                results.append(os.path.join(root, name))
        if results:
            print(f"Exact match found: {results}")
        else:
            print(f"No exact match for '{name}'.")

    # Search by Pattern
    def search_by_pattern(self, pattern):
        results = []
        for root, dirs, files in os.walk(self.base_directory):
            matches = fnmatch.filter(dirs + files, pattern)
            for match in matches:
                results.append(os.path.join(root, match))
        if results:
            print(f"Pattern matches: {results}")
        else:
            print(f"No matches for pattern '{pattern}'.")

# Example Usage
if __name__ == "__main__":
    file_manager = FileManager()

    # Insert operations
    file_manager.insert("example_file.txt")  # Insert a file
    file_manager.insert("example_folder", is_folder=True)  # Insert a folder

    # Delete operations
    file_manager.delete("example_file.txt")  # Delete a file
    file_manager.delete("example_folder")  # Delete a folder

    # Move operations
    file_manager.move("old_name.txt", "new_name.txt")  # Move/Rename file/folder

    # Search operations
    file_manager.search_by_exact("target_file.txt")  # Search by exact name
    file_manager.search_by_pattern("*.txt")  # Search by pattern
