# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
from bs4 import BeautifulSoup 

def Beautiful_Soup():

	base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
	rqt = requests.get(base_url)
	soup = BeautifulSoup(rqt.text, 'lxml')
	
	soup = BeautifulSoup(
		str(soup.prettify()).replace(" student ", " AMAZING student ") #replacing student with Amazing Student 
		, 'lxml'
		)

	
#-----------------------------------------------------
	
	#2 and #3
	for img in soup.find_all("img"):
		#print('-'*72)
		if img.get('src').find("bsi_exposition_041316_192.jpg") >= 0: #replacing main image
			#print(img.get('src'))
			img['src'] = "./img/me.jpg"
		else:
			img['src'] = "./img/logo.png" #replacing local image

	print(soup.prettify())

#------------------------------------------------------------------------


'''
soup = BeautifulSoup(str(bsi_admission), 'lxml')  #sending it to be broken into Beautiful Soup
	print("\n"+'='*72)
	print("Michigan Daily Most Read")
	print('-'*72)
	for li in soup.find_all('li'): #finding all the lists in tag
		print(li.text) 
'''






#-------------
#main
#---------------
Beautiful_Soup()