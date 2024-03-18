#!/usr/bin/python3

if __name__ == "__main__":
	"""Print the number of and list of arguments."""
	import sys
	t = 0
	if len(sys.argv) == 1:
		print(f"{len(sys.argv) - 1} arguments.")
	elif len(sys.argv) == 2:
		print(f"{len(sys.argv) - 1} argument")
	else:
		print(f"{len(sys.argv) - 1} arguments")
	for i in range(1, len(sys.argv)):

		print(f"{i}: {sys.argv[i]}")
		for t in sys.argv:
			print(int(t))
