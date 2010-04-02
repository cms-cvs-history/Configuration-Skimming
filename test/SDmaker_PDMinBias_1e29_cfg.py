import FWCore.ParameterSet.Config as cms


process = cms.Process("makeSD")

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision:$'),
    annotation = cms.untracked.string('SD and central skims'),
    name = cms.untracked.string('$Source:$')
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(30000)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/FA628320-C73D-DF11-A9ED-001D09F24D4E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/E0E03E54-C43D-DF11-904F-0030487CD184.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/D69A20E4-BB3D-DF11-B52F-001D09F24498.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/C2B28168-CD3D-DF11-8C52-001D09F24682.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/B659CB27-C03D-DF11-ABC6-001D09F24FEC.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/B40373C0-B93D-DF11-A994-0030487CD7E0.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/A67AC67F-CF3D-DF11-B1CA-0030487C778E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/9EEF901E-C73D-DF11-A36F-001D09F2960F.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/9EEF7D43-C93D-DF11-A60E-0030487CD6E6.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/9A42677C-C13D-DF11-AFD1-001D09F27067.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/94A8F7F6-C93D-DF11-888F-001D09F295FB.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/86447753-C43D-DF11-8F09-0030487C912E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/82BB90B4-CC3D-DF11-9286-001617C3B5F4.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/74AACD82-CC3D-DF11-8D77-001617C3B654.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/5E196245-BD3D-DF11-850F-001D09F2AF96.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/5A5E82E5-BB3D-DF11-89C3-001D09F2423B.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/4E807303-D33D-DF11-A2FC-000423D8F63C.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/46D91E9A-D13D-DF11-B534-0030487A1FEC.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/3E853BBD-C03D-DF11-A381-000423D60FF6.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/347B85B1-BE3D-DF11-97C7-0019B9F4A1D7.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/2C53D199-D83D-DF11-B152-0030487CD16E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/2C133F53-C43D-DF11-86F5-0030487D05B0.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/14F94E22-C23D-DF11-9D68-001617E30D4A.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/1456AA7F-CF3D-DF11-A6C4-0030487CAF0E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/513/08F27A7E-CF3D-DF11-9189-000423D98EC4.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/512/AAE2FE60-B83D-DF11-A282-0030487A18F2.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/512/0889ABCC-B43D-DF11-8251-001617DBD5AC.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/511/B019AB68-B33D-DF11-B708-0030487CD7B4.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/506/EC9342C5-9F3D-DF11-B291-0030487A18F2.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/504/1836E273-923D-DF11-B86E-0030487CD840.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/494/04535CCE-8C3D-DF11-91D3-0030487CAEAC.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/492/AA24AF7F-7F3D-DF11-8B8A-0030487CD76A.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/487/64E88AE8-803D-DF11-B2D5-0030487CD6B4.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/485/F450545B-6F3D-DF11-94F9-0030487CD7E0.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/485/E810220D-693D-DF11-9062-00304879FA4A.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/485/B474065C-6F3D-DF11-B08F-0030487CD6F2.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/485/825BAB4D-743D-DF11-9BC3-0030487CAEAC.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/485/66951330-6B3D-DF11-84BF-001617DBD556.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/485/4AE8133D-6D3D-DF11-8573-0030487A1884.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/484/0EF211A4-673D-DF11-8C81-0030487CD17C.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/482/BE7BC81B-643D-DF11-B92A-0030487C8E00.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/482/68F3F2EF-663D-DF11-9DD5-0030487D0D3A.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/482/5CCFD9EA-5F3D-DF11-8D08-0030487CD16E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/482/1098610C-623D-DF11-9D3A-0030487CD77E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/481/E29587DB-563D-DF11-9EFB-0030487A3C92.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/481/D2A87A57-583D-DF11-AE0E-0030487A322E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/481/7222538E-5C3D-DF11-89D0-0030487CD716.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/481/54663415-563D-DF11-96EA-0030487CAEAC.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/481/30FC64E0-563D-DF11-8E7D-0030487A195C.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/481/24DE3093-573D-DF11-8DB0-0030487C90D4.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/481/22B15356-5A3D-DF11-A1D5-0030487C90C4.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/F6C16FA8-4D3D-DF11-B15A-000423D98BC4.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/F428D2F5-4C3D-DF11-94B0-0030487CAF0E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/F0DD0341-4C3D-DF11-8229-000423D98EC8.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/E2A5EC99-503D-DF11-9E24-0030487C912E.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/CA8212C4-4F3D-DF11-8CA5-0030487C5CFA.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/B87CA1AE-4D3D-DF11-A02D-000423D98AF0.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/AE13DF14-4F3D-DF11-B400-000423D98AF0.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/A2950560-4E3D-DF11-9802-0030487CAEAC.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/52557FE6-513D-DF11-8DA6-001D09F2525D.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/36F1188D-503D-DF11-B9BD-0030487CD704.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/2E151BA9-4D3D-DF11-9A63-00151796CD80.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/0EA92561-4E3D-DF11-820F-0030487CD6B4.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/0C1936C3-4F3D-DF11-BE7F-0030487A1884.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/0A293BAF-503D-DF11-81C3-001D09F29524.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/478/0488FE14-563D-DF11-87F5-0030487CD6B4.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/477/FEA61727-303D-DF11-8145-001617C3B69C.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/477/FE659501-463D-DF11-8F83-000423D987FC.root',
        '/store/data/Commissioning10/MinimumBias/RECO/v7/000/132/477/F8A47D0D-413D-DF11-BE73-0030487A17B8.root',
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
#process.Mu_1e29.HLTPaths = ("HLT_L2Mu0","HLT_L2Mu3","HLT_L2Mu5")
process.Mu_1e29.HLTPaths = ("HLT_L2Mu0_NoVertex","HLT_Mu3","HLT_Mu5")
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
