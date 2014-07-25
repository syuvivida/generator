//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Fri Dec 21 13:48:28 2012 by ROOT version 5.32/00
// from TTree tree/tree
// found on file: zJettest_test.root
//////////////////////////////////////////////////////////

#ifndef simple_h
#define simple_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include <vector>
#include <iostream>
#include <string>

using namespace std;

// Fixed size dimensions of array or collections stored in the TTree if any.
const Int_t kMaxEvtInfo_VertexX = 1;
const Int_t kMaxEvtInfo_VertexY = 1;
const Int_t kMaxEvtInfo_VertexZ = 1;
const Int_t kMaxptHat = 1;
const Int_t kMaxmcWeight = 1;
const Int_t kMaxgenParE = 1;
const Int_t kMaxgenParPt = 1;
const Int_t kMaxgenParEta = 1;
const Int_t kMaxgenParPhi = 1;
const Int_t kMaxgenParM = 1;
const Int_t kMaxgenParQ = 1;
const Int_t kMaxgenParId = 1;
const Int_t kMaxgenParSt = 1;
const Int_t kMaxgenMomParId = 1;
const Int_t kMaxgenParIndex = 1;
const Int_t kMaxgenNMo = 1;
const Int_t kMaxgenNDa = 1;
const Int_t kMaxgenMo1 = 1;
const Int_t kMaxgenMo2 = 1;
const Int_t kMaxgenDa1 = 1;
const Int_t kMaxgenDa2 = 1;
const Int_t kMaxgenJetE = 1;
const Int_t kMaxgenJetPt = 1;
const Int_t kMaxgenJetEta = 1;
const Int_t kMaxgenJetPhi = 1;

class simple {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Int_t           EvtInfo_EventNum;
   Int_t           EvtInfo_RunNum;
   Int_t           EvtInfo_LumiSection;
   Int_t           EvtInfo_BunchXing;
   Int_t           EvtInfo_NumVtx;
   vector<double>  *EvtInfo_VertexX_;
   vector<double>  *EvtInfo_VertexY_;
   vector<double>  *EvtInfo_VertexZ_;
   Double_t        ptHat_;
   Double_t        mcWeight_;
   vector<double>  *genParE_;
   vector<double>  *genParPt_;
   vector<double>  *genParEta_;
   vector<double>  *genParPhi_;
   vector<double>  *genParM_;
   vector<int>     *genParQ_;
   vector<int>     *genParId_;
   vector<int>     *genParSt_;
   vector<int>     *genMomParId_;
   vector<int>     *genParIndex_;
   vector<int>     *genNMo_;
   vector<int>     *genNDa_;
   vector<int>     *genMo1_;
   vector<int>     *genMo2_;
   vector<int>     *genDa1_;
   vector<int>     *genDa2_;
   vector<double>  *genJetE_;
   vector<double>  *genJetPt_;
   vector<double>  *genJetEta_;
   vector<double>  *genJetPhi_;

   // List of branches
   TBranch        *b_EvtInfo_EventNum;   //!
   TBranch        *b_EvtInfo_RunNum;   //!
   TBranch        *b_EvtInfo_LumiSection;   //!
   TBranch        *b_EvtInfo_BunchXing;   //!
   TBranch        *b_EvtInfo_NumVtx;   //!
   TBranch        *b_EvtInfo_VertexX_;   //!
   TBranch        *b_EvtInfo_VertexY_;   //!
   TBranch        *b_EvtInfo_VertexZ_;   //!
   TBranch        *b_ptHat_;   //!
   TBranch        *b_mcWeight_;   //!
   TBranch        *b_genParE_;   //!
   TBranch        *b_genParPt_;   //!
   TBranch        *b_genParEta_;   //!
   TBranch        *b_genParPhi_;   //!
   TBranch        *b_genParM_;   //!
   TBranch        *b_genParQ_;   //!
   TBranch        *b_genParId_;   //!
   TBranch        *b_genParSt_;   //!
   TBranch        *b_genMomParId_;   //!
   TBranch        *b_genParIndex_;   //!
   TBranch        *b_genNMo_;   //!
   TBranch        *b_genNDa_;   //!
   TBranch        *b_genMo1_;   //!
   TBranch        *b_genMo2_;   //!
   TBranch        *b_genDa1_;   //!
   TBranch        *b_genDa2_;   //!
   TBranch        *b_genJetE_;   //!
   TBranch        *b_genJetPt_;   //!
   TBranch        *b_genJetEta_;   //!
   TBranch        *b_genJetPhi_;   //!

   simple(std::string input, TTree *tree=0);
   virtual ~simple();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop(int lepID=13);
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
   std::string      _inputFile;
};

#endif

#ifdef simple_cxx
simple::simple(std::string input, TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
  _inputFile = input;
  if (tree == 0) {
    TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject(_inputFile.data());
    if (!f || !f->IsOpen()) {
      f = new TFile(_inputFile.data());
    }
    TDirectory * dir = (TDirectory*)f->Get(Form("%s:/tree",_inputFile.data()));
    dir->GetObject("tree",tree);

  }
  Init(tree);
}

simple::~simple()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t simple::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t simple::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void simple::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   EvtInfo_VertexX_ = 0;
   EvtInfo_VertexY_ = 0;
   EvtInfo_VertexZ_ = 0;
   genParE_ = 0;
   genParPt_ = 0;
   genParEta_ = 0;
   genParPhi_ = 0;
   genParM_ = 0;
   genParQ_ = 0;
   genParId_ = 0;
   genParSt_ = 0;
   genMomParId_ = 0;
   genParIndex_ = 0;
   genNMo_ = 0;
   genNDa_ = 0;
   genMo1_ = 0;
   genMo2_ = 0;
   genDa1_ = 0;
   genDa2_ = 0;
   genJetE_ = 0;
   genJetPt_ = 0;
   genJetEta_ = 0;
   genJetPhi_ = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("EvtInfo_EventNum", &EvtInfo_EventNum, &b_EvtInfo_EventNum);
   fChain->SetBranchAddress("EvtInfo_RunNum", &EvtInfo_RunNum, &b_EvtInfo_RunNum);
   fChain->SetBranchAddress("EvtInfo_LumiSection", &EvtInfo_LumiSection, &b_EvtInfo_LumiSection);
   fChain->SetBranchAddress("EvtInfo_BunchXing", &EvtInfo_BunchXing, &b_EvtInfo_BunchXing);
   fChain->SetBranchAddress("EvtInfo_NumVtx", &EvtInfo_NumVtx, &b_EvtInfo_NumVtx);
   fChain->SetBranchAddress("EvtInfo_VertexX_", &EvtInfo_VertexX_, &b_EvtInfo_VertexX_);
   fChain->SetBranchAddress("EvtInfo_VertexY_", &EvtInfo_VertexY_, &b_EvtInfo_VertexY_);
   fChain->SetBranchAddress("EvtInfo_VertexZ_", &EvtInfo_VertexZ_, &b_EvtInfo_VertexZ_);
   fChain->SetBranchAddress("ptHat_", &ptHat_, &b_ptHat_);
   fChain->SetBranchAddress("mcWeight_", &mcWeight_, &b_mcWeight_);
   fChain->SetBranchAddress("genParE_", &genParE_, &b_genParE_);
   fChain->SetBranchAddress("genParPt_", &genParPt_, &b_genParPt_);
   fChain->SetBranchAddress("genParEta_", &genParEta_, &b_genParEta_);
   fChain->SetBranchAddress("genParPhi_", &genParPhi_, &b_genParPhi_);
   fChain->SetBranchAddress("genParM_", &genParM_, &b_genParM_);
   fChain->SetBranchAddress("genParQ_", &genParQ_, &b_genParQ_);
   fChain->SetBranchAddress("genParId_", &genParId_, &b_genParId_);
   fChain->SetBranchAddress("genParSt_", &genParSt_, &b_genParSt_);
   fChain->SetBranchAddress("genMomParId_", &genMomParId_, &b_genMomParId_);
   fChain->SetBranchAddress("genParIndex_", &genParIndex_, &b_genParIndex_);
   fChain->SetBranchAddress("genNMo_", &genNMo_, &b_genNMo_);
   fChain->SetBranchAddress("genNDa_", &genNDa_, &b_genNDa_);
   fChain->SetBranchAddress("genMo1_", &genMo1_, &b_genMo1_);
   fChain->SetBranchAddress("genMo2_", &genMo2_, &b_genMo2_);
   fChain->SetBranchAddress("genDa1_", &genDa1_, &b_genDa1_);
   fChain->SetBranchAddress("genDa2_", &genDa2_, &b_genDa2_);
   fChain->SetBranchAddress("genJetE_", &genJetE_, &b_genJetE_);
   fChain->SetBranchAddress("genJetPt_", &genJetPt_, &b_genJetPt_);
   fChain->SetBranchAddress("genJetEta_", &genJetEta_, &b_genJetEta_);
   fChain->SetBranchAddress("genJetPhi_", &genJetPhi_, &b_genJetPhi_);
   Notify();
}

Bool_t simple::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void simple::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t simple::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef simple_cxx
