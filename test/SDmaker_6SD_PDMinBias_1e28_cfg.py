import FWCore.ParameterSet.Config as cms


process = cms.Process("makeSD")

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.7 $'),
    annotation = cms.untracked.string('SD and central skims'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/Skimming/test/SDmaker_6SD_PDMinBias_1e28_cfg.py,v $')
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.GeometryExtended_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.EventContent.EventContent_cff')
process.GlobalTag.globaltag = "GR10_P_V4::All"  


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/528/867BB35A-2B3E-DF11-AC1D-000423D99996.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/526/5491FB8D-213E-DF11-B3A5-000423D6006E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/524/6A6E09B5-1C3E-DF11-BEA5-0030487CD17C.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/523/0E6FF7ED-143E-DF11-98E6-000423D99BF2.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/521/306927B4-023E-DF11-B2C3-000423D98BE8.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/519/E431D7E8-F13D-DF11-AE5A-0030487CAF0E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/514/EC4F1421-E33D-DF11-B07D-0030487C6088.root'
        )
)
process.source.inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")

#process.MessageLogger = cms.Service("MessageLogger",
#    detailedInfo = cms.untracked.PSet(
#        threshold = cms.untracked.string('INFO')
#    ),
#    critical = cms.untracked.PSet(
#        threshold = cms.untracked.string('ERROR')
#    ),
#    debugModules = cms.untracked.vstring('*')
#    cout = cms.untracked.PSet(
#        threshold = cms.untracked.string('WARNING'),
#        WARNING = cms.untracked.PSet(
#            limit = cms.untracked.int32(0)
#        ),
#        noLineBreaks = cms.untracked.bool(True)
#    )
#    destinations = cms.untracked.vstring('detailedInfo', 
#        'critical', 
#        'cout')
#)
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

import HLTrigger.HLTfilters.hltHighLevelDev_cfi


### JetMETTau SD
process.JetMETTau_1e28 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.JetMETTau_1e28.HLTPaths = (
"HLT_Jet15U",
"HLT_DiJetAve15U_8E29",
"HLT_FwdJet20U",
"HLT_Jet30U", 
"HLT_Jet50U",
"HLT_DiJetAve30U_8E29",
"HLT_QuadJet15U",
"HLT_MET45",
"HLT_MET100",
"HLT_HT100U",
"HLT_SingleLooseIsoTau20",
"HLT_DoubleLooseIsoTau15",
"HLT_DoubleJet15U_ForwardBackward",
"HLT_BTagMu_Jet10U",
"HLT_BTagIP_Jet50U",
"HLT_StoppedHSCP_8E29"
)
process.JetMETTau_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
process.JetMETTau_1e28.HLTOverallPrescale = cms.uint32(1)
process.JetMETTau_1e28.throw = False
process.JetMETTau_1e28.andOr = True

process.filterSdJetMETTau_1e28 = cms.Path(process.JetMETTau_1e28)



### JetMETTauMonitor SD
process.JetMETTauMonitor_1e28 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.JetMETTauMonitor_1e28.HLTPaths = (
"HLT_L1Jet6U",
"HLT_L1MET20",
"HLT_L1SingleCenJet",
"HLT_L1SingleForJet",
"HLT_L1SingleTauJet",
"HLT_L1Jet10U",
"HLT_L1Jet10U_NoBPTX",
"HLT_L1Jet6U_NoBPTX",
"HLT_L1SingleCenJet_NoBPTX",
"HLT_L1SingleForJet_NoBPTX",
"HLT_L1SingleTauJet_NoBPTX"
)
process.JetMETTauMonitor_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1,1)
process.JetMETTauMonitor_1e28.HLTOverallPrescale = cms.uint32(1)
process.JetMETTauMonitor_1e28.throw = False
process.JetMETTauMonitor_1e28.andOr = True

process.filterSdJetMETTauMonitor_1e28 = cms.Path(process.JetMETTauMonitor_1e28)

### MuMonitor SD
process.MuMonitor_1e28 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.MuMonitor_1e28.HLTPaths = (
"HLT_L1MuOpen",
"HLT_L1Mu"
)
process.MuMonitor_1e28.HLTPathsPrescales  = cms.vuint32(1,1)
process.MuMonitor_1e28.HLTOverallPrescale = cms.uint32(1)
process.MuMonitor_1e28.throw = False
process.MuMonitor_1e28.andOr = True

process.filterSdMuMonitor_1e28 = cms.Path(process.MuMonitor_1e28)



### Mu SD
process.Mu_1e28 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.Mu_1e28.HLTPaths = (
"HLT_L2Mu0",
"HLT_L2Mu3",
#"HLT_L2Mu5",
"HLT_L1Mu20",
"HLT_L2Mu9",
"HLT_L2Mu11",
"HLT_L1Mu14_L1SingleEG10",
"HLT_L1Mu14_L1SingleJet6U",
"HLT_L1Mu14_L1ETM30",
"HLT_L2DoubleMu0",
"HLT_L1DoubleMuOpen",
"HLT_DoubleMu0",
"HLT_DoubleMu3",
"HLT_Mu3",
"HLT_Mu5",
"HLT_Mu9",
"HLT_IsoMu3",
"HLT_Mu0_L1MuOpen",
"HLT_Mu0_Track0_Jpsi",
"HLT_Mu3_L1MuOpen",
"HLT_Mu3_Track0_Jpsi",
"HLT_Mu5_L1MuOpen",
"HLT_Mu5_Track0_Jpsi",
"HLT_Mu0_L2Mu0",
"HLT_Mu3_L2Mu0",
"HLT_Mu5_L2Mu0"
)
process.Mu_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
process.Mu_1e28.HLTOverallPrescale = cms.uint32(1)
process.Mu_1e28.throw = False
process.Mu_1e28.andOr = True

process.filterSdMu_1e28 = cms.Path(process.Mu_1e28)


### EGMonitor SD
process.EGMonitor_1e28 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.EGMonitor_1e28.HLTPaths = (
"HLT_L1SingleEG2",
"HLT_L1SingleEG5",
"HLT_L1SingleEG8",
"HLT_L1DoubleEG5",
"HLT_EgammaSuperClusterOnly_L1R",
"HLT_L1SingleEG20_NoBPTX",
"HLT_L1SingleEG2_NoBPTX",
"HLT_L1SingleEG5_NoBPTX"
)
process.EGMonitor_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1)
process.EGMonitor_1e28.HLTOverallPrescale = cms.uint32(1)
process.EGMonitor_1e28.throw = False
process.EGMonitor_1e28.andOr = True

process.filterSdEGMonitor_1e28 = cms.Path(process.EGMonitor_1e28)



### EG SD
process.EG_1e28 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.EG_1e28.HLTPaths = (
"HLT_Photon10_L1R",
"HLT_Photon15_L1R",
"HLT_Photon15_LooseEcalIso_L1R",
"HLT_Photon20_L1R",
"HLT_Photon30_L1R_8E29",
"HLT_DoublePhoton4_Jpsi_L1R",
"HLT_DoublePhoton4_Upsilon_L1R",
"HLT_DoublePhoton4_eeRes_L1R",
"HLT_DoublePhoton5_eeRes_L1R", #added to match the /cdaq/physics/firstCollisions10/v2.0/HLT_7TeV/V5 table
"HLT_DoublePhoton5_Jpsi_L1R",
"HLT_DoublePhoton5_Upsilon_L1R",
"HLT_DoublePhoton5_L1R",
"HLT_DoublePhoton10_L1R",
"HLT_DoubleEle5_SW_L1R",
"HLT_Ele20_LW_L1R",
"HLT_Ele15_SiStrip_L1R",
"HLT_Ele15_SC10_LW_L1R",
"HLT_Ele15_LW_L1R",
"HLT_Ele10_LW_EleId_L1R",
"HLT_Ele10_LW_L1R",
"HLT_Photon15_TrackIso_L1R"
)
process.EG_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
process.EG_1e28.HLTOverallPrescale = cms.uint32(1)
process.EG_1e28.throw = False
process.EG_1e28.andOr = True

process.filterSdEG_1e28 = cms.Path(process.EG_1e28)






process.outputSdJetMETTau = cms.OutputModule("PoolOutputModule",
                                          SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterSdJetMETTau_1e28')),                               
                                          dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('SD_JetMETTau')),
                                          outputCommands = process.RECOEventContent.outputCommands,
                                          fileName = cms.untracked.string('SD_JetMETTau_1e28.root')
                                          )

process.outputSdJetMETTauMonitor = cms.OutputModule("PoolOutputModule",
                                          SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterSdJetMETTauMonitor_1e28')),                               
                                          dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('SD_JetMETTauMonitor')),
                                          outputCommands = process.RECOEventContent.outputCommands,
                                          fileName = cms.untracked.string('SD_JetMETTauMonitor_1e28.root')
                                          )
process.outputSdMuMonitor = cms.OutputModule("PoolOutputModule",
                                          SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterSdMuMonitor_1e28')),                               
                                          dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('SD_MuMonitor')),
                                          outputCommands = process.RECOEventContent.outputCommands,
                                          fileName = cms.untracked.string('SD_MuMonitor_1e28.root')
                                          )

process.outputSdMu = cms.OutputModule("PoolOutputModule",
                                          SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterSdMu_1e28')),                               
                                          dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('SD_Mu')),
                                          outputCommands = process.RECOEventContent.outputCommands,
                                          fileName = cms.untracked.string('SD_Mu_1e28.root')
                                          )
process.outputSdEGMonitor = cms.OutputModule("PoolOutputModule",
                                          SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterSdEGMonitor_1e28')),                               
                                          dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('SD_EGMonitor')),
                                          outputCommands = process.RECOEventContent.outputCommands,
                                          fileName = cms.untracked.string('SD_EGMonitor_1e28.root')
                                          )
process.outputSdEG = cms.OutputModule("PoolOutputModule",
                                          SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterSdEG_1e28')),                               
                                          dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('SD_EG')),
                                          outputCommands = process.RECOEventContent.outputCommands,
                                          fileName = cms.untracked.string('SD_EG_1e28.root')
                                          )




process.this_is_the_end = cms.EndPath(
process.outputSdJetMETTau        +
process.outputSdJetMETTauMonitor +
process.outputSdMuMonitor        +
process.outputSdMu               +
process.outputSdEGMonitor        +
process.outputSdEG               
)
