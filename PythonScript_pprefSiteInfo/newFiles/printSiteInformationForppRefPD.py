#!/usr/bin/env python
#
# modified Script to print information about the pp Reference Run PDs in DAS in table format
#
 
from datetime import datetime
import os
from prettytable import PrettyTable
from prettytable import ALL

#Dir = "/afs/cern.ch/user/h/honi/CMSSW_7_5_5_patch3/src/PythonScript_pprefSiteInfo"
Dir = "."

breakDebug = False  # will process only the first PD
break2Debug = False  # will process only the first and second PDs

pdNames = ["MinimumBias1"]
pdNames.append("MinimumBias16")
pdNames.append("ppForward")
pdNames.append("HighMultiplicity")
pdNames.append("FullTrack")
pdNames.append("BTagCSV")
pdNames.append("HeavyFlavor")
pdNames.append("HighPtPhoton30AndZ")
pdNames.append("HighPtLowerPhotons")
pdNames.append("JetHT")
pdNames.append("HighPtJet80")
pdNames.append("HighPtLowerJets")
pdNames.append("DoubleMu")
pdNames.append("MuPlusX")
pdNames.append("SingleMuHighPt")
pdNames.append("SingleMuLowPt")

pdNum = len(pdNames)
x = PrettyTable(["PD Names","Site, Dataset Presense"])
x.align = "c"
x.valign = "m"
x.hrules = ALL
x.padding_width = 1

countPDs = 0
for pdName in pdNames:
    countPDs += 1
    print "Processing for PD", pdName
    dasAODPathName = '/' + pdName + '/Run2015E-PromptReco-v1/AOD'

    findSitesAODCommand = Dir + '/das.py --limit=1000 --format=plain --query="site dataset=' + dasAODPathName + ' | grep site.name,site.dataset_fraction" > tmp.txt ; tail -n +4 tmp.txt > sites.txt'
    os.system(findSitesAODCommand)

    fileInput = open('sites.txt', 'r')
    SiteNames = []
    for line in fileInput:
        tmpname = line.rstrip('\n')
        SiteNames.append(tmpname)

    for SiteName in SiteNames:
        if SiteName.find('Buffer') > 0:
            SiteNames.remove(SiteName)
        if SiteName.find('MSS') > 0 :
            SiteNames.remove(SiteName)
         
    SiteForThisPD = '\n'.join(SiteNames)

#    print SiteForThisPD 
    
    fileInput.close()
 
    x.add_row([pdName,SiteForThisPD])

    if(breakDebug):
         break   # break out of PD names loop after only one file
    if(break2Debug and countPDs == 2):
         break   # break out of PD names loop after two files
print x

exit()
