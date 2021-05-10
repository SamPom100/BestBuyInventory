import requests

headers = {"User-Agent":"Mozilla/5.0"}


SKU_3060 = [6439402,6460665,6454329,6460666,6444444,6429440,6454688,6429442,6452573,6454328,6452940,6442484,6446660,6444445,6444449,6441172,6442485,6462173,6454319]

def inStock(input):
	searchURL = 'https://www.bestbuy.com/site/searchpage.jsp?st='+str(input)
	source = requests.get(searchURL, headers=headers).text
	firstIndex = source.index("<title >",source.index('<!-- start simple component shop-pdp-seo-metadata'))
	secondIndex = source.index("</title>",firstIndex)
	title = (source[firstIndex+8:secondIndex])
	if(source.__contains__('class="btn btn-disabled btn-lg btn-block add-to-cart-button')):
		return "Not in Stock - "+title
	elif (source.__contains__('class="btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button"')):
		return "In Stock - "+title
	else:
		return "Error"

def buyURL(input):
	return "https://api.bestbuy.com/click/~/"+input+"/cart/"

for x in SKU_3060:
	print(inStock(x))
