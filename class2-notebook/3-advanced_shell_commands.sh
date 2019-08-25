# Advanced commands in shell script

# Print  the  first  10 lines of each FILE to standard output
head filename.txt

# Print  the  last  10  lines of each FILE to standard output.
tail filename.txt

#  Print newline, word, and byte counts for each FILE
wc filename.txt
wc -l file.txt

# Connecting commands using pipe
head -n5 file.txt | sort

# Filter  adjacent matching lines from INPUT
uniq filename.txt

# curl  is  a tool to transfer data from or to a server
curl www.google.com

# Outputting results to a file using > or >>
cat file1.txt >> output.txt






