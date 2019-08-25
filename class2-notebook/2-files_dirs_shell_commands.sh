# Basic files and directories shell commands

# Create the DIRECTORY(ies), if they do not already exist
mkdir my_new_directory

# Update  the  access  and modification times of each FILE to the current time
touch any_file

# vi / nano ( visually: text edit or vscode ) : Created and edit files
nano any_file
vi any_file

# Concatenate FILE(s) to standard output. (prints files)
cat any_file1 any_file2 ... any_file_n

# Prints files
less any_file

# Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.
cp source_file target_path

# Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.
mv source_file target_path

# rm removes each specified file.  By default, it does not remove directories.
rm file_to_be_deleted