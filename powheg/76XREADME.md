How to make use of LHEAnalyzer to evaluate the fraction of negative weights

cmsrel CMSSW_7_6_4

cd CMSSW_7_6_4/src/

cmsenv

git cms-addpkg GeneratorInterface/LHEInterface

git cms-merge-topic syuvivida:76X_lheweight_example 

scramv1 b

To run,
cmsRun GeneratorInterface/LHEInterface/test/dumpWeightLHE_cfg.py inputFiles="file:xxx.lhe" outputFile="test.root" maxEvents=-1

### 
In the example GeneratorInterface/LHEInterface/test/WeightLHEAnalyzer.cc, the Z mass distributions are 

plotted and the histograms are filled with either only positive-weighted events or only 

negative-weighted events or all events. 

You could modify this module and add the histograms most useful for your analysis.
