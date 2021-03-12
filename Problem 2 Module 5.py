Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
>>> for i in numbers:
    print(i)

    
12
10
32
3
66
17
42
99
20
>>> squared = [ ]
>>> for i in numbers:
	squared.append(i * i)
	print("The square of", i, "is", squared)

	
The square of 12 is [144]
The square of 10 is [144, 100]
The square of 32 is [144, 100, 1024]
The square of 3 is [144, 100, 1024, 9]
The square of 66 is [144, 100, 1024, 9, 4356]
The square of 17 is [144, 100, 1024, 9, 4356, 289]
The square of 42 is [144, 100, 1024, 9, 4356, 289, 1764]
The square of 99 is [144, 100, 1024, 9, 4356, 289, 1764, 9801]
The square of 20 is [144, 100, 1024, 9, 4356, 289, 1764, 9801, 400]
>>> 