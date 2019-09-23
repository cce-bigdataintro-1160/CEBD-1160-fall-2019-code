### Advanced commands in shell script

# Print  the  first  10 lines of each FILE to standard output
head filename.txt
head -n5 filename.txt

# Print  the  last  10  lines of each FILE to standard output.
tail filename.txt
tail -n5 filename.txt

# Print the shape, newline, word, and byte counts for each FILE
wc filename.txt
wc -l file.txt

# Connecting commands using pipe
head -n5 file.txt | sort

# Filter  adjacent matching lines from INPUT
uniq filename.txt

# curl is  a tool to transfer data from or to a server
curl http://donnees.ville.montreal.qc.ca/dataset/1d785ef8-f883-47b5-bac5-dce1cdddb1b0/resource/e62322fb-3e14-4ee0-b724-a77190dac8e7/download/remorquages.csv

# Outputting results to a file using > or >>
cat file1.txt > output.txt   # Always overwrites files
cat file1.txt >> output.txt  # Always appends to files


# cut



