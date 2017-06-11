import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


# THIS PYTHON SCRIPT IS USED FOR CREATING A CSV FILE OF STD CODES OF INDIAN CITIES

my_url = "https://www.spotthelost.com/india-std-codes.php"

# opening up connection
uClient = uReq(my_url)

#grabbing the page
page_html = uClient.read()
uClient.close()

#parse the html page
page_soup = soup(page_html,"html.parser")

#city = page_soup.findAll("font",{"color":"blue"})
# skip first row i.e. start from city[1]

filename = "std_data.csv"
f = open(filename,"w")
header = "CITY,CIRCLE,STD\n"
f.write(header)
f.close()

test = page_soup.findAll("b")
x = len(test)
print(x)

i = 10
j= x-1
while i < j:
	city = test[i].text
	circle = test[i+1].text
	std = test[i+2].text
	i=i+3
	f = open(filename,"a")
	f.write(city + "," + circle + "," + std + "\n")
	f.close()

print("data retrieved")
