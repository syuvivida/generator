# Auto generated configuration file
# using: 
# Revision: 1.381.2.7 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/EightTeV/Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_tauola_cff.py --step GEN --beamspot Realistic8TeVCollision --conditions START52_V9::All --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --datatier GEN -n -1 --python_filename=Temp_Hadronizer_5498_1.py --filein root://eoscms//eos/cms//store/lhe/5498/DY1JetsToLL_M-50_8TeV-madgraph_10001.lhe --no_output --no_exec
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
options.parseArguments()

process = cms.Process('ANA')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Input source for LHE source
#process.source = cms.Source("LHESource",
#    fileNames = cms.untracked.vstring(options.inputFiles)
#     fileNames = cms.untracked.vstring('file:DYJetsToLL_PtZ-100_TuneZ2_8TeV_ext-madgraph-tarball_487251988.lhe',
#				       'file:DYJetsToLL_PtZ-100_TuneZ2_8TeV_ext-madgraph-tarball_487252016.lhe'
#				       )
			    
#)

process.source = cms.Source("PoolSource",
			                                fileNames  = cms.untracked.vstring(options.inputFiles)
			                                )



# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.7 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/EightTeV/Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_tauola_cff.py nevts:-1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START52_V9::All', '')

process.generator = cms.EDFilter("Pythia6HadronizerFilter",
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            UseTauolaPolarization = cms.bool(True),
            InputCards = cms.PSet(
                mdtau = cms.int32(0),
                pjak2 = cms.int32(0),
                pjak1 = cms.int32(0)
            )
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    UseExternalGenerators = cms.untracked.bool(True),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),
    jetMatching = cms.untracked.PSet(
        MEMAIN_showerkt = cms.double(0),
        MEMAIN_maxjets = cms.int32(-1),
        MEMAIN_minjets = cms.int32(-1),
        MEMAIN_qcut = cms.double(-1),
        MEMAIN_excres = cms.string(''),
        MEMAIN_etaclmax = cms.double(-1),
        MEMAIN_nqmatch = cms.int32(5),
        outTree_flag = cms.int32(0),
        scheme = cms.string('Madgraph'),
        mode = cms.string('auto')
    ),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.921 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.227 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model'),
        processParameters = cms.vstring('MSEL=0         ! User defined processes', 
            'PMAS(5,1)=4.8   ! b quark mass', 
            'PMAS(6,1)=172.5 ! t quark mass', 
            'MSTJ(1)=1       ! Fragmentation/hadronization on or off', 
            'MSTP(61)=1      ! Parton showering on or off'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('GEN.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)


process.dummy = cms.EDAnalyzer("GenXSecAnalyzer")

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)
process.ana = cms.Path(process.dummy)

# Schedule definition
process.schedule = cms.Schedule(process.ana)

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
