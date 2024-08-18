#!/usr/bin/python3
"""
write a func that writes a string TXT with UTF,
return a num of caracters written
"""

def write_file(filename="", text=""):
	"""
	this func with write open or create txt file  for writting
	arg filename is file 
	arg text contain the string 
	return the num of craters
	"""
	with open(filename, "w", encoding="utf-8") as file:
		return file.write(text)
