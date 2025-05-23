import os

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
    if file_path:
        # Read sentences from the file
        try:
            with open(file_path, 'r') as file:
                #return [line.strip() for line in file.readlines()] # Does not skip lines
                return [line.strip() for line in file.readlines() if not line.strip().startswith("##")] # Skips lines starting with '##"
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")  # Print error to console
            return default_sentences
        except Exception as e:
            print(f"An error occurred: {e}")  # Print exception error to console
            return default_sentences
    else:
        # Return default sentences if no file path or invalid file path is provided
        print("Default sentences used. No file path provided")
        return default_sentences

def parse_slice(str_values):
    # Split by colon and convert to integers
    parts = str_values.split(':')
    start = int(parts[0]) if parts[0] else None
    stop = int(parts[1]) if len(parts) > 1 and parts[1] else None
    step = int(parts[2]) if len(parts) > 2 and parts[2] else None
    return slice(start, stop, step)
