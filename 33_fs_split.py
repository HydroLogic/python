import os.path # File system path manipulation library

# __file__ is a special global variable that references a string containing the current module's path.
# http://xkcd.com/917/
print 'The file containing this code is', __file__

my_file_path = __file__
# os.path.split splits a path into 'head' and 'tail' components
my_dir_path, my_file_name = os.path.split(my_file_path)
print 'My directory path', my_dir_path
print 'My file name', my_file_name
# Splitting a path to a file gives you (parent directory path, file name)
# Splitting a path to a directory gives you (parent directory path, directory name)

# Always use os.path.split(path) instead of the string methods path.split or path.rsplit
# It handles platform-specific path logic that the general string functions don't.

# To split a file name up
my_file_base_name, my_file_ext = os.path.splitext(my_file_name)
print 'My file base name', my_file_base_name
print 'My file extension', my_file_ext # Note that this contains the '.'!
# Different platforms have different file extension rules.
# Use os.path.splitext(file_name) of file_name.split or file_name.rsplit.
