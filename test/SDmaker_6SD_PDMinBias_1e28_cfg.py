import FWCore.ParameterSet.Config as cms


process = cms.Process("makeSD")

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('SD and central skims'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/Skimming/test/SDmaker_6SD_TauCS_PDMinBias_1e28_cfg.py,v $')
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
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/F85204EE-EB40-DF11-8F71-001A64789D1C.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/F80836A2-FF40-DF11-A43E-00E08178C067.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/F65A94F7-4141-DF11-9F4E-003048D47A80.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/F2118BE5-FF40-DF11-B2F0-00E081791865.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/E80DA1CD-0041-DF11-8CE3-0025B3E063A8.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/E6261B1F-EC40-DF11-89F7-00E08178C045.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/E2F3F819-F040-DF11-9B20-00E08178C0F5.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/DA86BDB2-E940-DF11-A3A8-0025B3E063A8.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/D6DB0FEC-FD40-DF11-93FC-003048D46004.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/D4C61300-E940-DF11-A659-003048673EA4.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/D27E9F23-FC40-DF11-92F3-00E08178C067.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/CEDBFF0C-E640-DF11-931F-003048D45FA2.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/CA0525F2-EC40-DF11-948D-0025B31E3C0A.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/C63BB055-EA40-DF11-B401-003048673F8A.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/C4DE0B83-ED40-DF11-BDC6-003048D46110.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/C4A9EF9C-F240-DF11-A5F3-002481E150FC.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/BC865204-EF40-DF11-A1FF-00E0817917E7.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/B84C00C3-ED40-DF11-AE86-00E0817917B9.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/B6FC5BA2-EB40-DF11-AC16-003048D45FEA.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/B62BF913-FE40-DF11-95C0-0015170AE328.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/B0889A04-F240-DF11-BA37-00E081B08BC9.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/ACCAE48C-EB40-DF11-B88F-0025B3E05CE4.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/AC1AA07C-4041-DF11-8F7E-00E081791813.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/A65FBFDC-E640-DF11-9BC5-003048D45FEA.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/A4AF10B5-0041-DF11-B6A0-0025B3E0650E.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/A41D9B67-EC40-DF11-A121-003048D45FA8.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/A2CE75FE-EE40-DF11-A061-003048D4600C.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/A286F3B9-EE40-DF11-8F19-003048D47796.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/A26890AB-E740-DF11-97DC-003048D45FA2.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/9CE0781A-EC40-DF11-A3BD-003048D45FA2.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/9CAF81A9-E940-DF11-A84C-003048D4600C.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/9C70947C-ED40-DF11-825C-003048D47A84.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/9AB2191A-EF40-DF11-B3D4-001A64789DDC.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/98842725-FC40-DF11-BF7E-001A64789DEC.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/98098625-FF40-DF11-8DBA-003048D47A1A.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/94A4A967-E940-DF11-8008-003048D47A1A.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/944D50F8-EF40-DF11-918F-002481E14FCA.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/8A446821-EF40-DF11-9FC1-002481E150FC.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/88F8CF52-EA40-DF11-8D78-003048673F74.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/86871F39-FF40-DF11-BC3C-003048D46004.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/860DED05-3E41-DF11-B4E2-00E08178C181.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/80673EAD-E740-DF11-AE30-0025B3E05CE4.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/709CE2A3-EB40-DF11-9B71-003048D45FD4.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/702A765E-F140-DF11-A66F-002481E14D76.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/700A76F0-FC40-DF11-9BB3-0015170ACA88.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/6A5EB2B2-E740-DF11-A543-0015170ACA88.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/66D8AECE-EF40-DF11-BFB8-00E08178C05F.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/669FC07F-ED40-DF11-9532-001A64789458.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/667FDFA7-E940-DF11-AF69-0025B3E05CE4.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/5EFD390B-ED40-DF11-89D1-0025B3E06698.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/5E800FB2-F240-DF11-AC55-0025B3E05CDA.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/5E53FAC0-E440-DF11-A2CF-003048D4774E.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/5A90DBB0-F340-DF11-A32E-001A64789DDC.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/4E3D0F6F-ED40-DF11-91D2-0025B3E05CE4.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/4CA21995-EB40-DF11-A5E0-003048D4600C.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/489A0CF6-E940-DF11-89A6-003048D46004.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/46DB27A6-E940-DF11-A620-003048D45FA2.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/42E38BB5-EF40-DF11-819D-003048D47A46.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/4299620D-F240-DF11-80E6-003048635E12.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/3CC87CA8-3B41-DF11-958D-003048D460D4.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/3680D462-EB40-DF11-B36F-003048D45FC8.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/283724A6-FA40-DF11-B8D2-001A64789DF8.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/24F9EA4B-F340-DF11-9FFA-001A64789D1C.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/22D65FC8-EF40-DF11-B2FB-003048D4624A.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/1E29E006-4141-DF11-9FF1-002481E15000.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/1E127F4A-EE40-DF11-AAE6-003048635E12.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/1C1A8D9C-F140-DF11-8A96-003048D47A46.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/1AF719A8-F140-DF11-AB66-001A64789458.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/16F51B00-E940-DF11-B3FE-00E0817917E7.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/162DD150-FB40-DF11-AD4A-003048673EA4.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/0E1FFB86-0141-DF11-805E-003048D46028.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/0813F6D1-FF40-DF11-A473-003048D47774.root',
        '/store/data/Commissioning10/MinimumBias/RAW-RECO/v8/000/132/601/02071949-FA40-DF11-9990-001A64789DEC.root'
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


### JetMetTau SD
process.JetMetTau_1e28 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.JetMetTau_1e28.HLTPaths = (
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
"HLT_DoubleJet15U_ForwardBackward"
)
process.JetMetTau_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1,1,1,1)
process.JetMetTau_1e28.HLTOverallPrescale = cms.uint32(1)
process.JetMetTau_1e28.andOr = True

process.filterSdJetMetTau_1e28 = cms.Path(process.JetMetTau_1e28)



### JetMetTauMonitor SD
process.JetMetTauMonitor_1e28 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.JetMetTauMonitor_1e28.HLTPaths = (
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
process.JetMetTauMonitor_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1,1)
process.JetMetTauMonitor_1e28.HLTOverallPrescale = cms.uint32(1)
process.JetMetTauMonitor_1e28.andOr = True

process.filterSdJetMetTauMonitor_1e28 = cms.Path(process.JetMetTauMonitor_1e28)

### MuMonitor SD
process.MuMonitor_1e28 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
process.MuMonitor_1e28.HLTPaths = ("HLT_L1MuOpen","HLT_L1Mu")
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
"HLT_L1DoubleMuOpen"
)
process.Mu_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1)
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
"HLT_DoublePhoton10_L1R"
)
process.EG_1e28.HLTPathsPrescales  = cms.vuint32(1,1,1,1,1,1,1,1,1,1,1,1)
process.EG_1e28.HLTOverallPrescale = cms.uint32(1)
process.EG_1e28.andOr = True

process.filterSdEG_1e28 = cms.Path(process.EG_1e28)






process.outputSdJetMetTau = cms.OutputModule("PoolOutputModule",
                                          SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterSdJetMetTau_1e28')),                               
                                          dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('SD_JetMetTau')),
                                          outputCommands = process.RECOEventContent.outputCommands,
                                          fileName = cms.untracked.string('SD_JetMetTau_1e28.root')
                                          )

process.outputSdJetMetTauMonitor = cms.OutputModule("PoolOutputModule",
                                          SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterSdJetMetTauMonitor_1e28')),                               
                                          dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('SD_JetMetTauMonitor')),
                                          outputCommands = process.RECOEventContent.outputCommands,
                                          fileName = cms.untracked.string('SD_JetMetTauMonitor_1e28.root')
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
process.outputSdJetMetTau        +
process.outputSdJetMetTauMonitor +
process.outputSdMuMonitor        +
process.outputSdMu               +
process.outputSdEGMonitor        +
process.outputSdEG               
)
