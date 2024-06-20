def bottle_song():
	# write your code here!
	
	
		num_bottles = input("How many bottles are on the wall? ")
		finalsong = bildsong(int(num_bottles))
		print(finalsong)

	
		
		


def bildsong(num_bottles):
			if num_bottles == 1: 
				song = []
				
				song.append("Go to the store and buy some more, 99 bottles of beer on the wall")
				song.append("No more bottles of beer on the wall, no more bottles of beer") 
				song.append("1 bottle of beer on the wall, 1 bottle of beer.")
				song.append("Take one down and pass it around, no more bottles of beer on the wall.")

					
				return song
			else:  
				song = []
				song.append(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
				song.append(f"Take one down and pass it around, {num_bottles-1} bottles of beer on the wall.")

				return song.append(bildsong(num_bottles-1)) 


bottle_song()
