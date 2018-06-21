import ROOT
import numpy as np

import matplotlib

matplotlib.use('Agg') #look up what this means. Fixes 'no environment' error

import matplotlib.pyplot as plt

files = [
    ["nano_3.root"],
    ["nano_4.root"],
    ["nano_5.root"],
    ["nano_6.root"],
    ["nano_7.root"],
    ["nano_8.root"],
    ["nano_9.root"]
]

ptHist1 = ROOT.TH1F("Over4JetpTHist",";Jet pT (GeV?); Normalized events",20,0,2000)
#TH1F(name, xlabel,ylabel,bins,xmin,max)
ptHist2 = ROOT.TH1F("Over150nJets",";Number of jets; Normalised events",20,0,20)

chain = ROOT.TChain("Events") #Events is the tree of events
#chainFriend = ROOT.TChain("Events")

for fileList in files:
    chain.Add(fileList[0])
    #chainFriend.Add(fileList[1])

njcut = ROOT.TCut("nJet>0")
ptcut = ROOT.TCut("Jet_pt>150")

pchain1 = []
pchain2 = []
pchain3 = []
pchain4 = []
pchain5 = []
pchain6 = []
pchain7 = []
pchain8 = []
pchain9 = []
pchain10 = []

l = []

for event in chain:
    nJet = event.nJet
    #print nJet  
    Id = event.Jet_jetId 

    
    for i in range(nJet):
        if event.Jet_pt[i]>30 and nJet > 0 and abs(event.Jet_eta[i])<2.4: 
            # = event.Jet_mass[i]
            l.append(event.Jet_pt[i])
            
    total = sum(l)
    
    if len(event.llpinfo_llp_mass)>0:
        llpm = event.llpinfo_llp_mass[0]
    else:
        llpm = 0.0
    
        #print llpm[0]
        #pchain1.append(total)
    
    
    if llpm> 500 and llpm <700:
        pchain1.append(total)
        print "appended to 1"
    elif llpm >700 and llpm<900:
        pchain2.append(total)
        print "appended to 2"
    elif llpm >900 and llpm <1100:
        pchain3.append(total)
        print "appended to 3"
    elif llpm>1100 and llpm <1300:
        pchain4.append(total)
        print "appended to 4"
    elif llpm>1300 and llpm<1500:
        pchain5.append(total)
        print "appended to 5"
    elif llpm>1500 and llpm<1700:
        pchain6.append(total)
        print "appended to 6"
    elif llpm>1700 and llpm<1900:
        pchain7.append(total)
        print "appended to 7"
    elif llpm>1900 and llpm<2100:
        pchain8.append(total)
        print "appended to 8"
    elif llpm>2100 and llpm<2300:
        pchain9.append(total)
        print "appended to 9"
    elif llpm>2300 and llpm<2500:
        pchain10.append(total)  
        print "appended to 10"
    else:
        print "no LLP"
    l = []  
    

#chain.AddFriend(chain)

#plt.hist(pchain1, bins=40, normed = True, histtype='step')
fig, ax = plt.subplots()
ax.hist(pchain1, 40, ec = 'red', histtype='step', label='600')
ax.hist(pchain2, 40, ec = 'orange', histtype='step', label='800')
ax.hist(pchain3, 40, ec = 'yellow', histtype='step', label='1000')
ax.hist(pchain4, 40, ec = 'green', histtype='step', label='1200')
ax.hist(pchain5, 40, ec = 'blue', histtype='step', label='1400')
ax.hist(pchain6, 40, ec = 'midnightblue', histtype='step', label='1600')
ax.hist(pchain7, 40, ec = 'purple', histtype='step', label='1800')
ax.hist(pchain8, 40, ec = 'maroon', histtype='step', label='2000')
ax.hist(pchain9, 40, ec = 'gray',histtype='step', label='2200')
ax.hist(pchain10, 40, ec = 'black',histtype='step', label='2400')
ax.legend(title = "Gluino mass (GeV/c^2)", loc='upper right')
plt.xlim(0,5000)
plt.xlabel("Ht of all jets (GeV)")
plt.ylabel("Number of events")
plt.title("Dependence of Ht dist on gluino mass (ctau 0.001mm) (NoJetId)")

#plt.plot(pdf_x,pdf_y,'k--')


plt.savefig("htllplt0p001n.png")



#chain.Project(ptHist1.GetName(),"abs(Jet_pt[0])","(nJet>=4)")
#chain.Project(ptHist2.GetName(),"nJet[0]", str(ptcut))
#TTree.Project: (name, data, cut)
#ptHist1.Scale(1./ptHist1.Integral()) #normalisation
#ptHist2.Scale(1./ptHist2.Integral())
#cv1 = ROOT.TCanvas("cv1","",800,600) #create canvas
#ptHist1.Draw("HIST") 
#cv1.Update()
#cv1.Print("jetpt.pdf")

#cv2 = ROOT.TCanvas("cv2","",800,600)
#ptHist2.Draw("HIST")
#cv2.Update()
#cv2.Print("njet150.pdf")
#cv.WaitPrimitive()
