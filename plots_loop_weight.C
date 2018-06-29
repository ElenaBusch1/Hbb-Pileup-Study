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

////////////////////////////////////////////////////////////////////////////////////////////////////////
//////This macro make comparison histograms of variables for low vs high pileup studies               //
//////Fill in the user inputs below and then run with "root -l plots_loop_weight.C                    //
////////////////////////////////////////////////////////////////////////////////////////////////////////


void plots_loop_weight()
{
	//-----------------User Input--------------------//
	//Enter filenames
	//Make sure file1 is low pileup and file2 is high pileup, or change the legend
	TString fileName1="/afs/cern.ch/work/e/ebusch/public/h_bbar_datasets/ebuschFiles/lowpileupM3-4M6-9M12M14M18M22M25M27.root";
	TString fileName2="/afs/cern.ch/work/e/ebusch/public/h_bbar_datasets/evillhauFiles/highpileupM3-4M6-9M12M14M18M22M25M27.root";
	
	//Specify tree within file
	TString treeName1="jetTree";
	TString treeName2="jetTree";

	//Specify number of varaibles you want to plot
	const int numVars = 1;

	//Uncomment the correct variable type. You can only run one type at a time.
	//Float_t varPointers1[numVars];
	//Float_t varPointers2[numVars];
	Int_t varPointers1[numVars];
	Int_t varPointers2[numVars];

	//Add Branch names exactly as they appear 
	//Float_t variables
	//const char * varNames[numVars] = {"jet_pt", "jet_eta", "jet_Exkt_phi_Lead", "jet_Exkt_m_Lead", "jet_Exkt_pt_Lead", "jet_Exkt_eta_Lead", "jet_Exkt_rnnip_pu_Lead", "jet_Exkt_pt_SubLead", "jet_Exkt_m_SubLead", "jet_Exkt_rnnip_pu_SubLead"};
	//const char * varNames[numVars] = {"jet_trk_mv2c10_SubLead", "jet_trk_mv2c10_Lead", "jet_trk_eta_Lead", "jet_trk_eta_SubLead", "jet_trk_pt_Lead", "jet_trk_pt_SubLead", "jet_trk_m_Lead", "jet_trk_m_SubLead", "jet_Exkt_sv1_deltaR_Lead", "jet_Exkt_sv1_deltaR_SubLead", "jet_Exkt_ip3d_pc_Lead", "jet_Exkt_ip3d_pc_SubLead", "jet_Exkt_ip3d_pb_Lead", "jet_Exkt_ip3d_pb_SubLead"};
	//const char * varNames[numVars] = {"PVy", "PVx"};
	//Int_t variables
	const char * varNames[numVars] = {"nvtx"};
	
	//set this to 1 to save files as pngs in Plots folder (run with -b option). Set to 0 to see plots immediately
	Int_t saveFlag = 1;
	
	//--------------Open Root Files------------------//
	cout << "Opening "<< fileName1 << endl;
	TFile* myFile1 = new TFile(fileName1);
	TTree* myTree1 = (TTree*) myFile1->Get(treeName1);

	cout << "Opening "<< fileName2 << endl;
	TFile* myFile2 = new TFile(fileName2);
	TTree* myTree2 = (TTree*) myFile2->Get(treeName2);
	
	//Initialize variables for scaling
	Float_t Cross_Section1;
	Float_t Cross_Section2;
	Int_t Events1;
	Int_t Events2;
	Float_t Filter_ef1;	
	Float_t Filter_ef2;
	Float_t mcwg1;
	Float_t mcwg2;
	
	//Associate branch information with local address
	for (Int_t iter1 = 0; iter1 <numVars; iter1++){
		myTree1->SetBranchAddress(varNames[iter1],&varPointers1[iter1]);
		myTree2->SetBranchAddress(varNames[iter1],&varPointers2[iter1]);
	}
	//Add scaling variables
	myTree1->SetBranchAddress("Cross_Section",&Cross_Section1);
	myTree2->SetBranchAddress("Cross_Section",&Cross_Section2);
	myTree1->SetBranchAddress("Events",&Events1);
	myTree2->SetBranchAddress("Events",&Events2);	
	myTree1->SetBranchAddress("Filter_ef",&Filter_ef1);
	myTree2->SetBranchAddress("Filter_ef",&Filter_ef2);
	myTree1->SetBranchAddress("mcwg",&mcwg1);
	myTree2->SetBranchAddress("mcwg",&mcwg2);

	//Calculate entries
	Long64_t numEvents1 = myTree1->GetEntries();
	Long64_t numEvents2 = myTree2->GetEntries();
        
	//Initialize histograms
	TH1F *hist1[int(numVars)];
	TH1F *hist2[int(numVars)];
	
	//Define histogram ranges
	for (Int_t iter = 0; iter <numVars; iter++){
		TString hTitle1;
		TString hTitle2;
		hTitle1.Form("%s_low-pu",varNames[iter]);
		hTitle2.Form("%s_high-pu",varNames[iter]);
		//Calculate range
		Double_t min1 = myTree1->GetMinimum(varNames[iter]);
		Double_t max1 = myTree1->GetMaximum(varNames[iter]);
		Double_t min2 = myTree2->GetMinimum(varNames[iter]);
		Double_t max2 = myTree2->GetMaximum(varNames[iter]);
		Double_t minuse;
		if (min1 < 0 || min2 < 0){
			minuse = 1.05*min(min1,min2);
		}
		else{
			minuse = 0.95*min(min1,min2);
		}
		Double_t maxuse;
		if (max1 < 0 || max2 < 0){
			maxuse = 0.95*max(max1,max2);
		} else{
			maxuse = 1.05*max(max1, max2);
		}
		hist1[iter] = new TH1F(hTitle1,varNames[iter],100,minuse,maxuse);
		hist2[iter] = new TH1F(hTitle2,varNames[iter],100,minuse,maxuse);
	}

	
	//Add entries to histograms
	for(Int_t iter = 0; iter <numVars; iter++){
		for(Long64_t iEntry1 = 0; iEntry1 <numEvents1; iEntry1++){
			myTree1->GetEntry(iEntry1);
			Double_t scale1 = mcwg1*Cross_Section1*Filter_ef1/Events1;		
			hist1[iter]->Fill(varPointers1[iter],scale1);
		}
	}

	for(Int_t iter = 0; iter <numVars; iter++){
        	for(Long64_t iEntry2 = 0; iEntry2 <numEvents2; iEntry2++){
                	myTree2->GetEntry(iEntry2);
			Double_t scale2 = mcwg2*Cross_Section2*Filter_ef2/Events2;
                        hist2[iter]->Fill(varPointers2[iter],scale2);///Events2);
                }
        }



	//----------------Make Plots-------------------//
	cout << "Making plots" << endl;
	
	//Initialize plotting variables
	TCanvas *c[numVars];
	TLegend *legend[numVars];
	TImage *img[int(numVars)];
	
	//Make a plots directory
	if(gSystem->AccessPathName("Plots/")){
		system("mkdir Plots/");
	}
	TString outFolder = "Plots/";
	
	Double_t norm = 1;
	Double_t normalize1[numVars];
	Double_t normalize2[numVars];

	for(Int_t iter = 0; iter <numVars; iter++){
		//Set up histograms
		TString canv;
		canv.Form("c%d",int(iter));
		c[iter] = new TCanvas(canv,canv,600,400);
		c[iter]->cd();
		hist1[iter]->SetStats(0);
		hist2[iter]->SetStats(0);
		hist1[iter]->SetLineColor(kBlue);
		hist2[iter]->SetLineColor(kRed);
		hist1[iter]->GetXaxis()->SetTitle(varNames[iter]);
		hist2[iter]->GetXaxis()->SetTitle(varNames[iter]);
		hist1[iter]->GetYaxis()->SetTitle("A.U.");
		hist2[iter]->GetYaxis()->SetTitle("A.U.");
	
		//Switch to arbitrary units
		normalize1[iter] = norm/(hist1[iter]->Integral());
		normalize2[iter] = norm/(hist2[iter]->Integral());
		hist1[iter]->Scale(normalize1[iter]);
		hist2[iter]->Scale(normalize2[iter]);
	
		//Plot taller bins first
		Double_t binmax1 = hist1[iter]->GetMaximum();
		Double_t binmax2 = hist2[iter]->GetMaximum();
		if (binmax1 > binmax2){
			hist1[iter]->Draw("hist");
			hist2[iter]->Draw("hist same");
		} else{
			hist2[iter]->Draw("hist");
			hist1[iter]->Draw("hist same");
		}	 	
		
		//Add legend	
		//TLegend *legend[numVars];
		legend[iter] = new TLegend(0.7,0.8,0.9,0.9);
		legend[iter]->AddEntry(hist1[iter],"Low Pileup");
		legend[iter]->AddEntry(hist2[iter],"High Pileup");
		legend[iter]->Draw();
		//c[iter]->BuildLegend();
	
		//Save images
		if (saveFlag == 1){
			img[iter] = TImage::Create();
               		img[iter]->FromPad(c[iter]);
                	TString img_name;
                	img_name.Form("%s.png",varNames[iter]);
			TString img_out = outFolder + img_name;
                	img[iter]->WriteImage(img_out);
		}
	}
	

}


