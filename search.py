import csv

readfile = open('std_data.csv',"r")

filereader = csv.reader(readfile)

city = input("enter the city name to search std: ")

for row in filereader:
	for field in row:
		if field == city.upper():
			stdno = eval(row[2])
			# print(stdno)
			# print(len(str(stdno)))
			x=len(str(stdno))
			if x==2:
				std_str = '%0*d' % (3,stdno)
			elif x==3:
				std_str = '%0*d' % (4,stdno)
			else:
				std_str = '%0*d' % (5,stdno)
			print(std_str)
			#print(len(std_str))	
