"""
Python code to process data.txt

"""

"""
l =[1,2,34,5,1]


d={'first_name':'John',
	'last_name':'Doe',
	'gpa': 3.5
}
print(d['gpa'])
"""
# Open the file 
infile = open("data.txt")
# Skip first two lines
infile.readline()
infile.readline()
# Store the rest of lines in the list lines
lines = infile.readlines()
#print(lines)

# Create an empty list 
data =[]
# for every line in lines
for line in lines:
	# strip line
	line = line.strip()
	# split each line by |, save as tokens
	tokens = line.split("|")
	# for i in range of 0 and the length of tokens
	for i in range(0,len(tokens)):
		# Strip each token
		tokens[i] = tokens[i].strip()
	# append tokens to data
	data.append(tokens)
	
#print(data)

# Create empty dictionary
divisions={}
# Set div_id to 1
div_id=1
# Process the contents of data
for i in range(0, len(data)):
	# Get the tokens stored in position i of data
	tokens=data[i]
	# Get the department name from token position 3
	dept = tokens[3]
	# Get the division name from token position 4
	div = tokens[4]
	#print(dept+" "+div)
	# If div is not a key in divisions dictionary
	if div not in divisions.keys():
		# Add div as a key and store div_id and dept in a list and 
		# store the list as the value of div key
		divisions[div]=[div_id,dept]
		# Update div_id by 1
		div_id+=1
	else:
		# Retrieve the value of div key and store in departments
		departments = divisions[div]
		# If dept is not already in departments
		if dept not in departments:
			# Add dept to departments
			departments.append(dept)

print(divisions)

# Processing the divisions dictionary
for key in divisions.keys():
	# Get the div_id from the first element of the list
	div_id = divisions[key][0]
	# Create the insert statement with div_id and key name
	print("Insert into divisions(id,div_title) values("+str(div_id)+",'"+str(key)+"');")

# Assign 1 to dept_id
dept_id=1
# Create a dictionary with department names as keys
departments={}
# Process the divisions dictionary
for key in divisions.keys():
	# Retrieve the list store in the key
	l=divisions[key]
	# Get the div_id from the first element in list l
	div_id=l[0]
	# Process list l starting with position 1
	for i in range(1,len(l)):
		# Get the department title
		dept_title = l[i]
		if dept_title not in departments.keys():
			departments[dept_title]=dept_id
		
		# Put the insert statement together
		print("Insert into departments(id,dept_title,div_id) values("+str(dept_id)+",'"+dept_title+"',"+str(div_id)+");")
		dept_id+=1

#print(departments)

# Process data list to get employee information
for i in range(0,len(data)):
	# Retrieve tokens at position i
	tokens = data[i]
	first_name = tokens[0]
	last_name = tokens[1]
	e_mail = tokens[2]
	dept_title = tokens[3]
	dept_id=departments[dept_title]
	print("Insert into employees(first_name,last_name,e_mail,dept_id) values('" + first_name + "','" + last_name + "','" + e_mail + "'," + str(dept_id) + ");")

