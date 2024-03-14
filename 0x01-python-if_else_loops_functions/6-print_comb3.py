#!/usr/bin/python3
for i in range(10):
	for u in range(i+1, 10):
		if u == 9 and i == 8:
			print(89)
		else:
			print(f"{i}{u}" ,end=', ')
