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

def get_sentences(file_path=None, default_sentences=None):
    """Reads sentences from a file if file_path is provided; otherwise, returns default sentences."""
    if file_path and os.path.isfile(file_path):
        # Read sentences from the file
        try:
            with open(file_path, 'r') as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return f"Error: File not found at {file_path}"
        except Exception as e:
            return f"An error occurred: {e}"
    else:
        # Return default sentences if no file path or invalid file path is provided
        return default_sentences
