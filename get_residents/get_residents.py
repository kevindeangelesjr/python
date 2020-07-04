import requests

### Variables ###
whitepages_baseurl = "https://whitepages.com/address/"

### Get User Input ###
address = input("Please enter the address (in the format of 2065 Store Rd, Harleysville PA 19426): ")
address = address.replace(',', '') # Remove all commas from input
address_list = address.split() # Convert address string to a list

### Split out inidividual elements of address into separate variables
num = address_list[0]
street_name = address_list[1]
street_type = address_list[2]
town = address_list[3]
state = address_list[4]
zip = address_list[5]

address_url = whitepages_baseurl + num + "-" + street_name + "-" + street_type + "/" + town + "-" + state

print(address_url)

res = requests.get(address_url)

print(res.text)