import csv
import requests
from bs4 import BeautifulSoup  
from HTMLParser import HTMLParseError
main_url = "https://www.lazada.sg/shop-laptops/lenovo"
filename = "lenovo_lazada.csv"
with open(filename,"w") as csvfile:
        writer = csv.writer(csvfile)
        header = ["Lenovo_Name","Price", "Installments"]
        writer.writerow(header)
lenovo_url_list = []
def convert_web_content_to_soup(main_url):
    web_content = requests.get(main_url).text
    soup = BeautifulSoup(web_content, "html.parser")
    return soup
# description Web html code = <div class="c-product-card__img-placeholder">
# price web html code = a href="/apple-lenovo-pro-13-inch-29ghz-256gb-20976177.html
 
def get_web_lenovo_details_url(main_url):
    soup = convert_web_content_to_soup(main_url)
    web_lenovo_details_list = soup.find_all ("a",{"class":"c-product-card__img-placeholder-inner"})
    temp_list = []
    for lenovo in web_lenovo_details_list:
        lenovo_url = lenovo.get("href")
        full_url = main_url + lenovo_url
        temp_list.append(full_url)
        # print full_url     # print url related to each lenovo
    return temp_list
#Check if the tag is empty or none, and return true or false.
#This will take care of the error when the website does not have what the code is scraping.
def isnone(tag):
    if tag == None or tag == '':
        return True
    else:
        return False
lenovo_result_url = get_web_lenovo_details_url(main_url)  
lenovo_url_list.extend(lenovo_result_url)
for page_number in range (3, 4):           # print everything in Page 1 & 2
    page_url = main_url + "?page=%s"%page_number 
    lenovo_result_url = get_web_lenovo_details_url(page_url)
    lenovo_url_list.extend(lenovo_result_url)
# getting the lenovo description and price
# website --> h1 id="prod_title"
# website = span id="special_price_box">2,588.00
# <span id="product_saving_percentage" class="price_highlight"> 4%</span>
# <span class="prod_pricebox_installments_amount_value">
def get_lenovo_details(main_url):
    soup = convert_web_content_to_soup(main_url)
    
    h1_tag = soup.find("h1",{"id":"prod_title"})
    try:
        print (h1_tag.text.strip())     #.strip() will remove empty spaces, etc               
        description = h1_tag.text.strip().encode("utf-8")
    except:
        description = "No info"
        return "No info"
        
    
    lenovo_price = soup.find("span",{"id":"special_price_box"})
    try:    
        print(lenovo_price.text.strip())
        price = lenovo_price.text.strip()
    except:
        price = "No price"
        print ("No price")
       
    
    installment = soup.find("span",{"class":"prod_pricebox_installments_amount_value"})
    if not isnone(installment):
        try:
            print(installment.text.strip())
            installments = installment.text.strip()
        except:
            savings = "No Installment"
            print("No Installment")
        
    
# write to a csv file        
    with open(filename,"a") as csv_file:
        writer = csv.writer(csv_file)
        
        description = h1_tag.text.strip().encode("utf-8")
        price = lenovo_price.text.strip()
        installments = ""
        if not isnone(installment):
            installments = installment.text.strip()
            
        table = [description, price,installments]
        writer.writerow(table)
        
for main_url in lenovo_url_list:
    get_lenovo_details(main_url)
Add Comment