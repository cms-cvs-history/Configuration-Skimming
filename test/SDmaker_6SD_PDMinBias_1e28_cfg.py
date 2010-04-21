import FWCore.ParameterSet.Config as cms


process = cms.Process("makeSD")

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.3 $'),
    annotation = cms.untracked.string('SD and central skims'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/Skimming/test/SDmaker_6SD_PDMinBias_1e28_cfg.py,v $')
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.GeometryExtended_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.EventContent.EventContent_cff')
process.GlobalTag.globaltag = "GR10_P_V4::All"  


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/E0DA54C8-964B-DF11-80F6-0030487CD7C6.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/DA6F9B16-964B-DF11-89DF-000423D99614.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/D81E4B7C-974B-DF11-AD43-0030487CD718.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/AE58D015-964B-DF11-9B6B-0030487CD840.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/6864B8B5-A24B-DF11-AB97-0030487A3C92.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/6250317B-974B-DF11-8DEE-0030487CD76A.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/46272118-964B-DF11-9A6C-0030487CAF5E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/44D14EA8-994B-DF11-B046-000423D94908.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/24523F7C-974B-DF11-B9C2-0030487CD6DA.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/126592C9-964B-DF11-BD57-0030487C7392.root'



        )
)

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
process.EG_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
process.EG_1e28.HLTOverallPrescale = cms.uint32(1)
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
