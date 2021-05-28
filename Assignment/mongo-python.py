'''
1. Run a program every 5 seconds
2. Use psutil to collect metrics about CPU & memory
3. Write the metrics into a csv. file
'''
import time
import psutil
import csv
import datetime
from pymongo import MongoClient

filename = "cpu_mem.csv"

#GET DB Conncetion 1 time
url = "mongodb://python:python@ds123695.mlab.com:23695/pythonapp"
client = MongoClient(url)    
db = client["pythonapp"]
 
def write_to_mongodb(sno,cpu, mem, date):
    db.Metrics.insert_one({
            "id": sno,
            "cpu": cpu,
            "mem": mem,
            "date": date
        })
    print ("Inserted to Db")

def write_header_to_a_csv_file():
    with open(filename, "ab") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["sno","cpu","mem","date"])


def write_to_csv(sno,cpu, mem, date):
    print (cpu,mem,date)
    with open(filename, "ab") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([sno,cpu,mem,date])

def task_to_be_executed(index):
    cpu,mem = collect_cpu_mem_metrics()
    date = datetime.datetime.now()
    date = str(date)[:19]
    write_to_csv( index, cpu, mem , date )
    write_to_mongodb( index, cpu, mem , date )
    

def run_something_every_x_seconds(seconds):
    index = 1
    while (True):
        """
        Every x second block
        """
        print ("Running every %s Seconds" %seconds )
        # function to be executed, every x seconds
        task_to_be_executed(index)
        index += 1
        time.sleep( seconds )


def collect_cpu_mem_metrics():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    return (cpu_percent, mem_percent)

write_header_to_a_csv_file()
run_something_every_x_seconds(5)