import FWCore.ParameterSet.Config as cms


process = cms.Process("testFilter")

process.load("PDSDCode.SDFilter.filterSdMu9_8e29_cfi")


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/relval/CMSSW_3_5_2/RelValLM1_sfts/GEN-SIM-RECO/MC_3XY_V21-v1/0016/AA4589C2-2E1E-DF11-B877-0018F3D0968A.root'
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





process.SdHltFilterPath = cms.Path(process.filterSdMu9_8e29) 
 
process.out = cms.OutputModule("PoolOutputModule",
                               SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('SdHltFilterPath')),                               
                               dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('SD_MET')),
                               fileName = cms.untracked.string('testSdHltFilter.root')
                               )




process.this_is_the_end = cms.EndPath(process.out)
