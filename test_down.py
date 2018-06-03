import urllib.request
import json
import re

with open('photo.json','r') as infile:                          # Input your file
	data = json.load(infile)
	print(type(data))                                           # Cross check the load
	for k,v in data.items():                                    # Key Value pairs 
		print("------------------------------------------")
		print(type(v))
		count = 1
		for ele in v:
			print(str(ele) + "\n")
			count = count + 1
			url = ele["imageURI"]                               # Keyname for the image url
			print(url)                                          # Printing on the console
			download_path = "data/image"+str(count)+".jpg"      # Make a new directory to store the data 
			urllib.request.urlretrieve(url, download_path)
print(" ALL Downloaded")


