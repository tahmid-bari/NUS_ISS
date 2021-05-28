import time
import requests
#generic routine for capturing data_api from data.gov.sg
#make changes to URL and filename only

from pprint import pprint
import csv
headers=[]
off = 10
lim = 10
total=0

# filename="data.csv"
# url = "https://data.gov.sg/api/action/datastore_search?offset=%s&limit=%s&resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84"
filename="jobs.csv"
url = "https://data.gov.sg/api/action/datastore_search?offset=%s&limit=%s&resource_id=34b5dc65-4a44-4fee-9431-7131c347f9cf"
"https://data.gov.sg/api/action/datastore_search?offset=%s&limit=%s&resource_id=f927c39b-3b44-492e-8b54-174e775e0d98"
def collectdata(url):
    custom_header = {
        "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    }
    content = requests.get(url).json()
    return content

def write_csv_headers_and_get_total():
#   perform a read to get headers
    current_url=url %(0,10)
    content = collectdata(current_url)
    global total
    total=content.get("result").get("total")
    with open (filename,"wb") as csvfile: #change mode to 'at' for append
        csv_writer =csv.writer(csvfile,delimiter=",")
        fields=content.get("result").get("fields")
        for field in fields:
            header=field.get("id")
            headers.append(header)
        print headers
        csv_writer.writerow(headers)
        
def write_records(total):
    for i in range(0,total,off):
        current_url = url % (i,lim)
        print current_url
        content = collectdata(current_url)
#        pprint(content)
# get the records
        records=content.get("result").get("records")
#        field_name = (records[0].keys()) # using this will not return fields in correct order
#        pprint (field_name)
#     pprint (records)
        for record in records:
            record_array=[]
            for key in headers:
                record_array.append(record.get(key))
#         print(record.get(headers[0]),record.get(headers[1]),record.get(headers[2]),record.get(headers[3]))
            print record_array
            with open (filename,"ab") as csvfile: #change mode to 'at' for append
                csv_writer =csv.writer(csvfile,delimiter=",")
                csv_writer.writerow(record_array)
        time.sleep(2)
        

        
write_csv_headers_and_get_total()
print total
write_records(total)