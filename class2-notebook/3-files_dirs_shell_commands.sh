### Basic files and directories shell commands

# Create the directory, if they do not already exist
mkdir <my_new_directory>                                          # Creates single directory
mkdir -p <my_new_directory>/<my_new_directory>/<my_new_directory> # Creates multiple levels of directories

# Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.
cp <source_file> <target_path>    # Copy single file
cp -r <source_file> <target_path> # Copy directory and files inside it

# Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.
mv <source_file> <target_directory>     # Moves single file from source_file to target_path
mv <old_file_name> <new_file_name> # Renames an existing file
mv *.csv my-target-directory       # Moves all files with an csv extension to `my-target-directory`
mv data* my-target-directory       # Moves all files starting with data to `my-target-directory`

# Update  the  access  and modification times of each FILE to the current time
touch <any_file>

# nano / vi (visually: text edit or vscode) : Creates and/or edit files
nano <any_file>
vi <any_file>

# Concatenate FILE(s) to standard output. (prints files)
cat any_file1 any_file2 ... any_file_n

# Prints paginated files
less any_file

# rm removes each specified file.  By default, it does not remove directories.
rm <file_to_be_deleted>            # Deletes file
rm -r <directory_to_be_deleted>    # Deletes empty directory