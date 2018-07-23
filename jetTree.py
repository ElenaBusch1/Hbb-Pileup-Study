import ROOT 
import my_variableDictionary as vd
#import new_val as vd
from io import StringIO 
import os, sys, resource
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


def createJetTree(eventTree0, list_xsec, isSignal, isCut=False, isSpecify=True):

    #with open('XSection.txt', 'r') as myfile: data=myfile.read().replace('\n', '')
    

    jetTree = ROOT.TTree("jetTree","tree of jets")
    jetTree.SetDirectory(0)

    getVar       = vd.getVariables()
    varDictInt   = getVar.getVariableDict('int')
    varDictIntSub = getVar.getVariableDict('intsub')
    varDictFloat = getVar.getVariableDict('float')
    varDictFloatSub = getVar.getVariableDict('floatsub')
    for varName in varDictFloat:
           jetTree.Branch(varName, varDictFloat[varName], varName + "/F")
    for varName in varDictInt:
           jetTree.Branch(varName, varDictInt[varName], varName + "/I")
    for varName in varDictIntSub:
           jetTree.Branch(varName, varDictIntSub[varName], varName + "/I")
    for varName in varDictFloatSub:
           jetTree.Branch(varName, varDictFloatSub[varName], varName + "/F")
    nevents =array('i',[0])
    selected_nevents =array('i',[0])
    Filter =array('f',[0])
    xsec =array('f',[0])
    jetTree.Branch("Events",nevents,"nevents/I");  
    jetTree.Branch("Cross_Section",xsec,"Xsec/F");  
    jetTree.Branch("Filter_ef",Filter,"Filter_ef/F");  
    jetTree.Branch("SelectedEvents",selected_nevents,"selected_nevents/I");  
    label =array('i',[0])
    cl=jetTree.Branch("Class_label",label,"label/I");  
    print "Creating Jet tree..."
 #   eventTree=eventTree0.CopyTree("jet_pt>250e3&&jet_nBHadr<=2&&jet_nCHadr<=2&&jet_pt<2000e3&&abs(jet_eta)<2&&(jet_m<1.46e5&&jet_m>7.6e4)")
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  
    print "Memory usage is: {0} KB".format(mem)   
    
    for i in xrange(eventTree.GetEntries()):
    #for i in range(100):
        eventTree.GetEntry(i)
        selected_nevents[0]=1

        if(i%100==0): print "%i/%i"%(i,eventTree.GetEntries())
        row=in_list( eventTree.mcchan, list_xsec)
        Filter[0]=list_xsec[row][3]
        xsec[0]=list_xsec[row][1]
        nevents[0]=list_xsec[row][4]

        for jet in xrange(len(eventTree.jet_2Exkt_pt)):
            for varName in varDictIntSub:
                if "2Exkt" in varName:
		    if "_Lead" in varName:
                        if(len(eventTree.__getattr__(varName.replace("_Lead", ""))[jet])!=2):
                       	    break
                        varDictIntSub[varName][0]   = eventTree.__getattr__(varName.replace("_Lead", ""))[jet][0]     #var[jet][i]
                    elif "_SubLead" in varName:
                        if(len(eventTree.__getattr__(varName.replace("_SubLead", ""))[jet])!=2):
                   	    break
                        varDictIntSub[varName][0]   = eventTree.__getattr__(varName.replace("_SubLead", ""))[jet][1]     #var[jet][i]
            	elif "3Exkt" in varName:
                    if "_Lead" in varName:
                        if(len(eventTree.__getattr__(varName.replace("_Lead", ""))[jet])!=3):
                            break
                        varDictIntSub[varName][0]   = eventTree.__getattr__(varName.replace("_Lead", ""))[jet][0]     #var[jet][i]
                    elif "_SubLead" in varName:
                        if(len(eventTree.__getattr__(varName.replace("_SubLead", ""))[jet])!=3):
                            break
                        varDictIntSub[varName][0]   = eventTree.__getattr__(varName.replace("_SubLead", ""))[jet][1]     #var[jet][i]
                    elif "_SubSubLead" in varName:
                        if(len(eventTree.__getattr__(varName.replace("_SubSubLead", ""))[jet])!=3):
                            break
                        varDictIntSub[varName][0]   = eventTree.__getattr__(varName.replace("_SubSubLead", ""))[jet][2]
	    
            for varName in varDictInt:
               if "jet" in varName:   
                   varDictInt[varName][0] = eventTree.__getattr__(varName)[jet]
               else:
                   #print varName
                   varDictInt[varName][0] =eventTree.__getattr__(varName)
           # print  varDictFloatSub

            for varName in varDictFloatSub:
                if "2Exkt" in varName:
                    if "_Lead" in varName:
                        if(len(eventTree.__getattr__(varName.replace("_Lead", ""))[jet])!=2):
                            break
                        varDictIntSub[varName][0]   = eventTree.__getattr__(varName.replace("_Lead", ""))[jet][0]     #var[jet][i]
                    elif "_SubLead" in varName:
                        if(len(eventTree.__getattr__(varName.replace("_SubLead", ""))[jet])!=2):
                            break
                        varDictIntSub[varName][0]   = eventTree.__getattr__(varName.replace("_SubLead", ""))[jet][1]     #var[jet][i]
                elif "3Exkt" in varName:
                    if "_Lead" in varName:
                        if(len(eventTree.__getattr__(varName.replace("_Lead", ""))[jet])!=3):
                            break
                        varDictIntSub[varName][0]   = eventTree.__getattr__(varName.replace("_Lead", ""))[jet][0]     #var[jet][i]
                    elif "_SubLead" in varName:
                        if(len(eventTree.__getattr__(varName.replace("_SubLead", ""))[jet])!=3):
                            break
                        varDictIntSub[varName][0]   = eventTree.__getattr__(varName.replace("_SubLead", ""))[jet][1]     #var[jet][i]
                    elif "_SubSubLead" in varName:
                        if(len(eventTree.__getattr__(varName.replace("_SubSubLead", ""))[jet])!=3):
                            break
                        varDictIntSub[varName][0]   = eventTree.__getattr__(varName.replace("_SubSubLead", ""))[jet][2]  


             for varName in varDictFloat:
               if "jet" in varName:
                   #print varName,  eventTree.__getattr__(varName)[jet]   
                   varDictFloat[varName][0]   = eventTree.__getattr__(varName)[jet]
               else:
                  # print varName,  eventTree.__getattr__(varName) 
                   varDictFloat[varName][0]   = eventTree.__getattr__(varName)

            if(isSpecify=="1"):
                if(isSignal=="1"):   
                   # print jetTree.jet_nGhostHBoso, jetTree.jet_nBHadr
                  #  print "!!!"
                   # if jetTree.jet_nGhostHBoso!=0 and jetTree.jet_nBHadr!=0:
                   #    print jetTree.jet_nGhostHBoso, jetTree.jet_nBHadr
            #if(subclass=='bb'):
                    if (jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr ==2 ):
                       label[0]=1
            #if(subclass=='bl'):
                    if( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==1 and  jetTree.jet_nCHadr<=1):
                       label[0]=2
            #if(subclass=='bc'):
                    if( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==1 and  jetTree.jet_nCHadr==2):
                       label[0]=3
            #if(subclass=='cc'):
                    if( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==0 and  jetTree.jet_nCHadr==2):
                       label[0]=4
            #if(subclass=='ll'):
                    if( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==0 and  jetTree.jet_nCHadr==0):
                       label[0]=5
            #if(subclass=='cl'):
                    if( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==0 and  jetTree.jet_nCHadr==1):
                       label[0]=6
                else:
                    if( jetTree.jet_nBHadr  ==2 ):
                       label[0]=1
                    if( jetTree.jet_nBHadr  ==1 and  jetTree.jet_nCHadr<=1):
                       label[0]=2
                    if( jetTree.jet_nBHadr  ==1 and  jetTree.jet_nCHadr==2):
                       label[0]=3
                    if( jetTree.jet_nBHadr  ==0 and  jetTree.jet_nCHadr==2):
                       label[0]=4
                    if( jetTree.jet_nBHadr  ==0 and  jetTree.jet_nCHadr==0):
                       label[0]=5
                    if( jetTree.jet_nBHadr  ==0 and  jetTree.jet_nCHadr==1):
                       label[0]=6

            else:
                if(isSignal=="1"):
                    if( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==2):
                       label[0]=10
                    elif( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==1):
                       label[0]=11
                    elif( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==0):
                       label[0]=12
                if(isSignal=="0"):
                    if( jetTree.jet_nBHadr  ==2):
                       label[0]=10
                    elif( jetTree.jet_nBHadr  ==1):
                       label[0]=11
                    elif( jetTree.jet_nBHadr  ==0):
                       label[0]=12
           # print label[0]
            if(label[0]<1 or label[0]>12):
                label[0]=0
            cl.Fill()      
            jetTree.Fill()

    jetTree=jetTree.CopyTree("jet_pt>250e3&&jet_nBHadr<=2&&jet_nCHadr<=2&&jet_pt<2000e3&&abs(jet_eta)<2&&(jet_m<1.46e5&&jet_m>7.6e4)")
    jetTree.Write()
            
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  
    print "Memory usage is: {0} KB".format(mem)   

  #  jetTree_out  = classify_lable(jetTree, isSignal, isCut, isSpecify) 
    del varDictFloatSub, varDictFloat, varDictInt, varDictIntSub

   # return jetTree_out

    return jetTree


def classify_lable(jetTree, isSignal =True, isCut=False, isSpecify=True ):
            if(isCut):
              jetTree=jetTree.CopyTree("jet_pt>250e3&&jet_nBHadr<=2&&jet_nCHadr<=2&&jet_pt<2000e3&&abs(jet_eta)<2&&(jet_m<1.46e5&&jet_m>7.6e4)")
            

            label =array('i',[0])
            cl=jetTree.Branch("Class_label",label,"label/I");  

            for i in xrange(jetTree.GetEntries()):

              jetTree.GetEntry(i)
              
              if(isSpecify=="1"):
                if(isSignal=="1"):   
                  #  print "!!!"
                 #   if jetTree.jet_nGhostHBoso!=0 and jet_nBHadr !=0:
                    #  print jetTree.jet_nGhostHBoso, jetTree.jet_nBHadr
            #if(subclass=='bb'):
                    if (jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr ==2 ):
                     #  print "!!!"
                       label[0]=1
                  #     print "0"
                       #jetTree.Fill()
            #if(subclass=='bl'):
                    if( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==1 and  jetTree.jet_nCHadr<=1):
                     #  print jetTree.jet_nBHadr, jetTree.jet_nCHadr 
                   #    print "1"
                       label[0]=2
                       #jetTree.Fill()
            #if(subclass=='bc'):
                    if( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==1 and  jetTree.jet_nCHadr==2):
                       label[0]=3
                     #  print "2"
                       #jetTree.Fill()
            #if(subclass=='cc'):
                    if( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==0 and  jetTree.jet_nCHadr==2):
                       label[0]=4
                    #   print "3"
                       #jetTree.Fill()
            #if(subclass=='ll'):
                    if( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==0 and  jetTree.jet_nCHadr==0):
                       label[0]=5
                    #   print "4"
                       #jetTree.Fill()
            #if(subclass=='cl'):
                    if( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==0 and  jetTree.jet_nCHadr==1):
                       label[0]=6
                       #jetTree.Fill()
                elif(isSignal=="0"):
                    if( jetTree.jet_nBHadr  ==2 ):
                       label[0]=1
                       #jetTree.Fill()
                    if( jetTree.jet_nBHadr  ==1 and  jetTree.jet_nCHadr<=1):
                       label[0]=2
                       #jetTree.Fill()
                    if( jetTree.jet_nBHadr  ==1 and  jetTree.jet_nCHadr==2):
                       label[0]=3
                       #jetTree.Fill()
                    if( jetTree.jet_nBHadr  ==0 and  jetTree.jet_nCHadr==2):
                       label[0]=4
                       #jetTree.Fill()
                    if( jetTree.jet_nBHadr  ==0 and  jetTree.jet_nCHadr==0):
                       label[0]=5
                       #jetTree.Fill()
                    if( jetTree.jet_nBHadr  ==0 and  jetTree.jet_nCHadr==1):
                       label[0]=6

              else:
                if(isSignal=="1"):
            #if(subclass=='2b'):
                    if( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==2):
                       label[0]=10
            #if(subclass=='1b'):
                    elif( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==1):
                       label[0]=11
            #if(subclass=='0b'):
                    elif( jetTree.jet_nGhostHBoso ==1 and jetTree.jet_nBHadr  ==0):
                       label[0]=12
                
                if(isSignal=="0"):
                    if( jetTree.jet_nBHadr  ==2):
                       label[0]=10
                    elif( jetTree.jet_nBHadr  ==1):
                       label[0]=11
                    elif( jetTree.jet_nBHadr  ==0):
                       label[0]=12
              if(label[0]<1 or label[0]>12):
                label[0]=0
                   
              cl.Fill()

            return jetTree
        


if __name__ == '__main__':
        usage = "usage: %prog [options]"
        parser = OptionParser(usage=usage)

        parser.add_option("--filename", dest="filename", default = '', help="path + name of root file")
        parser.add_option("--saveAs", dest="saveAs", default = '', help="path + name of root file")
        parser.add_option("--num", dest="num_hadron", default = '', help="path + name of root file")
        parser.add_option("--sig", dest="signal", default = '', help="path + name of root file")
        parser.add_option("--specify", dest="specify", default = '', help="path + name of root file")


        (options, args) = parser.parse_args()


        list_of_lists = []
        with open('XSection.txt') as XS_FILE:
            for line in XS_FILE:
                        if "#" in line: continue
                        inner_list = [elt.strip() for elt in line.split(' ')]
                        inner_list[0]=int(inner_list[0])
                        inner_list[1]=float(inner_list[1])
                        inner_list[4]=int(inner_list[4])
                        inner_list[3]=float(inner_list[3])
  
                        list_of_lists.append(inner_list)


        XS_FILE.close()
        filenames  = options.filename.split(",")
        
        saveAs    = "test"
        saveAs    = options.saveAs
        
        if(options.specify):
           saveAs=saveAs+"_specified"

        eventTree=ROOT.TChain("bTag_AntiKt10LCTopoTrimmedPtFrac5SmallR20Jets")

        ROOT.gROOT.cd()
        for file in filenames:
           eventTree.AddFile(file)


       # file.close()
        newFile   = ROOT.TFile.Open("out1"+".root", 'recreate')

        jetTree   = createJetTree(eventTree, list_of_lists, options.signal , True, options.specify) 
      #  newFile.Write()

        ROOT.gDirectory.Delete("bTag_AntiKt10LCTopoTrimmedPtFrac5SmallR20Jets")    

        newFile.Close()
        sys.exit(0)

