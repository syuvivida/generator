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

readFiles = cms.untracked.vstring()

process.source = cms.Source("LHESource",firstEvent = cms.untracked.uint32(0),skipEvents = cms.untracked.uint32(0),
    fileNames =readFiles

)

readFiles.extend( [
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/401_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/402_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/403_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/404_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/405_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/406_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/407_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/408_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/409_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/410_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/411_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/412_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/413_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/414_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/415_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/416_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/417_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/418_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/419_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/420_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/421_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/422_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/423_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/424_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/425_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/426_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/427_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/428_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/429_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/430_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/431_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/432_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/433_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/434_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/435_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/436_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/437_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/438_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/439_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/440_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/441_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/442_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/443_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/444_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/445_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/446_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/447_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/448_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/449_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/450_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/451_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/452_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/453_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/454_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/455_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/456_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/457_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/458_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/459_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/460_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/461_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/462_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/463_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/464_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/465_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/466_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/467_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/468_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/469_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/470_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/471_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/472_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/473_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/474_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/475_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/476_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/477_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/478_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/479_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/480_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/481_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/482_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/483_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/484_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/485_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/486_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/487_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/488_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/489_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/490_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/491_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/492_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/493_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/494_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/495_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/496_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/497_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/498_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/499_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/500_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/501_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/502_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/505_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/506_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/507_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/508_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/510_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/511_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/512_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/513_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/514_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/515_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/516_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/517_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/518_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/521_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/522_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/523_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/524_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/526_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/528_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/529_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/530_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/531_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/533_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/534_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/535_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/536_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/537_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/538_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/540_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/541_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/543_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/544_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/545_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/546_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/547_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/549_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/550_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/551_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/552_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/554_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/555_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/557_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/558_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/559_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/560_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/561_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/562_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/563_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/564_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/565_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/566_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/567_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/568_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/570_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/571_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/573_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/574_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/575_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/577_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/578_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/579_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/580_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/581_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/582_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/583_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/584_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/585_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/586_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/587_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/588_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/589_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/590_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/591_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/592_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/593_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/595_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/596_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/597_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/598_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/599_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/600_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/601_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/602_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/603_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/604_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/605_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/606_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/608_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/609_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/611_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/612_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/613_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/614_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/615_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/616_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/617_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/618_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/619_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/620_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/621_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/622_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/623_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/624_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/625_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/626_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/627_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/628_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/629_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/630_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/631_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/632_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/633_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/634_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/635_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/636_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/637_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/638_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/639_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/640_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/641_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/643_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/645_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/646_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/648_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/649_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/650_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/651_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/652_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/655_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/656_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/657_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/658_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/661_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/662_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/663_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/664_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/665_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/666_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/667_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/668_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/669_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/671_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/672_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/673_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/674_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/675_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/676_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/677_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/678_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/681_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/683_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/686_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/687_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/690_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/693_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/695_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/696_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/701_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/702_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/703_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/704_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/705_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/706_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/707_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/708_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/709_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/710_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/711_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/712_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/713_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/714_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/715_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/717_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/718_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/719_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/720_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/721_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/722_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/723_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/724_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/725_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/726_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/727_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/729_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/730_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/731_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/732_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/733_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/735_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/737_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/738_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/739_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/740_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/741_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/743_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/744_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/745_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/747_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/748_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/749_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/751_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/752_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/754_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/757_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/759_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/760_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/761_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/762_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/765_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/766_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/767_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/768_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/770_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/771_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/772_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/773_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/774_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/775_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/777_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/780_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/781_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/782_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/783_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/784_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/785_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/787_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/788_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/789_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/790_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/791_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/793_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/795_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/796_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/797_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/798_unweighted_events.lhe',
'file:/data4/syu/madgraph_lhe/xqcut5_lhe_files/799_unweighted_events.lhe'
	
	]
		  );




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
				   cms.string('/data4/syu/madgraph_lhe/zj_zjj_xqcut5_qcut10.root'))

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

