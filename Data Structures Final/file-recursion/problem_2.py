import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    path_list = []
    # Get current directory files
    list_dir = os.listdir(path)
    # Check each file in directory 
    for file in list_dir:
        file_path = path + '/' + file
        # Check if file is a file 
        if os.path.isfile(file_path):
            # Check if file ends with suffix
            if file.endswith(suffix):
                path_list.append(file_path)
        # If folder enter new folder and call find_files
        else:
            path_list.extend(find_files(suffix, file_path))
    return path_list

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(find_files('.c', '.'))
# Test Case 2
print(find_files('.gitkeep', '.'))
# Test Case 3
print(find_files('.h', '.'))