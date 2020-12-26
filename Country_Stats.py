import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

country = input("Enter a country: ")
country_cleaned= country.replace(" ", "%20")

my_url = 'https://en.wikipedia.org/wiki/' + country_cleaned

#opening a connection and grabbing a page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#focusing on just finding the first instance of an info table
infobox = page_soup.find("table",{"class":"infobox geography vcard"})

infobox_narrowed = infobox.findAll("td")
#loop to find which section of the infobox that population is involved in. 
index = -1

for i in range(len(infobox_narrowed)):   
    #print("Currently Searching Section: " + str(section))
    if "population" in str(infobox_narrowed[i]):
        index = i
        break

#enable for developer mode, to bug where to find a section
#print("\nThe chosen one is section number: " + str(index) + "\n")

population = str(infobox_narrowed[index].text.strip())
string_population = population.split("[", 1)[0] #"[" was chosen after realizing that's the indicator to population
int_population = int(string_population.replace(',', ''))

print("The population of " + country + " is " + string_population)

#### could just write a function instead but I copy pasted it:

country2 = input("Enter another country: ")
country_cleaned= country2.replace(" ", "%20")

my_url = 'https://en.wikipedia.org/wiki/' + country_cleaned

#opening a connection and grabbing a page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#focusing on just finding the first instance of an info table
infobox = page_soup.find("table",{"class":"infobox geography vcard"})

infobox_narrowed = infobox.findAll("td")
#loop to find which section of the infobox that population is involved in. 
index = -1

for i in range(len(infobox_narrowed)):   
    #print("Currently Searching Section: " + str(section))
    if "population" in str(infobox_narrowed[i]):
        index = i
        break

#enable for developer mode, to bug where to find a section
#print("\nThe chosen one is section number: " + str(index) + "\n")

population = str(infobox_narrowed[index].text.strip())
string_population = population.split("[", 1)[0] #"[" was chosen after realizing that's the indicator to population
int_population2 = int(string_population.replace(',', ''))
print("The population of " + country2 + " is " + string_population)
print("----------------------")
print("The population of " + country2 + " is about " + str(round(int_population2/int_population,2)) + " times the size of " + country)
