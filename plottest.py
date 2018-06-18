import ROOT
import numpy

files = [
    ["nano_6.root","nano_6.root.friend"],
    ["nano_7.root","nano_7.root.friend"],
    ["nano_8.root","nano_8.root.friend"],
    ["nano_9.root","nano_9.root.friend"]
]

ptHist = ROOT.TH1F("nJetHist",";Number of Jets; Normalized events",20,0,21)
#TH1F(name, xlabel,ylabel,bins,xmin,max?)

chain = ROOT.TChain("Events") #Events is the tree of events
chainFriend = ROOT.TChain("Events")

for fileList in files:
    chain.Add(fileList[0])
    chainFriend.Add(fileList[1])
    
chain.AddFriend(chain)
chain.Project(ptHist.GetName(),"nJet[0]","(nJet>0)")
ptHist.Scale(1./ptHist.Integral())
cv = ROOT.TCanvas("cv","",800,600)
ptHist.Draw("HIST")
cv.Update()
cv.Print("njet.pdf")
#cv.WaitPrimitive()
