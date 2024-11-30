def modify_file_content(input_file, output_file):
    try:

        with open(input_file, 'r') as file:
            content = file.readlines()
        
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]
        
        with open(output_file, 'w') as file:
            file.writelines(modified_content)
        
        print(f"Content successfully modified and saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


modify_file_content('example.txt', 'modified_example.txt')

def read_user_file():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_user_file()
