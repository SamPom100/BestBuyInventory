from sendMail import sendMail
import requests

headers = {"User-Agent":"Mozilla/5.0"}


SKU_3060 = [6439402,6460665,6454329,6460666,6444444,6429440,6454688,6429442,6452573,6454328,6452940,6442484,6446660,6444445,6444449,6441172,6442485,6462173,6454319]

def inStock(input):
	try:
		searchURL = 'https://www.bestbuy.com/site/searchpage.jsp?st='+str(input)
		source = requests.get(searchURL, headers=headers).text
		firstIndex = source.index("<title >",source.index('<!-- start simple component shop-pdp-seo-metadata'))
		secondIndex = source.index("</title>",firstIndex)
		title = (source[firstIndex+8:secondIndex])
		if(source.__contains__('class="btn btn-disabled btn-lg btn-block add-to-cart-button')):
			print("Not in Stock")
			return "No"
		elif (source.__contains__('class="btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button"')):
			print("In Stock - "+title)
			return input
		else:
			return "No"
	except:
		return "No"

def buyURL(input):
	return "https://api.bestbuy.com/click/~/"+str(input)+"/cart/"

while(True):
	for x in SKU_3060:
		temp = inStock(x)
		if not(temp == "No"):
			sendMail('IN STOCK ALERT',"This item is in stock\n"+buyURL(temp))
			print("Mail Sent!")
			





