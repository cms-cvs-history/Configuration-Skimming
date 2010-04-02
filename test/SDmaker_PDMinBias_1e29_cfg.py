import FWCore.ParameterSet.Config as cms


process = cms.Process("makeSD")

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('SD and central skims'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/Skimming/test/SDmaker_PDMinBias_1e29_cfg.py,v $')
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(30000)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/FA628320-C73D-DF11-A9ED-001D09F24D4E.root',
#        '/store/relval/CMSSW_3_5_4/RelValZTT/GEN-SIM-RECO/START3X_V24-v1/0004/020492F1-2C2C-DF11-AF77-002618943826.root'
        )
)

process.MessageLogger = cms.Service("MessageLogger",
    detailedInfo = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO')
    ),
    critical = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
    ),
    debugModules = cms.untracked.vstring('*'),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING'),
        WARNING = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        noLineBreaks = cms.untracked.bool(True)
    ),
    destinations = cms.untracked.vstring('detailedInfo', 
        'critical', 
        'cout')
)

import HLTrigger.HLTfilters.hltHighLevelDev_cfi

process.Jet_1e29 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.Jet_1e29.HLTPaths = ("HLT_L1Jet6U","HLT_Jet15U","HLT_Jet30U")
process.Jet_1e29.HLTPathsPrescales  = cms.vuint32(1,1,1)
process.Jet_1e29.HLTOverallPrescale = cms.uint32(1)
process.Jet_1e29.andOr = True

process.filterSdJet_1e29 = cms.Path(process.Jet_1e29)



process.EGamma_1e29 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.EGamma_1e29.HLTPaths = ("HLT_L1SingleEG5","HLT_L1SingleEG8")
process.EGamma_1e29.HLTPathsPrescales  = cms.vuint32(1,1)
process.EGamma_1e29.HLTOverallPrescale = cms.uint32(1)
process.EGamma_1e29.andOr = True

process.filterSdEGamma_1e29 = cms.Path(process.EGamma_1e29)



process.Mu_1e29 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.Mu_1e29.HLTPaths = ("HLT_L2Mu0","HLT_L2Mu3","HLT_L2Mu5")
#process.Mu_1e29.HLTPaths = ("HLT_L2Mu0_NoVertex","HLT_Mu3","HLT_Mu5")
process.Mu_1e29.HLTPathsPrescales  = cms.vuint32(1,1,1)
process.Mu_1e29.HLTOverallPrescale = cms.uint32(1)
process.Mu_1e29.andOr = True

process.filterSdMu_1e29 = cms.Path(process.Mu_1e29)



process.DiJetAve_1e29 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.DiJetAve_1e29.HLTPaths = ("HLT_DiJetAve15U_8E29","HLT_DiJetAve30U_8E29")
process.DiJetAve_1e29.HLTPathsPrescales  = cms.vuint32(1,1)
process.DiJetAve_1e29.HLTOverallPrescale = cms.uint32(1)
process.DiJetAve_1e29.andOr = True

process.filterCsDiJetAve_1e29 = cms.Path(process.DiJetAve_1e29)



#process.load("Configuration.Skimming.filterSdJet_1e29_cfi")
#process.load("Configuration.Skimming.filterSdMu_1e29_cfi")
#process.load("Configuration.Skimming.filterSdEGamma_1e29_cfi")
#process.load('Configuration.Skimming.filterCsDiJetAve_1e29_cfi')

process.outputSdEGamma = cms.OutputModule("PoolOutputModule",
                               SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterSdEGamma_1e29')),                               
                               dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('SD_EGamma')),
                               fileName = cms.untracked.string('SD_EGamma_1e29.root')
                               )

process.outputSdMu = cms.OutputModule("PoolOutputModule",
                               SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterSdMu_1e29')),                               
                               dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('SD_Mu')),
                               fileName = cms.untracked.string('SD_Mu_1e29.root')
                               )

process.outputSdJet = cms.OutputModule("PoolOutputModule",
                               SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterSdJet_1e29')),                               
                               dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('SD_Jet')),
                               fileName = cms.untracked.string('SD_Jet_1e29.root')
                               )

process.outputCsDiJet = cms.OutputModule("PoolOutputModule",
                                         dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('USER'),
        filterName = cms.untracked.string('CS_DiJetAve')),
       outputCommands = cms.untracked.vstring(
        'drop *',
        #------- CaloJet collections ------
        'keep recoCaloJets_kt4CaloJets_*_*',
        'keep recoCaloJets_kt6CaloJets_*_*',
        'keep recoCaloJets_ak5CaloJets_*_*',
        'keep recoCaloJets_ak7CaloJets_*_*',
        'keep recoCaloJets_iterativeCone5CaloJets_*_*',
        #------- CaloJet ID ---------------
        'keep *_kt4JetID_*_*',
        'keep *_kt6JetID_*_*',
        'keep *_ak5JetID_*_*',
        'keep *_ak7JetID_*_*',
        'keep *_ic5JetID_*_*', 
        #------- PFJet collections ------  
        'keep recoPFJets_kt4PFJets_*_*',
        'keep recoPFJets_kt6PFJets_*_*',
        'keep recoPFJets_ak5PFJets_*_*',
        'keep recoPFJets_ak7PFJets_*_*',
        'keep recoPFJets_iterativeCone5PFJets_*_*',
        #------- JPTJet collections ------
        #'keep *_ak5JPTJets_*_*',
        #'keep *_iterativeCone5JPTJets_*_*',
        #------- Trigger collections ------
        'keep edmTriggerResults_TriggerResults_*_*',
        'keep *_hltTriggerSummaryAOD_*_*',
        'keep L1GlobalTriggerObjectMapRecord_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_*_*_*',
        #------- Tracks collection --------
        'keep recoTracks_generalTracks_*_*',
        #------- CaloTower collection -----
        'keep *_towerMaker_*_*',
        #------- Various collections ------
        'keep *_EventAuxilary_*_*',
        'keep *_offlinePrimaryVertices_*_*',
        'keep *_hcalnoise_*_*',
        #------- MET collections ----------
        'keep *_metHO_*_*',
        'keep *_metNoHF_*_*',
        'keep *_metNoHFHO_*_*', 
        'keep *_met_*_*'),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterCsDiJetAve_1e29')), 
    fileName = cms.untracked.string('JetAOD_DiJetAve.root')
)



process.this_is_the_end = cms.EndPath(process.outputSdEGamma+process.outputSdMu+process.outputSdJet+process.outputCsDiJet)
