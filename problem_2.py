import os
def find_files(suffix, path, files=list()):
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
    temp = suffix
    if path:
        temp = suffix+'/'+path
    for r in os.listdir(temp):
        temp_ = temp+'/'+r
        if os.path.isfile(temp_) and temp_.endswith(".c"):
            files.append(temp_)

        elif os.path.isdir(temp_):
            files = find_files(temp, r, files)
    return files

print(find_files('.', 'testdir'))
print(find_files('.', ''))
print(find_files('.', 'testdir/subdir3'))
