import FWCore.ParameterSet.Config as cms


process = cms.Process("skimSdMu1e29")



process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/relval/CMSSW_3_5_4/RelValZTT/GEN-SIM-RECO/START3X_V24-v1/0004/020492F1-2C2C-DF11-AF77-002618943826.root'
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



process.load("Configuration.Skimming.filterSdMu_1e29_cfi")
 
process.out = cms.OutputModule("PoolOutputModule",
                               SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('filterSdMu_1e29')),                               
                               dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('SD_Mu_1e29')),
                               fileName = cms.untracked.string('SD_Mu_1e29.root')
                               )




process.this_is_the_end = cms.EndPath(process.out)
