### Basic files and directories shell commands

# Create the directory, if they do not already exist
mkdir <my_new_directory>

# Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.
cp source_file target_path

# Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.
mv source_file target_path
mv *.csv my-target-directory  # moves all files with an csv extension to `my-target-directory`
mv .csv my-target-directory  # moves all files with an csv extension to `my-target-directory`

# Update  the  access  and modification times of each FILE to the current time
touch <any_file>

# nano / vi (visually: text edit or vscode) : Creates and edit files
nano <any_file>
vi <any_file>

# Concatenate FILE(s) to standard output. (prints files)
cat any_file1 any_file2 ... any_file_n

# Prints files
less any_file

# rm removes each specified file.  By default, it does not remove directories.
rm file_to_be_deleted