# -------------------------------------------------------------
# Author: Bartosz Szczepkowski
# Project: Tracker generator
# Contact: bartoszszczepkowski99@gmail.com
#
# Copyright (c) 2025 Bartosz
#
# All rights reserved. Redistribution and modification of this
# code in any form is **not permitted** without explicit
# written permission from the author.
# -------------------------------------------------------------


import csv


file_content = []
headers = []

def get_loading_plan(path):
    _file_content = []
    with open(path, mode='r', newline='') as file:
        reader  = csv.reader(file)
        for row in reader:
            _file_content.append(row)
    
    return _file_content

def get_loading_plan_headers(content):
    for row in content:
        if (row[0] == "Vehicle No."):
            return row


file_content = get_loading_plan('load_plan.csv')
headers = get_loading_plan_headers(file_content)



def create_tracker_data():

    loads = {}

    for index, row in enumerate(file_content):
        if (row[get_loading_plan_headers(file_content).index('Customer Depot')] == "TOTAL"):
            pallet_number = row[get_loading_plan_headers(file_content).index('MORAN')]
            continue
        if (index < 3):
            continue
    
        
        load_number = row[get_loading_plan_headers(file_content).index('Vehicle No.')]
        load_name = row[get_loading_plan_headers(file_content).index('Customer Depot')]
        departure_time = row[get_loading_plan_headers(file_content).index('Time of Departure')]
        haulier = row[get_loading_plan_headers(file_content).index('Haulier')]

        if (load_number not in loads):
            loads[load_number] = {"depots": []}

        loads[f"{load_number}"]["departure_time"] = departure_time
        if (load_name not in loads[f"{load_number}"]["depots"]):
            loads[f"{load_number}"]["depots"].append(load_name)
        loads[f"{load_number}"]["haulier"] = haulier
        loads[f"{load_number}"]["pallet_number"] = pallet_number
        
        
    
    return loads


        
def create_csv_tracker(loads):
    lines = []
    for load in loads:
        
        depos = loads[load]["depots"]
        depos = ' / '.join(depos)

        load_number = load
        departure_time = loads[load]["departure_time"]
        haulier = loads[load]["haulier"]
        pallet_number = loads[load]["pallet_number"]

        file_line = f",{load_number}, {departure_time}, {depos}, {haulier},,,{pallet_number}\n"
        lines.append(file_line)

    with open('tracker.csv', 'w') as file:
        file.writelines(lines)
    


get_loading_plan('load_plan.csv')
get_loading_plan_headers(file_content)
create_csv_tracker(create_tracker_data())