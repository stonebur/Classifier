'''
bingsearch.py
Further instructions found in INSTRUCTIONS_PLEASE READ.
Image scraper that uses the Microsoft Bing Image Search API v7.
This tool is used to collect data sets that can be used by the
image classifier to train with. Segments of this code are 
adapted from Adrian Rosebrock's tutorial "How to (quickly)
build a deep learning image dataset".
Information about the API can be located in the documentation
at https://docs.microsoft.com/en-us/azure/cognitive-services/bing-image-search/
'''

from requests import exceptions
import argparse
import requests
import os


API_KEY = "63f783587b9842c0a87b22e4354725f5"	#Type in key here
#Set NUM_RESULTS to desired number of images to gather
NUM_RESULTS = 250
RESULTS_PER_PAGE = 50	#max 150

search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"


query = input("Enter image to search for: ")

#creates directory in catvdog, named after query
dirPath = "./tf_files/catvdog/{}".format(query.replace(" ", ""))
os.mkdir(dirPath)

#possible exceptions common when using request library
EXCEPTIONS = set([IOError, FileNotFoundError, 
	exceptions.RequestException, exceptions.HTTPError,
	exceptions.ConnectionError, exceptions.Timeout])

#calls Bing search APIs, returns results as JSON object
headers = {"Ocp-Apim-Subscription-Key" : API_KEY}
params = {"q": query, "offset": 0, "count": RESULTS_PER_PAGE}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

print("Starting search for '{}'".format(query))

#total number of images gathered
total = 0

#outer loop grabs one page of results, while the inner loop iterates over each image in that
#group and writes it to disk
for offset in range(0, NUM_RESULTS, RESULTS_PER_PAGE):
	#increments offset to next page
	params["offset"] = offset
	response = requests.get(search_url, headers=headers, params=params)
	response.raise_for_status()
	search_results = response.json()


	for v in search_results["value"]:
		try:
			r = requests.get(v["contentUrl"], timeout=15)

			print("Fetching: {}".format(v["contentUrl"]))

			#grabs the file extension from the url
			ext = v["contentUrl"][v["contentUrl"].rfind("."):]
			#path to image file
			p = dirPath + '/' + str(total) + ext 
			
			#write image to disk
			f = open(p, "wb")
			f.write(r.content)
			f.close()

		except Exception as e:
			if type(e) in EXCEPTIONS:
				continue
			
		
			
		total+=1	

