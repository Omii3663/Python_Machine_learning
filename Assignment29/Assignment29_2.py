import sys
import os

def find_and_read_file(target_filename, directory):
    print(f"Searching for file: '{target_filename}' inside '{directory}' directory...\n")
    
    file_found = False
    
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return
    
    for folder_name, sub_folders, file_names in os.walk(directory):
        for fname in file_names:
            if fname == target_filename:
                file_found = True
               
                full_file_path = os.path.join(folder_name, fname)
                print(f"--- Found file at: {full_file_path} ---")
                
                try:
                    with open(full_file_path, 'r') as fobj:
                        data = fobj.read()
                        print(data)
                except Exception as e:
                    print(f"Could not read file due to an error: {e}")
                
                print("-" * 40)
                
    if not file_found:
        # Dynamic error message fix
        print(f"Error: '{target_filename}' was not found anywhere inside the '{directory}' folder.")

def main():
    # sys.argv[0] is the script name
    # sys.argv[1] will be the file name
    # sys.argv[2] will be the directory folder path
    if len(sys.argv) == 3:
        find_and_read_file(sys.argv[1], sys.argv[2])
    else:
        print("Usage Error: Please provide both the file name and the target directory.")
        print("Example: python script.py Demo.txt C:\\Users\\MyFolder")
        print("Example (Current Directory): python script.py Demo.txt .")

if __name__ == "__main__":
    main()
