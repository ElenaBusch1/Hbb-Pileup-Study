######################################################
#   Pass a tree of events, return a tree of jets     #
#   labeled as sig or bkd by number of b's matched   #
######################################################

import ROOT 
#import my_variableDictionary as vd
from io import StringIO 
import os
from optparse import OptionParser, OptionGroup
from array import array
from ROOT import TTree, TChain

ROOT.gROOT.ProcessLine(".L Loader.C+")
#ROOT.gROOT.Macro("$ROOTCOREDIR/scripts/load_packages.C")
#def addMCinfo()
def in_list(item,L):
        for i in L:
             if item in i:
               return L.index(i)


def cutTree(jetTree ):
            print jetTree.GetEntries()
            jetTree=jetTree.CopyTree("jet_pt>250e3&&jet_nBHadr<=2&&jet_nCHadr<=2&&jet_pt<2000e3&&abs(jet_eta)<2&&(jet_m<1.46e5&&jet_m>7.6e4)")
            print jetTree.GetEntries()
            return jetTree
        
    #     tracksFromJet = eventTree.ljet_JetTrackVariables_parentJet_nTracks


if __name__ == '__main__':
        usage = "usage: %prog [options]"
        parser = OptionParser(usage=usage)

        parser.add_option("--filename", dest="filename", default = '', help="path + name of root file")
        parser.add_option("--saveAs", dest="saveAs", default = '', help="path + name of root file")


        (options, args) = parser.parse_args()

        eventTree=ROOT.TChain("jetTree")
       # eventTree.Add(filenames)
        files= options.filename.split(',')
        ROOT.gROOT.cd()
        for file in files:
           print file
           eventTree.AddFile(file)



        newFile   = ROOT.TFile.Open(file+"_cut.root", 'recreate')
        jetTree   = cutTree(eventTree) 
        newFile.Write()
        newFile.Close()


