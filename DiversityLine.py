def townCalc(line, under):

    # if 2000 comparison figures are blank, we skip it.
    # Caldwell, this means you.

    if (line[under['P003001.2000']] == ''):
        return ''
    town=line[under['NAME']]
    county=line[under['COUNTY']]
    totalPop = int(line[under['P003001']]) - int(line[under['P003007']])            
    if (totalPop == 0):
        return ''
    totalPop2000 = int(line[under['P003001.2000']]) - int(line[under['P003007.2000']])            

    totalWhite = int(line[under['P003002']])            
    totalBlack = int(line[under['P003003']])            
    totalAmericanIndian = int(line[under['P003004']])            
    totalAsian = int(line[under['P003005']])            
    totalPacific = int(line[under['P003006']])            

    totalWhite2000 = int(line[under['P003002.2000']])            
    totalBlack2000 = int(line[under['P003003.2000']])            
    totalAmericanIndian2000 = int(line[under['P003004.2000']])            
    totalAsian2000 = int(line[under['P003005.2000']])            
    totalPacific2000 = int(line[under['P003006.2000']])            

    sameWhite = (float(totalWhite)/totalPop) ** 2
    sameBlack = (float(totalBlack)/totalPop) ** 2
    sameAmericanIndian = (float(totalAmericanIndian)/totalPop) ** 2
    sameAsian = (float(totalAsian)/totalPop) ** 2
    samePacific = (float(totalPacific)/totalPop) ** 2
    sameRace = sameWhite + sameBlack + sameAmericanIndian
    sameRace = sameRace + sameAsian + samePacific

    sameWhite2000 = (float(totalWhite2000)/totalPop2000) ** 2
    sameBlack2000 = (float(totalBlack2000)/totalPop2000) ** 2
    sameAmericanIndian2000 = (float(totalAmericanIndian2000)/totalPop2000) ** 2
    sameAsian2000 = (float(totalAsian2000)/totalPop2000) ** 2
    samePacific2000 = (float(totalPacific2000)/totalPop2000) ** 2
    sameRace2000 = sameWhite2000 + sameBlack2000 + sameAmericanIndian2000
    sameRace2000 = sameRace2000 + sameAsian2000 + samePacific2000

    totalHispanicOrNot = int(line[under['P004001']])
    totalHispanic = int(line[under['P004002']])
    totalNotHispanic = int(line[under['P004003']])

    totalHispanicOrNot2000 = int(line[under['P004001.2000']])
    totalHispanic2000 = int(line[under['P004002.2000']])
    totalNotHispanic2000 = int(line[under['P004003.2000']])

    sameHispanic = (float(totalHispanic)/totalHispanicOrNot) ** 2
    sameNonHispanic = (float(totalNotHispanic)/totalHispanicOrNot) ** 2
    sameEthnicity = sameHispanic + sameNonHispanic

    sameHispanic2000 = (float(totalHispanic2000)/totalHispanicOrNot2000) ** 2
    sameNonHispanic2000 = (float(totalNotHispanic2000)/totalHispanicOrNot2000) ** 2
    sameEthnicity2000 = sameHispanic2000 + sameNonHispanic2000

    sameBoth = sameRace * sameEthnicity
    sameBoth2000 = sameRace2000 * sameEthnicity2000

    diversityIndexFloat = 1 - sameBoth
    diversityIndex2000Float = 1 - sameBoth2000

    diversityIndexPct = int((diversityIndexFloat + 0.005)*100)
    diversityIndex2000Pct = int((diversityIndex2000Float + 0.005)*100)
    DIP = diversityIndexPct
    DIP2k = diversityIndex2000Pct
    DIPdelta = DIP - DIP2k
    

    print county + ' ' + town + ', Population ' + str(totalPop) + ' ' + str(DIP) + ' ' + str(DIP2k) + ' ' + str(DIPdelta)

    return ''
