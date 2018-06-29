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


void plots_sig_and_background()
{
	//-----------------User Input--------------------//
	//Enter filenames
	//Make sure file1 is low pileup and file2 is high pileup, or change the legend
	TString sigName1="/afs/cern.ch/work/e/ebusch/public/h_bbar_datasets/ebuschFiles/lowpileupM3-4M6-9M12M14M18M22M25M27.root";
	TString sigName2="/afs/cern.ch/work/e/ebusch/public/h_bbar_datasets/evillhauFiles/highpileupM3-4M6-9M12M14M18M22M25M27.root";
        TString bkgName1="/afs/cern.ch/work/e/ebusch/public/h_bbar_datasets/ebuschFiles/user.ebusch.JZ11W.out1.root";
        TString bkgName2="/afs/cern.ch/work/e/ebusch/public/h_bbar_datasets/evillhauFiles/user.evillhar.JZ11W.out1.root";

	
	//Specify tree within file
	TString sigTreeName1="jetTree";
	TString sigTreeName2="jetTree";
	TString bkgTreeName1="jetTree";
        TString bkgTreeName2="jetTree";

	//Specify number of varaibles you want to plot
	const int numVars = 10;

	//Uncomment the correct variable type. You can only run one type at a time.
	Float_t sigVarPointers1[numVars];
	Float_t sigVarPointers2[numVars];
	Float_t bkgVarPointers1[numVars];
	Float_t bkgVarPointers2[numVars];
	//Int_t sigVarPointers1[numVars];
	//Int_t sigVarPointers2[numVars];
	//Int_t bkgVarPointers1[numVars];
        //Int_t bkgVarPointers2[numVars];

	//Add Branch names exactly as they appear 
	//Float_t variables
	const char * varNames[numVars] = {"jet_pt", "jet_eta", "jet_Exkt_phi_Lead", "jet_Exkt_m_Lead", "jet_Exkt_pt_Lead", "jet_Exkt_eta_Lead", "jet_Exkt_rnnip_pu_Lead", "jet_Exkt_pt_SubLead", "jet_Exkt_m_SubLead", "jet_Exkt_rnnip_pu_SubLead"};
	//const char * varNames[numVars] = {"jet_trk_mv2c10_SubLead", "jet_trk_mv2c10_Lead", "jet_trk_eta_Lead", "jet_trk_eta_SubLead", "jet_trk_pt_Lead", "jet_trk_pt_SubLead", "jet_trk_m_Lead", "jet_trk_m_SubLead", "jet_Exkt_sv1_deltaR_Lead", "jet_Exkt_sv1_deltaR_SubLead", "jet_Exkt_ip3d_pc_Lead", "jet_Exkt_ip3d_pc_SubLead", "jet_Exkt_ip3d_pb_Lead", "jet_Exkt_ip3d_pb_SubLead"};
	//const char * varNames[numVars] = {"PVy", "PVx"};
	//Int_t variables
	//const char * varNames[numVars] = {"nvtx"};
	
	//set this to 1 to save files as pngs in Plots folder (run with -b option). Set to 0 to see plots immediately
	Int_t saveFlag = 0;
	
	//--------------Open Root Files------------------//
	cout << "Opening "<< sigName1 << endl;
	TFile* sigFile1 = new TFile(sigName1);
	TTree* sigTree1 = (TTree*) sigFile1->Get(sigTreeName1);

	cout << "Opening "<< sigName2 << endl;
	TFile* sigFile2 = new TFile(sigName2);
	TTree* sigTree2 = (TTree*) sigFile2->Get(sigTreeName2);
	
	cout << "Opening "<< bkgName1 << endl;
        TFile* bkgFile1 = new TFile(bkgName1);
        TTree* bkgTree1 = (TTree*) bkgFile1->Get(bkgTreeName1);

        cout << "Opening "<< sigName2 << endl;
        TFile* bkgFile2 = new TFile(bkgName2);
        TTree* bkgTree2 = (TTree*) bkgFile2->Get(bkgTreeName2);

	//Initialize variables for scaling
	Float_t sigCross_Section1; Float_t bkgCross_Section1;
	Float_t sigCross_Section2; Float_t bkgCross_Section2;
	Int_t sigEvents1; Int_t bkgEvents1;
	Int_t sigEvents2; Int_t bkgEvents2;
	Float_t sigFilter_ef1; Float_t bkgFilter_ef1;
	Float_t sigFilter_ef2; Float_t bkgFilter_ef2;
	Float_t sigmcwg1; Float_t bkgmcwg1;
	Float_t sigmcwg2; Float_t bkgmcwg2;
	
	//Associate branch information with local address
	for (Int_t iter1 = 0; iter1 <numVars; iter1++){
		sigTree1->SetBranchAddress(varNames[iter1],&sigVarPointers1[iter1]);
		sigTree2->SetBranchAddress(varNames[iter1],&sigVarPointers2[iter1]);
	        bkgTree1->SetBranchAddress(varNames[iter1],&bkgVarPointers1[iter1]);
                bkgTree2->SetBranchAddress(varNames[iter1],&bkgVarPointers2[iter1]);
	}
	//Add scaling variables
	sigTree1->SetBranchAddress("Cross_Section",&sigCross_Section1);
	sigTree2->SetBranchAddress("Cross_Section",&sigCross_Section2);
	bkgTree1->SetBranchAddress("Cross_Section",&bkgCross_Section1);
        bkgTree2->SetBranchAddress("Cross_Section",&bkgCross_Section2);
	
	sigTree1->SetBranchAddress("Events",&sigEvents1);
	sigTree2->SetBranchAddress("Events",&sigEvents2);	
	bkgTree1->SetBranchAddress("Events",&bkgEvents1);
        bkgTree2->SetBranchAddress("Events",&bkgEvents2);

	sigTree1->SetBranchAddress("Filter_ef",&sigFilter_ef1);
	sigTree2->SetBranchAddress("Filter_ef",&sigFilter_ef2);
        bkgTree1->SetBranchAddress("Filter_ef",&bkgFilter_ef1);
        bkgTree2->SetBranchAddress("Filter_ef",&bkgFilter_ef2);

	sigTree1->SetBranchAddress("mcwg",&sigmcwg1);
	sigTree2->SetBranchAddress("mcwg",&sigmcwg2);
        bkgTree1->SetBranchAddress("mcwg",&bkgmcwg1);
        bkgTree2->SetBranchAddress("mcwg",&bkgmcwg2);


	//Calculate entries
	Long64_t numsigEvents1 = sigTree1->GetEntries();
	Long64_t numsigEvents2 = sigTree2->GetEntries();
        Long64_t numbkgEvents1 = bkgTree1->GetEntries();
        Long64_t numbkgEvents2 = bkgTree2->GetEntries();        

	//Initialize histograms
	TH1F *sigHist1[int(numVars)];
	TH1F *sigHist2[int(numVars)];
	TH1F *bkgHist1[int(numVars)];
        TH1F *bkgHist2[int(numVars)];
	
	//Define histogram ranges
	for (Int_t iter = 0; iter <numVars; iter++){
		TString sighTitle1;
		TString sighTitle2;
		TString bkghTitle1;
                TString bkghTitle2;
		sighTitle1.Form("%s_low-pu-sig",varNames[iter]);
		sighTitle2.Form("%s_high-pu-sig",varNames[iter]);
                bkghTitle1.Form("%s_low-pu-bkg",varNames[iter]);
                bkghTitle2.Form("%s_high-pu-bkg",varNames[iter]);
		
		//Calculate range
		Double_t sigMin1 = sigTree1->GetMinimum(varNames[iter]);
		Double_t sigMax1 = sigTree1->GetMaximum(varNames[iter]);
		Double_t sigMin2 = sigTree2->GetMinimum(varNames[iter]);
		Double_t sigMax2 = sigTree2->GetMaximum(varNames[iter]);
		
		Double_t bkgMin1 = bkgTree1->GetMinimum(varNames[iter]);
                Double_t bkgMax1 = bkgTree1->GetMaximum(varNames[iter]);
                Double_t bkgMin2 = bkgTree2->GetMinimum(varNames[iter]);
                Double_t bkgMax2 = bkgTree2->GetMaximum(varNames[iter]);
		
		Double_t minElement = min(sigMin1,min(sigMin2,min(bkgMin1,bkgMin2)));
		Double_t maxElement = max(sigMax1,max(sigMax2,max(bkgMax1,bkgMax2)));	

	
		Double_t minuse;
		if (sigMin1 < 0 || sigMin2 < 0 || bkgMin1 < 0 || bkgMin2 <0){
			minuse = 1.05*minElement;
		}
		else{
			minuse = 0.95*minElement;
		}
		Double_t maxuse;
		if (sigMax1 < 0 || sigMax2 < 0 || bkgMax1 < 0 || bkgMax2 <0){
			maxuse = 0.95*maxElement;
		} else{
			maxuse = 1.05*maxElement;
		}
		sigHist1[iter] = new TH1F(sighTitle1,varNames[iter],100,minuse,maxuse);
		sigHist2[iter] = new TH1F(sighTitle2,varNames[iter],100,minuse,maxuse);
		bkgHist1[iter] = new TH1F(bkghTitle1,varNames[iter],100,minuse,maxuse);
                bkgHist2[iter] = new TH1F(bkghTitle2,varNames[iter],100,minuse,maxuse);
	}

	
	//Add entries to histograms
	for(Int_t iter = 0; iter <numVars; iter++){
		for(Long64_t iEntry1 = 0; iEntry1 <numsigEvents1; iEntry1++){
			sigTree1->GetEntry(iEntry1);
			Double_t sigScale1 = sigmcwg1*sigCross_Section1*sigFilter_ef1/sigEvents1;		
			sigHist1[iter]->Fill(sigVarPointers1[iter],sigScale1);
		}
	}

	for(Int_t iter = 0; iter <numVars; iter++){
        	for(Long64_t iEntry2 = 0; iEntry2 <numsigEvents2; iEntry2++){
                	sigTree2->GetEntry(iEntry2);
			Double_t sigScale2 = sigmcwg2*sigCross_Section2*sigFilter_ef2/sigEvents2;
                        sigHist2[iter]->Fill(sigVarPointers2[iter],sigScale2);///sigEvents2);
                }
        }

        for(Int_t iter = 0; iter <numVars; iter++){
                for(Long64_t iEntry3 = 0; iEntry3 <numbkgEvents1; iEntry3++){
                        bkgTree1->GetEntry(iEntry3);
                        Double_t bkgScale1 = bkgmcwg1*bkgCross_Section1*bkgFilter_ef1/bkgEvents1;
                        bkgHist1[iter]->Fill(bkgVarPointers1[iter],bkgScale1);
                }
        }

        for(Int_t iter = 0; iter <numVars; iter++){
                for(Long64_t iEntry4 = 0; iEntry4 <numbkgEvents2; iEntry4++){
                        bkgTree2->GetEntry(iEntry4);
                        Double_t bkgScale2 = bkgmcwg2*bkgCross_Section2*bkgFilter_ef2/bkgEvents2;
                        bkgHist2[iter]->Fill(bkgVarPointers2[iter],bkgScale2);
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
	Double_t sigNormalize1[numVars];
	Double_t sigNormalize2[numVars];
        Double_t bkgNormalize1[numVars];
        Double_t bkgNormalize2[numVars];

	for(Int_t iter = 0; iter <numVars; iter++){
		//Set up histograms
		TString canv;
		canv.Form("c%d",int(iter));
		c[iter] = new TCanvas(canv,canv,600,400);
		c[iter]->cd();

		sigHist1[iter]->SetStats(0);
		sigHist2[iter]->SetStats(0);
		sigHist1[iter]->SetLineColor(kBlue);
		sigHist2[iter]->SetLineColor(kRed);
		sigHist1[iter]->GetXaxis()->SetTitle(varNames[iter]);
		sigHist2[iter]->GetXaxis()->SetTitle(varNames[iter]);
		sigHist1[iter]->GetYaxis()->SetTitle("A.U.");
		sigHist2[iter]->GetYaxis()->SetTitle("A.U.");
	
                bkgHist1[iter]->SetStats(0);
                bkgHist2[iter]->SetStats(0);
                bkgHist1[iter]->SetLineColor(kBlue);
                bkgHist2[iter]->SetLineColor(kRed);
		bkgHist1[iter]->SetLineStyle(2);
                bkgHist2[iter]->SetLineStyle(2);
                bkgHist1[iter]->GetXaxis()->SetTitle(varNames[iter]);
                bkgHist2[iter]->GetXaxis()->SetTitle(varNames[iter]);
                bkgHist1[iter]->GetYaxis()->SetTitle("A.U.");
                bkgHist2[iter]->GetYaxis()->SetTitle("A.U.");

		//Switch to arbitrary units
		sigNormalize1[iter] = norm/(sigHist1[iter]->Integral());
		sigNormalize2[iter] = norm/(sigHist2[iter]->Integral());
		bkgNormalize1[iter] = norm/(bkgHist1[iter]->Integral());
                bkgNormalize2[iter] = norm/(bkgHist2[iter]->Integral());
		sigHist1[iter]->Scale(sigNormalize1[iter]);
		sigHist2[iter]->Scale(sigNormalize2[iter]);
                bkgHist1[iter]->Scale(bkgNormalize1[iter]);
                bkgHist2[iter]->Scale(bkgNormalize2[iter]);
	
		//Plot taller bins first
		Double_t binsigMax1 = sigHist1[iter]->GetMaximum();
		Double_t binsigMax2 = sigHist2[iter]->GetMaximum();
                Double_t binbkgMax1 = bkgHist1[iter]->GetMaximum();
                Double_t binbkgMax2 = bkgHist2[iter]->GetMaximum();
		
		Double_t binArray[4] = {binsigMax1,binsigMax2,binbkgMax1,binbkgMax2};
		Double_t maxBin = max(binsigMax1,max(binsigMax2,max(binbkgMax1,binbkgMax2)));
		if (binsigMax1 == maxBin){
			sigHist1[iter]->Draw("hist");
			sigHist2[iter]->Draw("hist same");
			bkgHist1[iter]->Draw("hist same");
			bkgHist2[iter]->Draw("hist same");
		} else if (binsigMax2 == maxBin){
			sigHist2[iter]->Draw("hist");
			sigHist1[iter]->Draw("hist same");
			bkgHist1[iter]->Draw("hist same");
			bkgHist2[iter]->Draw("hist same");
		}else if (binbkgMax1 == maxBin){
		 	bkgHist1[iter]->Draw("hist");
                        sigHist1[iter]->Draw("hist same");
			sigHist2[iter]->Draw("hist same");
			bkgHist2[iter]->Draw("hist same");
		}else {
			bkgHist2[iter]->Draw("hist");
                        sigHist1[iter]->Draw("hist same");
                        sigHist2[iter]->Draw("hist same");
                        bkgHist1[iter]->Draw("hist same");	
		}
		//Add legend	
		//TLegend *legend[numVars];
		legend[iter] = new TLegend(0.7,0.7,0.9,0.9);
		legend[iter]->AddEntry(sigHist1[iter],"Sig:Low PU");
		legend[iter]->AddEntry(sigHist2[iter],"Sig:High PU");
		legend[iter]->AddEntry(bkgHist1[iter],"Bkg:Low PU");
		legend[iter]->AddEntry(bkgHist2[iter],"Bkg:High PU");
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


