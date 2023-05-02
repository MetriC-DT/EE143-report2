import csv
import glob

def write_csv_data(infile, outfile):
    with open(infile) as csvfile:
        rdr = list(csv.reader(csvfile))[104:]
    with open(outfile, 'w+') as csvfile:
        wtr = csv.writer(csvfile, delimiter=' ')
        wtr.writerows(rdr)
    return

for file in glob.glob('*.csv'):
    write_csv_data(file, file[:-4] + '_out.txt')
