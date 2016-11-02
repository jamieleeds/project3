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

def part_Three():

	base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
	rqt = requests.get(base_url)
	soup = BeautifulSoup(rqt.text, 'lxml')
	
	#bsi_admission = soup.find_all('class_="ytp-thumbnail-overlay-image")

	bsi_admission = soup.find_all('div')

	
	print('-'*72)
	print(type(bsi_admission))
	print(dir(bsi_admission))

	for div in soup.find_all("div"):
		classes = 
		print(div.get("class"))
		for c in div.get("class"):
			print(c)



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
part_Three()