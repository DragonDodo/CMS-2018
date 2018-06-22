import ROOT
import numpy as np

import matplotlib

matplotlib.use('Agg') #look up what this means. Fixes 'no environment' error

import matplotlib.pyplot as plt

massmin = 1900
massmax = 2100

fp001 = [
    ["ctp001a.root"],
    ["ctp001b.root"],
    ["ctp001c.root"],
    ["ctp001d.root"],
    ["ctp001e.root"],
    ["ctp001f.root"],
    ["ctp001g.root"]
]

fp01 = [
    ["ctp01a.root"],
    ["ctp01b.root"],
    ["ctp01c.root"],
    ["ctp01d.root"],
    ["ctp01e.root"],
    ["ctp01f.root"]
]

fp1 = [
    ["ctp1a.root"],
    ["ctp1b.root"],
    ["ctp1c.root"],
    ["ctp1d.root"],
    ["ctp1e.root"]
]

f1 = [
    ["ct1a.root"],
    ["ct1b.root"],
    ["ct1c.root"],
    ["ct1d.root"],
    ["ct1f.root"],
    ["ct1g.root"],
    ["ct1h.root"]
]

f10 = [
    ["ct10a.root"],
    ["ct10b.root"],
    ["ct10c.root"],
    ["ct10d.root"]
]

f100 = [
    ["ct100a.root"],
    ["ct100b.root"],
    ["ct100c.root"],
    ["ct100d.root"]
]


f1000 = [
    ["ct1000a.root"],
    ["ct1000b.root"],
    ["ct1000c.root"],
    ["ct1000d.root"]
]
        

f10000 = [
    ["ct10000a.root"],
    ["ct10000b.root"],
    ["ct10000c.root"],
    ["ct10000d.root"],
    ["ct10000e.root"],
    ["ct10000f.root"]
]

f100000 = [
    ["ct100000a.root"],
    ["ct100000b.root"],
    ["ct100000c.root"]
]


chain1 = ROOT.TChain("Events") #Events is the tree of events
chain2 = ROOT.TChain("Events") 
chain3 = ROOT.TChain("Events") 
chain4 = ROOT.TChain("Events") 
chain5 = ROOT.TChain("Events") 
chain6 = ROOT.TChain("Events") 
chain7 = ROOT.TChain("Events") 
chain8 = ROOT.TChain("Events") 
chain9 = ROOT.TChain("Events") 

for fileList in f10000:
    chain1.Add(fileList[0])
    
for fileList in f100000:
    chain2.Add(fileList[0])
    
for fileList in f1000:
    chain3.Add(fileList[0])
    
for fileList in f100:
    chain4.Add(fileList[0])
    
for fileList in f10:
    chain5.Add(fileList[0])
    
for fileList in f1:
    chain6.Add(fileList[0])

for fileList in fp1:
    chain7.Add(fileList[0])

for fileList in fp01:
    chain8.Add(fileList[0])
    
for fileList in fp001:
    chain9.Add(fileList[0])

pchain1 = []
pchain2 = []
pchain3 = []
pchain4 = []
pchain5 = []
pchain6 = []
pchain7 = []
pchain8 = []
pchain9 = []

l = []

for event in chain1:
    nJet = event.nJet
    #print nJet  
    Id = event.Jet_jetId     
    for i in range(nJet):
        if event.Jet_pt[i]>30 and nJet > 0 and abs(event.Jet_eta[i])<2.4 and Id>0: 
            # = event.Jet_mass[i]
            l.append(event.Jet_pt[i])
            
    total = sum(l)
    
    if len(event.llpinfo_llp_mass)>0:
        llpm = event.llpinfo_llp_mass[0]
    else:
        llpm = 0.0
    
        #print llpm[0]
        #pchain1.append(total)
    
    
    if llpm> massmin and llpm <massmax:
        pchain1.append(total)
        print "appended to 1"
    else:
        print "llpmass not in range: discarded (1)"
    l = []  
    
for event in chain2:
    nJet = event.nJet
    #print nJet  
    Id = event.Jet_jetId     
    for i in range(nJet):
        if event.Jet_pt[i]>30 and nJet > 0 and abs(event.Jet_eta[i])<2.4 and Id>0: 
            # = event.Jet_mass[i]
            l.append(event.Jet_pt[i])
            
    total = sum(l)
    
    if len(event.llpinfo_llp_mass)>0:
        llpm = event.llpinfo_llp_mass[0]
    else:
        llpm = 0.0
    
        #print llpm[0]
        #pchain1.append(total)
    
    
    if llpm> massmin and llpm <massmax:
        pchain2.append(total)
        print "appended to 2"
    else:
        print "llpmass not in range: discarded (2)"
    l = [] 
    
for event in chain3:
    nJet = event.nJet
    #print nJet  
    Id = event.Jet_jetId     
    for i in range(nJet):
        if event.Jet_pt[i]>30 and nJet > 0 and abs(event.Jet_eta[i])<2.4 and Id>0: 
            # = event.Jet_mass[i]
            l.append(event.Jet_pt[i])
            
    total = sum(l)
    
    if len(event.llpinfo_llp_mass)>0:
        llpm = event.llpinfo_llp_mass[0]
    else:
        llpm = 0.0
    
        #print llpm[0]
        #pchain1.append(total)
    
    
    if llpm> massmin and llpm <massmax:
        pchain3.append(total)
        print "appended to 3"
    else:
        print "llpmass not in range: discarded (3)"
    l = [] 
    
    
for event in chain4:
    nJet = event.nJet
    #print nJet  
    Id = event.Jet_jetId     
    for i in range(nJet):
        if event.Jet_pt[i]>30 and nJet > 0 and abs(event.Jet_eta[i])<2.4 and Id>0: 
            # = event.Jet_mass[i]
            l.append(event.Jet_pt[i])
            
    total = sum(l)
    
    if len(event.llpinfo_llp_mass)>0:
        llpm = event.llpinfo_llp_mass[0]
    else:
        llpm = 0.0
    
        #print llpm[0]
        #pchain1.append(total)
    
    
    if llpm> massmin and llpm <massmax:
        pchain4.append(total)
        print "appended to 4"
    else:
        print "llpmass not in range: discarded (4)"
    l = [] 
    
for event in chain5:
    nJet = event.nJet
    #print nJet  
    Id = event.Jet_jetId     
    for i in range(nJet):
        if event.Jet_pt[i]>30 and nJet > 0 and abs(event.Jet_eta[i])<2.4 and Id>0: 
            # = event.Jet_mass[i]
            l.append(event.Jet_pt[i])
            
    total = sum(l)
    
    if len(event.llpinfo_llp_mass)>0:
        llpm = event.llpinfo_llp_mass[0]
    else:
        llpm = 0.0
    
        #print llpm[0]
        #pchain1.append(total)
    
    
    if llpm> massmin and llpm <massmax:
        pchain5.append(total)
        print "appended to 5"
    else:
        print "llpmass not in range: discarded (5)"
    l = []  
    
for event in chain6:
    nJet = event.nJet
    #print nJet  
    Id = event.Jet_jetId     
    for i in range(nJet):
        if event.Jet_pt[i]>30 and nJet > 0 and abs(event.Jet_eta[i])<2.4 and Id>0: 
            # = event.Jet_mass[i]
            l.append(event.Jet_pt[i])
            
    total = sum(l)
    
    if len(event.llpinfo_llp_mass)>0:
        llpm = event.llpinfo_llp_mass[0]
    else:
        llpm = 0.0
    
        #print llpm[0]
        #pchain1.append(total)
    
    
    if llpm> massmin and llpm <massmax:
        pchain6.append(total)
        print "appended to 6"
    else:
        print "llpmass not in range: discarded (6)"
    l = []
    
for event in chain7:
    nJet = event.nJet
    #print nJet  
    Id = event.Jet_jetId     
    for i in range(nJet):
        if event.Jet_pt[i]>30 and nJet > 0 and abs(event.Jet_eta[i])<2.4 and Id>0: 
            # = event.Jet_mass[i]
            l.append(event.Jet_pt[i])
            
    total = sum(l)
    
    if len(event.llpinfo_llp_mass)>0:
        llpm = event.llpinfo_llp_mass[0]
    else:
        llpm = 0.0
    
        #print llpm[0]
        #pchain1.append(total)
    
    
    if llpm> massmin and llpm <massmax:
        pchain7.append(total)
        print "appended to 7"
    else:
        print "llpmass not in range: discarded (7)"
    l = []  

for event in chain8:
    nJet = event.nJet
    #print nJet  
    Id = event.Jet_jetId     
    for i in range(nJet):
        if event.Jet_pt[i]>30 and nJet > 0 and abs(event.Jet_eta[i])<2.4 and Id>0: 
            # = event.Jet_mass[i]
            l.append(event.Jet_pt[i])
            
    total = sum(l)
    
    if len(event.llpinfo_llp_mass)>0:
        llpm = event.llpinfo_llp_mass[0]
    else:
        llpm = 0.0
    
        #print llpm[0]
        #pchain1.append(total)
    
    
    if llpm> massmin and llpm <massmax:
        pchain8.append(total)
        print "appended to 8"
    else:
        print "llpmass not in range: discarded (8)"
    l = [] 

for event in chain9:
    nJet = event.nJet
    #print nJet  
    Id = event.Jet_jetId     
    for i in range(nJet):
        if event.Jet_pt[i]>30 and nJet > 0 and abs(event.Jet_eta[i])<2.4 and Id>0: 
            # = event.Jet_mass[i]
            l.append(event.Jet_pt[i])
            
    total = sum(l)
    
    if len(event.llpinfo_llp_mass)>0:
        llpm = event.llpinfo_llp_mass[0]
    else:
        llpm = 0.0
    
        #print llpm[0]
        #pchain1.append(total)
    
    
    if llpm> massmin and llpm <massmax:
        pchain9.append(total)
        print "appended to 9"
    else:
        print "llpmass not in range: discarded (9)"
    l = []       

fig, ax = plt.subplots()
ax.hist(pchain2, 40, normed = True, ec = 'red', histtype='step', label='100000')
ax.hist(pchain1, 40, normed = True, ec = 'orange', histtype='step', label='10000')
ax.hist(pchain3, 40, normed = True, ec = 'yellow', histtype='step', label='1000')
ax.hist(pchain4, 40, normed = True, ec = 'green', histtype='step', label='100')
ax.hist(pchain5, 40, normed = True, ec = 'blue', histtype='step', label='10')
ax.hist(pchain6, 40, normed = True, ec = 'midnightblue', histtype='step', label='1')
ax.hist(pchain7, 40, normed = True, ec = 'purple', histtype='step', label='0.1')
ax.hist(pchain8, 40, normed = True, ec = 'maroon', histtype='step', label='0.01')
ax.hist(pchain9, 40, normed = True, ec = 'gray',histtype='step', label='0.001')

ax.legend(title = "cTau [mm]", loc='upper right')
plt.xlim(0,5000)
plt.ylim(0,0.002)
plt.xlabel("Ht of all jets (GeV)")
plt.ylabel("Number of events (Normalised)")
plt.title("Dependence of Ht dist on ctau (Gluino mass: 2000 GeV/c^2)")




plt.savefig("ctau.png")


