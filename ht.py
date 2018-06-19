import ROOT
import numpy as np

import matplotlib

matplotlib.use('Agg') #look up what this means. Fixes 'no environment' error

import matplotlib.pyplot as plt

files = [
    ["nano_6.root","nano_6.root.friend"],
    ["nano_7.root","nano_7.root.friend"],
    ["nano_8.root","nano_8.root.friend"],
    ["nano_9.root","nano_9.root.friend"]
]

ptHist1 = ROOT.TH1F("Over4JetpTHist",";Jet pT (GeV?); Normalized events",20,0,2000)
#TH1F(name, xlabel,ylabel,bins,xmin,max)
ptHist2 = ROOT.TH1F("Over150nJets",";Number of jets; Normalised events",20,0,20)

chain = ROOT.TChain("Events") #Events is the tree of events
chainFriend = ROOT.TChain("Events")

for fileList in files:
    chain.Add(fileList[0])
    chainFriend.Add(fileList[1])

njcut = ROOT.TCut("nJet>0")
ptcut = ROOT.TCut("Jet_pt>150")

pchain = []
l = []

for event in chain:
    nJet = event.nJet
    #print nJet    
    
    for i in range(nJet):
        if event.Jet_pt[i]>150 and nJet > 0: 
            # = event.Jet_mass[i]
            l.append(event.Jet_pt[i])
    total = sum(l)
    
    pchain.append(total)
    l = []  
    

chain.AddFriend(chain)
'''
avg = np.mean(pchain)
var = np.var(pchain)
pdf_x = np.linspace(np.min(pchain),np.max(pchain),100)
pdf_y = 1.0/np.sqrt(2*np.pi*var)*np.exp(-0.5*(pdf_x-avg)**2/var)
'''

plt.hist(pchain, bins=40, normed = True)
plt.xlim(0,5000)
plt.xlabel("Ht of all jets (GeV)")
plt.ylabel("Number of events (normalised)")

#plt.plot(pdf_x,pdf_y,'k--')


plt.savefig("ht.png")



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
