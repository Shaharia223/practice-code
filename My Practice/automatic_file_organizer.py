import os
import shutil

SOURCE_DIR = "D:\\Download"
DESTINATION_BASE_DIR = SOURCE_DIR

CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv", ".odt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".heic"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Software": [".exe", ".dmg", ".zip", ".rar", ".7z", ".iso", ".deb", ".rpm"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".h", ".sh"],
    "Others": [],
}

def get_file_category(file_extension):
    for category, extensions in CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

def organize_files(source_directory, destination_base_directory):
    print(f"Starting file organization in: {source_directory}")
    print(f"Organized files will be moved to subfolders in: {destination_base_directory}\n")

    if not os.path.isdir(source_directory):
        print(f"Error: Source directory not found: {source_directory}")
        return

    others_dir = os.path.join(destination_base_directory, "Others")
    os.makedirs(others_dir, exist_ok=True)

    for item_name in os.listdir(source_directory):
        source_path = os.path.join(source_directory, item_name)

        if os.path.isdir(source_path):
            print(f"Skipping directory: {item_name}")
            continue

        file_name, file_extension = os.path.splitext(item_name)

        category = get_file_category(file_extension)
        destination_dir = os.path.join(destination_base_directory, category)

        os.makedirs(destination_dir, exist_ok=True)

        destination_path = os.path.join(destination_dir, item_name)

        counter = 1
        original_destination_path = destination_path
        while os.path.exists(destination_path):
            new_file_name = f"{file_name}_{counter}{file_extension}"
            destination_path = os.path.join(destination_dir, new_file_name)
            counter += 1

        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: '{item_name}' -> '{category}/'")
        except FileNotFoundError:
            print(f"Error: Could not find file {item_name} at {source_path}")
        except PermissionError:
            print(f"Error: Permission denied when moving {item_name}. Is the file in use?")
        except Exception as e:
            print(f"An unexpected error occurred while moving {item_name}: {e}")

    print("\nFile organization complete!")

if __name__ == "__main__":
    organize_files(SOURCE_DIR, DESTINATION_BASE_DIR)