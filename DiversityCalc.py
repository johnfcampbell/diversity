import csv
from DiversityWork import townCalc
from DiversityWork import countyCalc

county = countyCalc('all_050_in_34.P1.csv')
with open('all_060_in_34_combo.csv', 'r') as csvfile:
    thereader = csv.reader(csvfile)
    under = {}
    for line in thereader:
        if line[0] == 'GEOID':
            headingcount = 0
            print 'County,Town,Population,2010 Diversity Index,2000 Diversity Index,Points change'
            for cell in line:
                # print str(headingcount) + ',' + cell
                under[cell] = headingcount
                headingcount = headingcount + 1
        else:
            town = line[under['NAME']]
            totalPop = int(line[under['P003001']]) - int(line[under['P003007']])            
            #print town
            resultsLine = townCalc(line,under,county)
            print resultsLine
            # print town + ', Population ' + str(totalPop)


