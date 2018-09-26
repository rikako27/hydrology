import urllib.request
import urllib.error
import csv
import math
import sys
from tabulate import tabulate

url = " http://rapid-hub.org/data/angles_UCI_CS.csv"
savefile = "angles_UCI_CS.csv"


def resultList(filename):
#return the list of ordered dicts 
#whose keys are "station_id", "angle_degrees", and "cosine"
    l = []
    with open(filename) as csv_file:
        l = list(csv.DictReader(csv_file, skipinitialspace=True))

    for i in l:
        i.update({'cosine': math.cos(math.radians(eval(i['angle_degrees'])))})
#     print(l)
    return l

def formattedTable(d):
#create formatted table for the result
    header = d[0].keys()
    row = [ i.values() for i in d ]
    return tabulate(row, header)
    
    
if __name__ == '__main__':
    try:
        #fetching URLs
        res = urllib.request.urlopen(url)
        data = res.read()

        #write the data to "output.csv"
        with open(savefile, mode='wb') as f:
            f.write(data)
        
#         print(data)
        
        result = resultList(savefile)
        print(formattedTable(result))
        
    except urllib.error.URLError as e:
        print(e.reason)
        sys.exit()
        
