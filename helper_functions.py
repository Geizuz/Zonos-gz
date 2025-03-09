def txt_to_list(file_path):
    """Reads a text file and returns a list of strings, 
    where each element is a line from the file.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # Remove newline characters from each line
        return [line.strip() for line in lines]
    except FileNotFoundError:
        return f"Error: File not found at {file_path}"
    except Exception as e:
        return f"An error occurred: {e}"
