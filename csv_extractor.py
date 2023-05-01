import csv
import glob

def write_csv_data(infile, outfile):
    with open(infile) as csvfile:
        rdr = list(csv.reader(csvfile))[109:]
    with open(outfile, 'w+') as csvfile:
        wtr = csv.writer(csvfile, delimiter=' ')
        wtr.writerows(rdr)
    return

for file in glob.glob('*MOSFET*.csv'):
    write_csv_data(file, file + '_out.txt')
