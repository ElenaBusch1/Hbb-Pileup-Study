#include <iostream>
#include <iomanip>
using namespace std;
#include "TFile.h"
#include "TTree.h"
#include "TH1.h"
#include "TH2.h"
#include "TF1.h"
#include "TAttFill.h"
#include "TCanvas.h"
#include <vector>
#include "stdio.h"
#include <stdlib.h>
#include "math.h"
#include "TMath.h"
#include "TGraph.h"
#include "TLegend.h"
#include "TPaveStats.h"
#include "TStyle.h"
#include "THStack.h"
#include "TFitResultPtr.h"
#include <fstream>

void plots()
{
	//Enter filenames
	//Make sure file1 is low pileup and file2 is high pileup, or change the legend
	TString fileName1="/afs/cern.ch/user/e/ebusch/ATLAS/data/user.ebusch.mc16_13TeV.301491.MadPty8E_A14NNPDF23LO_RSGhh_bbbb_c10_M600.DAOD...jb_0625_5_out1.root/user.ebusch.14491605._000001.out1.root";
	TString fileName2="/afs/cern.ch/user/e/ebusch/ATLAS/data/user.evillhau.mc16_13TeV.301491.MadPty8E_A14NNPDF23LO_RSGhh_bbbb_c10_M600.DAOD..64b1b3a_Akt10LCTopoTrmJets.jetbased_9_out1.root/user.evillhau.14494813._000001.out1.root";
	
	//Specify tree within file
	TString treeName1="jetTree";
	TString treeName2="jetTree";



	//--------------Open first file------------------//
	cout << "Opening "<< fileName1 << endl;
	TFile* myFile1 = new TFile(fileName1);
	TTree* myTree1 = (TTree*) myFile1->Get(treeName1);

	//Initialize variables. Make sure type is correct
	//If you need to check the type, open the root file and execute tree->Print() to see all branches
	Int_t nvtx1;
	Float_t actmu1;	
	Float_t avgmu1;
	Float_t jetpt1;
	
	//Give your local variable as the address for the branch
	//myTree1->SetBranchAddress("nvtx",&nvtx1);
	//myTree1->SetBranchAddress("actmu",&actmu1);
	//myTree1->SetBranchAddress("avgmu",&avgmu1);
	myTree1->SetBranchAddress("jet_pt",&jetpt1);

	Long64_t numEvents1 = myTree1->GetEntries();

	//Initialize canvas and histograms. Histogram range must be adjusted for data
        //TCanvas *c1 = new TCanvas("c","c",600,400);
	//TH1F *hist1 = new TH1F("hist1","nvtx",100,0,50);
	//TH1F *hist1 = new TH1F("hist1","actmu",90,0,90);
        //TH1F *hist1 = new TH1F("hist1","avgmu",90,0,90);	
        TH1F *hist1 = new TH1F("hist1","jetpt",200,0,1000000);

	//Add entries to first histogram
	for(Long64_t iEntry1 = 0; iEntry1 <numEvents1; iEntry1++){
		myTree1->GetEntry(iEntry1);
		hist1->Fill(jetpt1);
	}



	//-------------Open second file-----------------//	
	cout << "Opening "<< fileName2 << endl;
	TFile* myFile2 = new TFile(fileName2);
	TTree* myTree2 = (TTree*) myFile2->Get(treeName2);	
	
	//Initialize new variables
	Int_t nvtx2;
	Float_t actmu2;
	Float_t avgmu2;
	Float_t jetpt2;
	
	//myTree2->SetBranchAddress("nvtx",&nvtx2);
	//myTree2->SetBranchAddress("actmu",&actmu2);
	//myTree2->SetBranchAddress("avgmu",&avgmu2);
	myTree2->SetBranchAddress("jet_pt",&jetpt2);	

	Long64_t numEvents2 = myTree2->GetEntries();
	//TH1F *hist2 = new TH1F("hist2","nvtx2",100,0,50);
	//TH1F *hist2 = new TH1F("hist2","actmu2",90,0,90);	
	//TH1F *hist2 = new TH1F("hist2","avgmu2",90,0,90);
	TH1F *hist2 = new TH1F("hist2","Fatjet pt",200,0,1000000);

	for(Long64_t iEntry2 = 0; iEntry2 <numEvents2; iEntry2++){
                myTree2->GetEntry(iEntry2);
		hist2->Fill(jetpt2);
	}



	//----------------Make Plots-------------------//
	cout << "Making plots" << endl;
	//Turn off statistics boxes
	hist1->SetStats(0);
	hist2->SetStats(0);
	hist1->SetLineColor(kBlue);
	hist2->SetLineColor(kRed);
	hist1->GetXaxis()->SetTitle("jetpt");
 	hist2->GetXaxis()->SetTitle("jetpt");
	hist1->GetYaxis()->SetTitle("A.U.");
	hist2->GetYaxis()->SetTitle("A.U.");
	
	//Normalize histograms
	Double_t norm = 1;
	Double_t scale1 = norm/(hist1->Integral());
	Double_t scale2 = norm/(hist2->Integral());
	hist1->Scale(scale1);
	hist2->Scale(scale2);

	//Whichever histogram has the fullest bin should be drawn first
	//hist1->Draw("hist");
	//hist2->Draw("hist same");
	hist2->Draw("hist");
	hist1->Draw("hist same");	

	//Add legend	
	auto legend = new TLegend(0.6,0.7,0.9,0.9);
	legend->AddEntry(hist1,"Low Pileup");
	legend->AddEntry(hist2,"High Pileup");
	legend->Draw();
}


