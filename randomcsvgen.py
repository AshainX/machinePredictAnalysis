'''
DATA DESCRIPTION :

    machine_id = Random machine ID like M-1 M-2.... upto M-50
    temperature = taking Temps in the range 50-120
    run_time = Run time in hours (1-24 hours)
    downtime_flag = Downtime flag (0 or 1)

'''

import random
import csv

opfile = "data.csv"
rows = 2000        #generating rows of random values 

def dataGeneration(rows):  #generating random data
    data = []
    for i in range(rows):
        machine_id = f"M_{random.randint(1, 50)}" 
        temperature = round(random.uniform(50, 120), 2)
        run_time = round(random.uniform(1, 24), 2) 
        downtime_flag = random.choice([0, 1]) 
        data.append([machine_id, temperature, run_time, downtime_flag])
    return data

data = dataGeneration(rows)


#putting in file here in csv format
with open(opfile, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"])
    writer.writerows(data)

print(f"random data saved to : '{opfile}'.")