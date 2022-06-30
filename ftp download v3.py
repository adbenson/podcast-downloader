import ftplib
import sys
# The datetime library has lots of useful stuff, but we're telling python we only want the date functions
from datetime import date

# PARAMETERS

HOST = "ftp.20thecountdown.com"
SUBFOLDERS = ["Hour 1", "Hour 2"]
# If `None`, the program will use the computer's current date
DOWNLOAD_DATE = "03-19-22"
DOWNLOAD_FOLDER = "downloaded"

# FUNCTIONS - creating reusable functions for use later

# Returns today's date in the format: mm-dd-yy
def get_date_string():
	today = date.today()
	# "strftime" is short for "string format time", turn a date object into a string in the desired format
	date_string = today.strftime("%m-%d-%y")
	return date_string

# Downloads a file at the given path and filename to the current folder
def download_file(ftp, path, filename):
	file = open(DOWNLOAD_FOLDER + "/" + filename, 'wb')
	ftp.retrbinary("RETR " + path + "/" + filename, file.write)
	
# Returns true if the given filename is not "." or ".."
def not_folder(filename):
	return filename != "." and filename != ".."

# Takes a list of ftp folder items and returns the names of just the files
# Each item is a tuple (like a list) of the item's name, and a dictionary of its properties
def find_files(items):
	# We filter the list for items with a property type of "file"
	files = list(filter(lambda i: i[1]["type"] == "file", items))
	# Then map it to just the file name	
	file_names = list(map(lambda f: f[0], files))
	return file_names
	
# Returns a list of files in the given path
def get_filenames(ftp, path):
	# "mlsd" is a more powerful FTP command that gives you helpful metadata for each item in a folder, we can use this metadata to determine which items are files and which are folders
	dir_contents = list(ftp.mlsd(path))
	file_names = find_files(dir_contents)
	return file_names
	
def download_files_in_folder(ftp, path):
	file_names = get_filenames(ftp, path)
	for file in file_names:
		download_file(ftp, path, file)
		
# PROGRAM - this is where it actually starts doing things

ftp = ftplib.FTP(HOST)
ftp.login()

date_string = DOWNLOAD_DATE or get_date_string()

for folder in SUBFOLDERS:
	path = date_string + "/" + folder
	download_files_in_folder(ftp, path)

ftp.quit()
