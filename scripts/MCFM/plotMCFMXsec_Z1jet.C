
void plotMCFMXsec_Z1jet(std::string file="Z_1jet_tota_CT10_mcfm.root")
{

  const double fBinsPt[]={30,40,55,75,105,150,210,315,500};
  const int nPtBins = sizeof(fBinsPt)/sizeof(fBinsPt[0])-1;

  cout << "There are " << nPtBins << " bins." << endl;    

  const double fBinsY[]={0.0,0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4};
  const int nYBins = sizeof(fBinsY)/sizeof(fBinsY[0])-1;

  cout << "There are " << nYBins << " bins." << endl;

  TH1D* h_diff_mcfm_jetpt01 = new TH1D("h_diff_mcfm_jetpt01", "",
				       nPtBins, fBinsPt);
  TH1D* h_diff_mcfm_jety01 = new TH1D("h_diff_mcfm_jety01", "",
				       nYBins, fBinsY);

  
  TH1F* h_mcfm_original_pt;
  TH1F* h_mcfm_original_y;


  TFile *fmcfm = TFile::Open(file.data());
  
  h_mcfm_original_pt =  (TH1F*)(fmcfm->Get("id5"));
  h_mcfm_original_pt -> SetName("h_mcfm_original_pt");

  h_mcfm_original_y =  (TH1F*)(fmcfm->Get("id6"));
  h_mcfm_original_y -> SetName("h_mcfm_original_y");

  double total_y_xsec = 0;
  for(int i=1; i<= nYBins; i++)
    {
      h_diff_mcfm_jety01->SetBinContent(i, h_mcfm_original_y->GetBinContent(i));
      h_diff_mcfm_jety01->SetBinError(i,h_mcfm_original_y->GetBinError(i));

      total_y_xsec += h_diff_mcfm_jety01->GetBinContent(i)*
	h_diff_mcfm_jety01->GetBinWidth(i);

      cout << "Differential cross section at "
	   << h_diff_mcfm_jety01->GetBinLowEdge(i) 
	   << "~"
	   << h_diff_mcfm_jety01->GetBinLowEdge(i+1) 
	   << " = " 
	   << h_diff_mcfm_jety01->GetBinContent(i)
	   << " +- " 
	   << h_diff_mcfm_jety01->GetBinError(i) <<  " fb" << endl;
    }

  double default_width = h_mcfm_original_pt->GetBinWidth(1);
  double total_pt_xsec=0;

  for(int i=1; i<= nPtBins; i++)
    {
      cout << "i = " << i << endl;
      int BinStart = h_mcfm_original_pt->FindBin(fBinsPt[i-1]);
      int BinEnd   = h_mcfm_original_pt->FindBin(fBinsPt[i])-1;

      double xStart = h_mcfm_original_pt->GetBinLowEdge(BinStart);
      double xEnd   = h_mcfm_original_pt->GetBinLowEdge(BinEnd+1);

      double Width = xEnd-xStart;

      cout << "Bin started at index " << BinStart << " at " 
	   << xStart << "\t";

      cout << "Bin ended at index " << BinEnd << " at " 
	   << xEnd << endl;

//       cout << "Width = " << Width << " GeV" << endl;
      
      double mcfm_diff = h_mcfm_original_pt->Integral(BinStart,BinEnd);

      mcfm_diff *= default_width;

//       cout << "Integrated cross section = " << mcfm_diff << " fb" << endl;

      if(Width<1e-6){
	cout << "Incorrect width" << endl;
	continue;
      }
      mcfm_diff /= Width;

      double mcfm_diff_err = 0;
      for(int ib=BinStart; ib<= BinEnd; ib++){
	mcfm_diff_err += pow(h_mcfm_original_pt->GetBinError(ib),2);
      }

      mcfm_diff_err = sqrt(mcfm_diff_err);
      mcfm_diff_err *= default_width/Width;

      h_diff_mcfm_jetpt01->SetBinContent(i,mcfm_diff);
      h_diff_mcfm_jetpt01->SetBinError(i,mcfm_diff_err);

      total_pt_xsec += h_diff_mcfm_jetpt01->GetBinContent(i)*
	h_diff_mcfm_jetpt01->GetBinWidth(i);

    }


  for(int i=1; i<= nPtBins; i++)
    {

      cout << "Differential cross section at "
	   << h_diff_mcfm_jetpt01->GetBinLowEdge(i) 
	   << "~"
	   << h_diff_mcfm_jetpt01->GetBinLowEdge(i+1) 
	   << " = " 
	   << h_diff_mcfm_jetpt01->GetBinContent(i)
	   << " +- " 
	   << h_diff_mcfm_jetpt01->GetBinError(i) <<  " fb/GeV" << endl;
    }
 
  cout << "Total xsection from pt graph = " << total_pt_xsec << " fb" << endl;
  cout << "Total xsection from y graph = " << total_y_xsec << " fb" << endl;

  cout << "Ratio = " << total_pt_xsec/total_y_xsec << endl;

  TFile* outFile = new TFile(Form("mcfm1jetXsec_%s",file.data()),"recreate");       
  
  h_diff_mcfm_jetpt01->Write();
  h_diff_mcfm_jety01->Write();
 
  outFile->Close();
}
