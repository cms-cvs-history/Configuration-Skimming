import FWCore.ParameterSet.Config as cms


process = cms.Process("makeSD")

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.4 $'),
    annotation = cms.untracked.string('SD and central skims'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/Skimming/test/SDmaker_6SD_PDMinBias_1e28_cfg.py,v $')
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50)
)

process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.GeometryExtended_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.EventContent.EventContent_cff')
process.GlobalTag.globaltag = "GR10_P_V4::All"  


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#       '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/447/E4FEDCAA-F149-DF11-ACF0-001D09F28E80.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/447/A8288196-F649-DF11-8B67-000423D6CA42.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/447/6C10F958-F249-DF11-97F8-001D09F29114.root'

#      '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/F64EA0B7-5149-DF11-8110-0019B9F72D71.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/D6A60EA5-4F49-DF11-8769-000423D8FA38.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/96C96FFB-4B49-DF11-8A6A-0030487CD76A.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/8E4D5E46-4B49-DF11-9B15-000423D944F0.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/8CC8B7C2-4C49-DF11-B918-001617DBD556.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/846B9C90-4F49-DF11-B8DB-000423D98C20.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/7C3D53CC-4C49-DF11-B419-001617DBD230.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/6C608494-4F49-DF11-A9C3-000423D99660.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/5C74849A-4A49-DF11-91BB-001D09F23174.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/48240546-5049-DF11-828E-000423D6CA42.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/2EBC4BF4-4B49-DF11-BD6A-0030487CD7CA.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/245B50C8-4C49-DF11-A7E4-0016177CA778.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/10957B54-6049-DF11-8EF9-0030487CD812.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/324/022658BD-4C49-DF11-BCBE-000423D6006E.root'
 
#      '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/036/BEC8D912-4C46-DF11-A3E3-0030487CD77E.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/036/86465D33-4E46-DF11-8207-001D09F29849.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/036/3E93FD33-4E46-DF11-BC6D-001D09F29619.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/036/30325801-4A46-DF11-9D74-0030487C60AE.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/036/22B8B42F-4746-DF11-BE73-001D09F2462D.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/036/0C3181B1-4A46-DF11-A70D-001617C3B76A.root'
 
#     '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/965/F4160693-AE44-DF11-96AF-001D09F282F5.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/965/F01083BE-AB44-DF11-A867-0030487CD906.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/965/BE2DEDE4-AD44-DF11-A324-001D09F25438.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/965/921B6278-AC44-DF11-A67E-001D09F24D67.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/965/603E0E32-AB44-DF11-8933-0030487CD812.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/965/5AE5EE96-B544-DF11-BB0F-0030487CD162.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/965/44D54496-AE44-DF11-B3A2-001D09F2932B.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/965/32D18EE5-AD44-DF11-A32B-001D09F23D1D.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/965/1090F991-AE44-DF11-85E9-001D09F297EF.root'
   
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/850/12123085-2043-DF11-A289-0030487C778E.root'

#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/546/EC7D81A5-5E3E-DF11-822A-0019B9F70468.root',


        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/132/514/EC4F1421-E33D-DF11-B07D-0030487C6088.root'

#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/FA628320-C73D-DF11-A9ED-001D09F24D4E.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/E0E03E54-C43D-DF11-904F-0030487CD184.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/D69A20E4-BB3D-DF11-B52F-001D09F24498.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/C2B28168-CD3D-DF11-8C52-001D09F24682.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/B659CB27-C03D-DF11-ABC6-001D09F24FEC.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/B40373C0-B93D-DF11-A994-0030487CD7E0.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/A67AC67F-CF3D-DF11-B1CA-0030487C778E.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/9EEF901E-C73D-DF11-A36F-001D09F2960F.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/9EEF7D43-C93D-DF11-A60E-0030487CD6E6.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/9A42677C-C13D-DF11-AFD1-001D09F27067.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/94A8F7F6-C93D-DF11-888F-001D09F295FB.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/86447753-C43D-DF11-8F09-0030487C912E.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/82BB90B4-CC3D-DF11-9286-001617C3B5F4.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/74AACD82-CC3D-DF11-8D77-001617C3B654.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/5E196245-BD3D-DF11-850F-001D09F2AF96.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/5A5E82E5-BB3D-DF11-89C3-001D09F2423B.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/4E807303-D33D-DF11-A2FC-000423D8F63C.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/46D91E9A-D13D-DF11-B534-0030487A1FEC.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/3E853BBD-C03D-DF11-A381-000423D60FF6.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/347B85B1-BE3D-DF11-97C7-0019B9F4A1D7.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/2C53D199-D83D-DF11-B152-0030487CD16E.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/2C133F53-C43D-DF11-86F5-0030487D05B0.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/14F94E22-C23D-DF11-9D68-001617E30D4A.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/1456AA7F-CF3D-DF11-A6C4-0030487CAF0E.root',
#       '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/08F27A7E-CF3D-DF11-9189-000423D98EC4.root'

#       '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/E0DA54C8-964B-DF11-80F6-0030487CD7C6.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/DA6F9B16-964B-DF11-89DF-000423D99614.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/D81E4B7C-974B-DF11-AD43-0030487CD718.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/AE58D015-964B-DF11-9B6B-0030487CD840.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/6864B8B5-A24B-DF11-AB97-0030487A3C92.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/6250317B-974B-DF11-8DEE-0030487CD76A.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/46272118-964B-DF11-9A6C-0030487CAF5E.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/44D14EA8-994B-DF11-B046-000423D94908.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/24523F7C-974B-DF11-B9C2-0030487CD6DA.root',
#        '/store/data/Commissioning10/MinimumBias/RECO/v8/000/133/516/126592C9-964B-DF11-BD57-0030487C7392.root'



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
#"HLT_L2Mu0", excluded to try to match the /cdaq/physics/firstCollisions10/v2.0/HLT_7TeV/V5 table
#"HLT_L2Mu3", excluded to try to match the /cdaq/physics/firstCollisions10/v2.0/HLT_7TeV/V5 table
#"HLT_L2Mu5", never present
"HLT_L1Mu20",
"HLT_L2Mu9",
"HLT_L2Mu11",
"HLT_L1Mu14_L1SingleEG10",
"HLT_L1Mu14_L1SingleJet6U",
"HLT_L1Mu14_L1ETM30",
#"HLT_L2DoubleMu0", excluded to try to match the /cdaq/physics/firstCollisions10/v2.0/HLT_7TeV/V5 table
"HLT_L1DoubleMuOpen",
"HLT_DoubleMu0",
"HLT_DoubleMu3",
"HLT_Mu3",
"HLT_Mu5",
"HLT_Mu9",
"HLT_IsoMu3",
"HLT_Mu0_L1MuOpen", #ok
"HLT_Mu0_Track0_Jpsi", #ok
"HLT_Mu3_L1MuOpen", #ok
"HLT_Mu3_Track0_Jpsi", #ok 
"HLT_Mu5_L1MuOpen", #ok
"HLT_Mu5_Track0_Jpsi", #ok
#"HLT_Mu0_L2Mu0", excluded to try to match the /cdaq/physics/firstCollisions10/v2.0/HLT_7TeV/V5 table
#"HLT_Mu3_L2Mu0", excluded to try to match the /cdaq/physics/firstCollisions10/v2.0/HLT_7TeV/V5 table
#"HLT_Mu5_L2Mu0" excluded to try to match the /cdaq/physics/firstCollisions10/v2.0/HLT_7TeV/V5 table
)
#process.Mu_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
process.Mu_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
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
#"HLT_DoublePhoton4_Jpsi_L1R", excluded to try to match the /cdaq/physics/firstCollisions10/v2.0/HLT_7TeV/V5 table
#"HLT_DoublePhoton4_Upsilon_L1R", excluded to try to match the /cdaq/physics/firstCollisions10/v2.0/HLT_7TeV/V5 table
#"HLT_DoublePhoton4_eeRes_L1R", excluded to try to match the /cdaq/physics/firstCollisions10/v2.0/HLT_7TeV/V5 table
"HLT_DoublePhoton5_Jpsi_L1R",
"HLT_DoublePhoton5_Upsilon_L1R",
#"HLT_DoublePhoton5_L1R", excluded to try to match the /cdaq/physics/firstCollisions10/v2.0/HLT_7TeV/V5 table
"HLT_DoublePhoton5_eeRes_L1R", #added to try to match the /cdaq/physics/firstCollisions10/v2.0/HLT_7TeV/V5 table
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
#process.EG_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
process.EG_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
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
