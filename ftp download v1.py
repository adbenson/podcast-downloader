# Tell python we need to use the standard FTP library
import ftplib
# Tell python we need to use the standard system library (for saving the file)
import sys

# Create a new FTP object
ftp = ftplib.FTP("ftp.20thecountdown.com")

# Log in anonymously
ftp.login()

# Change Working Directory (CWD) to the following
ftp.cwd("03-26-22/Hour 1")

# Open a new file in "write binary" (wb) mode
file = open("downloaded.mp3", 'wb')

# RETRieve binary file, save it to the download file
ftp.retrbinary("RETR 20 2213 H1 S1.mp3", file.write)

# Close the connection (not strictly necessary, but good practice)
ftp.quit()
