#list downloader
try:
	import time
	import os
	import subprocess
	import os.path
	import fnmatch
except:
	print("You seem to be missing a library")
	pass


#Pause Function
def Pause():
	pase = raw_input("Press Enter.. ")
	return

def Banner():
	os.system('cls' if os.name == 'nt' else 'clear')
	
	print("                                                |>>>")
	print("                                                |")
	print("                                            _  _|_  _")
	print("                                           |;|_|;|_|;|")
	print("      IP Fortress v1.0                     \\.    .  /")
	print("      A python run firewall rule setter     \\:  .  /")
	print("      using public lists from                ||:   |")
	print("      https://github.com/stamparm/ipsum      ||:.  |")
	print("                                             ||:  .|")
	print("                                             ||:   |       \,/")
	print("                                             ||: , |            /`\"")
	print("                                             ||:   |")
	print("                                             ||: . |")
	print("              __                            _||_   |")
	print("     ____--`~    '--~~__            __ ----~    ~`---,              ___")
	print("-~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~")
	print("-----------------------------------------------------------------------------------")
    #list files in working directory

def Run():
	Banner()
	i=0
	print("Working Directory Files ")
	print("___Name_____IP Amount")
    #list files in working directory
	#list files in current directory
	listOfFiles = os.listdir('./')
	pattern = "*.txt"
	for entry in listOfFiles:
		if fnmatch.fnmatch(entry, pattern):
			print("|| " + entry + " || " + str(len(open(entry).readlines(  ))))
			i -=1
		else:
			i += 1
	#if i > 0:
		#print("There are no list files (.txt) in this folder")
	filename= raw_input("Enter list file you wish to use, type all for all files to be run automaticlly, or leave blank and hit enter to return to the last screen: ")
	if filename:
		if filename == "all":
			try:
				listOfFiles = os.listdir('./')
				pattern = "*.txt"
				for entry in listOfFiles:
					if fnmatch.fnmatch(entry, pattern):
		#set x equal to the amount of lines in the file
						print("Apply " + entry + "?   ***********************************************************")
						Pause()
						count = len(open(entry).readlines(  ))
						x = 0
						with open(entry, 'r') as file:
							data = file.readlines()
					#print(data)
							while x < count:
				  #calculate percentage done
	
				  # now change the 2nd line, note that you have to add a newline
								print("Adding "+ str(x +1) +"/"+ str(count)+ " in list to Blocked IPs. ******************* IP:  " + (data[x]))
								try:
									command = "sudo ufw deny from " + str(data[x])
									command2= "sudo ufw deny out from any to " + str(data[x])
									print(command)
									print(command2)
									os.system(command )
									os.system(command2)
								except:
									print("something went wrong")
									pass
								x+=1
				Pause()
						
			except:
				print("Thats not a file")
				pass		
		else:
			try:
		#set x equal to the amount of lines in the file
				count = len(open(filename).readlines(  ))
				x = 0
				with open(filename, 'r') as file:
					data = file.readlines()
					#print(data)
					while x < count:
				  #calculate percentage done

				  # now change the 2nd line, note that you have to add a newline
						print("Adding "+ str(x +1) +"/"+ str(count)+ " in list to Blocked IPs. ******************* IP:  " + (data[x]))
						try:
							command = "sudo ufw deny from " + str(data[x])
							print(command)
							os.system(command )
						except:
							print("something went wrong")
							pass
						x+=1
				Pause()
				Run()
			except:
				print("Thats not a file")
				pass

	else:
		Main()
		
#Update lists
def update():
	Banner()
	print("Downloading lists from https://github.com/stamparm/ipsum")
	x=1
	while x <= 8:
		try:
			listName = (str(x) + ".txt")
			os.system("wget -q https://raw.githubusercontent.com/stamparm/ipsum/master/levels/" + listName + " -O ./" + listName)
			print("List " + listName + " Downloaded and or Updated!")
		except:
			print("List " + listName + " could not be downloaded")
			pass
		x+=1
	Pause()
	return
		
		
		
#main menu

def Main():
	Banner()
	print("[1]. Apply lists ")
	print("[2]. Update lists")
	print("[3]. Quit")
	choice = raw_input("ENter CHoice: ")
	if choice:
		if choice == '1':
			Run()
		if choice == '2':
			update()
		if choice == '3':
			quit()
		else:
			Main()
	else:
		Main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
Main()