#import pandas as pd
#data = pd.read_cvs("housing.csv")
#data
import datatable
import time

start = time.time()
os_scan_data = datatable.fread("housing.csv")
end = time.time()

print(end - start)

print(os_scan_data)
