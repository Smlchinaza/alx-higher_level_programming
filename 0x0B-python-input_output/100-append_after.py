def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file after each line containing a specific string"""
    with open(filename, 'r') as file, open(filename + '.tmp', 'w') as tmp_file:
        for line in file:
            tmp_file.write(line)
            if search_string in line:
                tmp_file.write(new_string + '\n')
    
    # Replace the original file with the temporary file
    os.rename(filename + '.tmp', filename)
