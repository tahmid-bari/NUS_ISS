'''
1. Run a program every 5 seconds
2. Use psutil to collect metrics about CPU & memory
3. Write the metrics into a csv. file
'''
import time
import psutil
import csv
import datetime

filename = "cpu_mem.csv"

def write_header_to_a_csv_file():
    with open(filename, "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["sno","cpu","mem","date"])


def write_to_csv(sno,cpu, mem, date):
    print (cpu,mem,date)
    with open(filename, "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([sno,cpu,mem,date])

def task_to_be_executed(index):
    cpu,mem = collect_cpu_mem_metrics()
    date = datetime.datetime.now()
    date = str(date)[:19]
    write_to_csv( index, cpu, mem , date )
    

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