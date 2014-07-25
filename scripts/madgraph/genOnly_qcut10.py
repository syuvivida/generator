import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.MessageLogger.cerr.FwkReport.reportEvery = 1000


# Input source
process.maxEvents = cms.untracked.PSet(
	input = cms.untracked.int32(-1)
	)


process.source = cms.Source("LHESource",firstEvent = cms.untracked.uint32(0),skipEvents = cms.untracked.uint32(0),
			        fileNames = cms.untracked.vstring(
	'INPUT'
	)
)

process.options = cms.untracked.PSet(
	)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('$Revision: 1.381.2.2 $'),
	annotation = cms.untracked.string('Configuration/GenProduction/python/EightTeV/file:/tmp/ymtzeng/ttbar.root'),
	name = cms.untracked.string('PyReleaseValidation')
	)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
					splitLevel = cms.untracked.int32(0),
					eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
					outputCommands = process.RAWSIMEventContent.outputCommands,
					fileName = cms.untracked.string('sim.root'),
					dataset = cms.untracked.PSet(
	filterName = cms.untracked.string(''),
	dataTier = cms.untracked.string('GEN-SIM')
	),
					SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
	)
					)

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'START53_V7A::All'

process.generator = cms.EDFilter("Pythia6HadronizerFilter",
    jetMatching = cms.untracked.PSet(
        MEMAIN_showerkt = cms.double(0),
        MEMAIN_nqmatch = cms.int32(5),
        MEMAIN_minjets = cms.int32(0),
        MEMAIN_maxjets = cms.int32(2),
        MEMAIN_qcut = cms.double(10.0),
        MEMAIN_excres = cms.string(''),
        MEMAIN_etaclmax = cms.double(5.0),
        outTree_flag = cms.int32(0),
        scheme = cms.string('Madgraph'),
        mode = cms.string('auto')
    ),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    displayPythiaCards   = cms.untracked.bool(True),				    comEnergy = cms.double(7000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
	pythiaUESettings = cms.vstring(
	'MSTU(21)=1     ! Check on possible errors during program execution', 
	'MSTJ(22)=2     ! Decay those unstable particles', 
	'PARJ(71)=10 .  ! for which ctau  10 mm', 
	'MSTP(33)=0     ! no K factors in hard cross sections', 
	'MSTP(2)=1      ! which order running alphaS', 
	'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
	'MSTP(52)=2     ! work with LHAPDF',

	'PARP(82)=1.832 ! pt cutoff for multiparton interactions', 
	'PARP(89)=1800. ! sqrts for which PARP82 is set', 
	'PARP(90)=0.275 ! Multiple interactions: rescaling power', 

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
	'MSTP(82)=4     ! Defines the multi-parton model', 
	),
	processParameters = cms.vstring(
            'MSTJ(1)=1       ! Fragmentation/hadronization on or off',
	    ),
        parameterSets = cms.vstring('pythiaUESettings', 'processParameters')                                )

)

baseJetSel = cms.PSet(
  Jets=cms.InputTag("selectedPatJetsPFlow")
)

from DelPanj.TreeMaker.eSel2012HZZ_cff import *
from DelPanj.TreeMaker.muSel2012HZZ_cff import *

process.tree = cms.EDAnalyzer(
	'TreeMaker',
	fillPUweightInfo_ = cms.bool(False),
	fillEventInfo_ = cms.bool(True),
	fillGenInfo_   = cms.bool(True),
	fillMuonInfo_  = cms.bool(False),
	fillElecInfo_  = cms.bool(False),
	fillElecIsoInfo_ = cms.bool(False),
	fillJetInfo_   = cms.bool(False),
	fillMetInfo_   = cms.bool(False),
	fillTrigInfo_  = cms.bool(False),
	fillPhotInfo_  = cms.bool(False),
	fillZJetPlant_ = cms.bool(False),
	genPartLabel=cms.InputTag("genParticles"),
	patMuons=cms.InputTag("userDataSelectedMuons"),
	patElectrons = cms.InputTag("userDataSelectedElectrons"),
        e2012IDSet  =  eSel2012HZZ,
        mu2012IDSet = muSel2012HZZ,
        eleRhoIso = cms.InputTag("kt6PFJetsForIso","rho"),
        muoRhoIso = cms.InputTag("kt6PFJetsCentralNeutral", "rho"),
	patMet=cms.InputTag("patMETs"),
	beamSpotLabel=cms.InputTag("offlineBeamSpot"),
	patJetPfAk05 = baseJetSel,
	outFileName=cms.string('outputFileName.root')
	)



process.TFileService = cms.Service("TFileService", fileName =
				   cms.string('zj_zjj_xqcut5_qcut10.root'))

process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
#process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)
process.end_ana     = cms.Path(process.tree)


# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.end_ana)
#process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

