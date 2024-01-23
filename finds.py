import csv
h0 = ['%','%','%','%','%','%']
with open('enjoy_sport.csv') as csv_file:
	readcsv = csv.reader(csv_file,delimiter=',')
	print(readcsv)
	data = []
	print("\nThe given training examples are:")
	for row in readcsv:
		print(row)
		if row[len(row)-1].upper() == "YES":
			data.append(row)

print("\nThe positive examples are:")
for row in data:
	print(row)
print("\n")

h1= data[0]
h1.pop(len(h1)-1)

print("h0 =",h0)
print("\n")

print("h1 =",h1)
print("\n")

x = 2
for row in data:
	for i in range(len(h1)):
		if h1[i]!=row[i]:
			h1[i]='?'
	print(f"h{x} =",h1)
	x += 1

