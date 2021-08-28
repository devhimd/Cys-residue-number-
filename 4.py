fasta = open('input.fasta', 'r+')
for line in fasta.read().split('\n'):
    if line.startswith(">"):
   	 header = line
   	 print(header)
   	 #fileline = fasta.readline()
   	 #line = fileline
   	# line.rstrip('\n')
   	# count = 0
   	# break
   	# ('\n')
    else: 
      	#print(line_list)
      	indexes = []
      	for i in range(0, len(line)-1):
      	      		if line[i] == 'C':
      	      				indexes.append(i+1)
      	print("Cys : ", indexes)	    		
	
	

# Program to find the indexes of Cys in the given mutlifasta sequences 
