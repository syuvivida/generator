#define simple_cxx
#include "simple.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TLorentzVector.h>

const double minZPt  =40.0;

const double minJetPt=30.0;
const double maxJetEta=2.4;
const double mindR=0.5;

const double minElePt = 20.0;
const double maxEleEta = 2.1;

const double minMee = 76.0;
const double maxMee =106.0;

const double minMuoPt = 20.0;
const double maxMuoEta = 2.1;
const double minMmm = 76.0;
const double maxMmm =106.0;

void simple::Loop(int lepID)
{
  //===========================================================================
  //   Print out information
  //===========================================================================

  if (fChain == 0) return;
  cout << "=========================================================" << endl;

  Long64_t nentries = fChain->GetEntries();

  cout << "The tree has " << nentries << " entries." << endl;
  std::string leptonName;
  if(abs(lepID)==13)leptonName = "muon";
  else if(abs(lepID)==11)leptonName = "electron";

  cout << "Running mode: " << endl;
  cout << "The cuts applied: " << endl;
  
  cout << " minZPt= " << minZPt << endl;
  cout << " minJetPt= " << minJetPt << endl;
  cout << " maxJetEta= " << maxJetEta << endl;
  cout << " mindR= " << mindR << endl;

  cout << "studying " << leptonName << endl;
  if(abs(lepID)==11){
    cout << " minElePt= " << minElePt << endl;
    cout << " maxEleEta = " << maxEleEta << endl;
    cout << " minMee = " << minMee << endl;
    cout << " maxMee = " << maxMee << endl;
  }
  else if(abs(lepID)==13){
    cout << " minMuoPt = " << minMuoPt << endl;
    cout << " maxMuoEta = " << maxMuoEta << endl;
    cout << " minMmm = " << minMmm << endl;
    cout << " maxMmm = " << maxMmm << endl;
  }
  cout << "=========================================================" << endl;

  // dummy proof, in case someone put a negative number
  int leptonPID = abs(lepID); 

  //===========================================================================
  //   Book histograms
  //===========================================================================

  TH1D* h_mZ   = new TH1D("h_mZ","",200,20.0,220.0);
  h_mZ->SetXTitle("M_{ll} [GeV/c^{2}");
  h_mZ->Sumw2();

  TH1D* h_mZ_parton   = new TH1D("h_mZ_parton","",200,20.0,220.0);
  h_mZ_parton->SetXTitle("M_{ll} [GeV/c^{2}");
  h_mZ_parton->Sumw2();

  TH1D* h_nvtx = new TH1D("h_nvtx","",41.5,-0.5,40.5);
  h_nvtx->SetXTitle("Number of good vertices");
  h_nvtx->Sumw2();

  TH1D* h_njet = new TH1D("h_njet","",6,-0.5,5.5);
  h_njet->SetXTitle("jet multiplicity (p_{T} > 20 GeV, |#eta| < 3.0)");
  h_njet->Sumw2();

  TH1D* h_zpt_template = new TH1D("h_zpt_template","",40,0,400);
  h_zpt_template->Sumw2();

  TH1D* h_zpt   = (TH1D*)h_zpt_template->Clone("h_zpt");
  h_zpt->SetXTitle("p_{T}(Z) [GeV]");

  TH1D* h_jetpt_template = new TH1D("h_jetpt_template","",40,0,400);
  h_jetpt_template->Sumw2();

  TH1D* h_jetpt = (TH1D*)h_jetpt_template->Clone("h_jetpt");
  h_jetpt->SetXTitle("p_{T}(jet) [GeV]");

  TH1D* h_ypart_template = new TH1D("h_ypart_template","",15,0.0,3.0); 
  h_ypart_template->Sumw2();

  TH1D* h_zy    = (TH1D*)h_ypart_template->Clone("h_zy");
  h_zy->SetXTitle("|y_{Z}|");

  TH1D* h_jety    = (TH1D*)h_ypart_template->Clone("h_jety");
  h_jety->SetXTitle("|y_{jet}|");

  TH1D* h_y_template = new TH1D("h_y_template","",15,0.0,3.0);
  h_y_template->Sumw2();

  TH1D* h_yB    = (TH1D*)h_y_template->Clone("h_yB");
  h_yB->SetXTitle("0.5|y_{Z}+y_{jet}|");

  TH1D* h_ystar = (TH1D*)h_y_template->Clone("h_ystar");
  h_ystar->SetXTitle("0.5|y_{Z}-y_{jet}|");

  int nPass[30]={0};
   
  Long64_t nbytes = 0, nb = 0;
  for (Long64_t jentry=0; jentry<nentries;jentry++) {
    
//     if(jentry > 1000) break;

    Long64_t ientry = LoadTree(jentry);
    if (ientry < 0) break;
    nb = fChain->GetEntry(jentry);   nbytes += nb;

    nPass[0]++;

    int lepPlusIndex = -1;
    int lepMinusIndex = -1;
    double eventWeight = 1;

    h_nvtx->Fill(EvtInfo_NumVtx, eventWeight);


    for(unsigned int igen=0; igen < genParId_->size(); igen++){

      int PID       = genParId_->at(igen);
      int motherPID = genMomParId_->at(igen);
      int status    = genParSt_->at(igen);
      bool isFromZAfterFSR  = (motherPID == PID) && (status == 1);

      bool isLepPlus = (PID == (-leptonPID)) && isFromZAfterFSR;
      bool isLepMinus= (PID == ( leptonPID)) && isFromZAfterFSR;

      TLorentzVector temp_l4(0,0,0,0);
      temp_l4.SetPtEtaPhiE(
			   genParPt_->at(igen),
			   genParEta_->at(igen),
			   genParPhi_->at(igen),
			   genParE_->at(igen)
			   );

      if(PID == 23 && status == 3)
	h_mZ_parton->Fill(temp_l4.M(), eventWeight);

      if(lepPlusIndex < 0 && isLepPlus)
	lepPlusIndex = igen;

      if(lepMinusIndex < 0 && isLepMinus)
	lepMinusIndex = igen;
	
      // need to add a line and see if this is a daughter of Z-> tau tau
      if(lepPlusIndex >= 0 && lepMinusIndex >=0)
	break;
	
    }

    // do not find m+ or lep-
    if(lepPlusIndex < 0 || lepMinusIndex < 0)continue;

    nPass[1]++;

    int nPt20=0;

    int indexNumbers[2] = {lepPlusIndex, lepMinusIndex};

    for(int ip=0; ip < 2; ip++){

      double pt  = genParPt_->at(indexNumbers[ip]);
      double eta = genParEta_->at(indexNumbers[ip]);

      // muon
      if(leptonPID==13 && pt > minMuoPt && fabs(eta) < maxMuoEta)nPt20++;
      if(leptonPID==11 && pt > minElePt && fabs(eta) < maxEleEta)nPt20++;
      
    }


    if(leptonPID==13 && (nPt20 < 2))continue;
    if(leptonPID==11 && (nPt20 < 2))continue;

    nPass[2]++;

    TLorentzVector l4_lepp(0,0,0,0);

    l4_lepp.SetPtEtaPhiE(genParPt_->at(lepPlusIndex),
			 genParEta_->at(lepPlusIndex),
			 genParPhi_->at(lepPlusIndex),
			 genParE_->at(lepPlusIndex));

    TLorentzVector l4_lepm(0,0,0,0);

    l4_lepm.SetPtEtaPhiE(genParPt_->at(lepMinusIndex),
			 genParEta_->at(lepMinusIndex),
			 genParPhi_->at(lepMinusIndex),
			 genParE_->at(lepMinusIndex));


    TLorentzVector l4_z = l4_lepp + l4_lepm;


    double mll = l4_z.M();

    h_mZ->Fill(mll,eventWeight);

    if(leptonPID==13 && (mll < minMmm || mll > maxMmm))continue;
    if(leptonPID==11 && (mll < minMee || mll > maxMee))continue;

    nPass[3]++;

    double ptz = l4_z.Pt();
    if(ptz < minZPt)continue;
    nPass[4]++;

    // now look for jets
    double maxGenJetPt = -9999;
    int maxGenJetIndex = -1;
    unsigned int nGenJets = 0;
    unsigned int nLooseGenJets = 0;

    for(unsigned int ij = 0; ij < genJetPt_->size(); ij ++){

      double thisGenJetPt  = genJetPt_->at(ij);
      double thisGenJetEta = genJetEta_->at(ij);

      if(fabs(thisGenJetEta) > maxJetEta)continue;

      TLorentzVector thisGenJet_l4(0,0,0,0);
	
      thisGenJet_l4.SetPtEtaPhiE(genJetPt_->at(ij),
				 genJetEta_->at(ij),
				 genJetPhi_->at(ij),
				 genJetE_->at(ij));
	
      double dr_ep = l4_lepp.DeltaR(thisGenJet_l4);
      double dr_em = l4_lepm.DeltaR(thisGenJet_l4);

      if(dr_ep < mindR)continue;
      if(dr_em < mindR)continue;

      if(thisGenJetPt < 20)continue;
      nLooseGenJets ++;

      if(thisGenJetPt < minJetPt)continue;
      nGenJets++; 

      if(thisGenJetPt > maxGenJetPt)
	{
	  maxGenJetPt = thisGenJetPt;
	  maxGenJetIndex = ij;
	}
	
    } // end of loop over jets
      
    if(maxGenJetIndex < 0)continue;
    nPass[5]++;
    h_njet->Fill(nLooseGenJets, eventWeight);

    if(nGenJets!=1)continue;     
    nPass[6]++;



    TLorentzVector l4_j(0,0,0,0);
    l4_j.SetPtEtaPhiE(genJetPt_->at(maxGenJetIndex),
		      genJetEta_->at(maxGenJetIndex),
		      genJetPhi_->at(maxGenJetIndex),
		      genJetE_->at(maxGenJetIndex));

    double ptjet = l4_j.Pt();
    double yz = l4_z.Rapidity();
    double yj = l4_j.Rapidity();

    double yB = 0.5*(yz + yj);
    double ystar = 0.5*(yz-yj);

    h_zpt->Fill(ptz,eventWeight);
    h_jetpt->Fill(ptjet,eventWeight); 
    h_zy->Fill(fabs(yz),eventWeight);
    h_jety->Fill(fabs(yj),eventWeight);
    h_yB->Fill(fabs(yB),eventWeight);
    h_ystar->Fill(fabs(ystar),eventWeight);


  } // end of loop over entries

  for(int i=0;i<30;i++)
    if(nPass[i]>0)cout << "nPass["<< i << "] = " << nPass[i] << endl;

  std::string remword  ="/data4/syu/madgraph_lhe/";

  size_t pos  = _inputFile.find(remword);

  if(pos!= std::string::npos)
    _inputFile.swap(_inputFile.erase(pos,remword.length()));
  TFile* outFile = new TFile(Form("histo_%s",_inputFile.data()),"recreate");       

  h_mZ->Write();
  h_mZ_parton->Write();
  h_nvtx->Write();
        
  h_yB->Write();
  h_ystar->Write();
  
  h_zy->Write();
  h_zpt->Write();

  h_jety->Write();   
  h_jetpt->Write();

  h_njet->Write();

  outFile->Close();
}


