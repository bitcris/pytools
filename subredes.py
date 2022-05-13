x = int(input("CIDR: "))

bit = 32 - x

print("bits:",bit,"\n\n")

#OCTETO 1
if(bit<9):
	o1 = bit
	
if(bit>8 and bit<17):
	o1 = 8
	
if(bit>16 and bit < 25):
    o1 = 8
 
if(bit>24):
    o1 = 8
    
print("OCTETO1:",o1)	



#OCTETO 2
if(bit<9):
	o2 = 0
		
if(bit>8 and bit<17):
	o2 = bit - 8
		
if(bit>16 and bit <25):
	o2 = 8
											
if(bit>24):
	o2 = 8
											
print("OCTETO2:",o2)


#OCTETO 3
if(bit<9):
	o3 = 0
	
if(bit>8 and bit < 17):
     o3 = 0
     
if(bit>16 and bit < 25):
	o3 = bit - 16
	
if(bit>24):
	o3 = 8
	
print("OCTETO3",o3)



#OCTETO 4
if(bit<9):
	o4=0
	
	
if(bit>8 and bit <17):
	o4=0
	

if(bit>16 and bit <25):
	o4=0
				
								
if(bit>25):
	o4 = bit - 24																							
																													
print("OCTETO4:",o4)		
																				
				
mask = (o1,o2,o3,o4)
print(mask)
