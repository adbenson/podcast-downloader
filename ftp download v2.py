import ftplib
import sys

# Declare the important information we'll need later.
# We could use these in place, but putting them all together at the top of the file makes it easier to find and change if necessary
# By convention, variables that use all capital letters shouldn't be changed later in the program
HOST = "ftp.20thecountdown.com"
DATE = "03-26-22"
HOUR = "1"

ftp = ftplib.FTP(HOST)
ftp.login()

# Change Working Directory (CWD) to the following
ftp.cwd(DATE + "/Hour " + HOUR)

# I think "nlst" is short for "name list"
dir_contents = ftp.nlst()

# The out of the nlst command above includes the self and parent folder references called "." and ".."
# We just want the files so we're going to filter out those two entries from the list
file_names = list(filter(lambda n: n != "." and n != "..", dir_contents))
# Print the file names out to the console, for convenience
print(file_names)

# Go through all the files found in the folder and download each using the same file name
for file in file_names:
	ftp.retrbinary("RETR " + file, open(file, 'wb').write)

# Close the connection (not strictly necessary, but good practice)
ftp.quit()
