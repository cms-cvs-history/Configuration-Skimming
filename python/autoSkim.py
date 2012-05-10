## autoSkim 2012 (7E33 menu)
#'SinglePhoton' : 'EXODisplacedPhoton',

## autoSkim 2012 (5E33 menu)
autoSkim = {
    'BTag' : 'LogError+LogErrorMonitor',
    'Commissioning' : 'LogError+LogErrorMonitor',
    'Cosmics' : 'LogError+LogErrorMonitor',    
    'DoubleElectron' : 'LogError+LogErrorMonitor+ZElectron+DiTau+HZZ',
    'DoubleMu' : 'LogError+LogErrorMonitor+HZZ+Zmmg',
    'ElectronHad' : 'LogError+LogErrorMonitor+TOPElePlusJets+EXOHSCP',
    'HcalNZS' : 'LogError+LogErrorMonitor',
    'HT' : 'LogError+LogErrorMonitor+EXOHSCP+HighMET',
    'Jet' : 'LogError+LogErrorMonitor',
    'MET' : 'LogError+LogErrorMonitor+ZHbb+EXOHSCP+HighMET',
    'MinimumBias' : 'LogError+LogErrorMonitor',    
    'MuEG' : 'LogError+LogErrorMonitor+HZZ',
    'MuHad' : 'LogError+LogErrorMonitor+TOPMuPlusJets',
    'MuOnia' : 'LogError+LogErrorMonitor+ChiB',
    'MultiJet' : 'LogError+LogErrorMonitor+HighMET',
    'Photon' : 'LogError+LogErrorMonitor+HighMET',
    'PhotonHad' : 'LogError+LogErrorMonitor',
    'SingleElectron' : 'LogError+LogErrorMonitor+HighMET+DiTau',
    'SingleMu' : 'LogError+LogErrorMonitor+ZMu+HighMET+EXOHSCP+MuTau',
    'Tau' : 'LogError+LogErrorMonitor',
    'TauPlusX' : 'LogError+LogErrorMonitor+MuTauMET',
    }

## autoSkim 2011
"""
    'MinimumBias':'MuonTrack+BeamBkg+ValSkim+LogError+HSCPSD',
    'ZeroBias':'LogError',
    'Commissioning':'DT+LogError',
    'Cosmics':'CosmicSP+LogError',
    'Mu' : 'WMu+ZMu+HighMET+LogError',    
    'EG':'WElectron+ZElectron+HighMET+LogError',
    'Electron':'WElectron+ZElectron+HighMET+LogError',
    'Photon':'WElectron+ZElectron+HighMET+LogError+DiPhoton+EXOHPTE',
    'JetMETTau':'LogError+Tau',
    'JetMET':'HighMET+LogError',
    'BTau':'LogError+Tau',
    'Jet':'HighMET+LogError',
    'METFwd':'HighMET+LogError',
    'SingleMu' : 'WMu+ZMu+HighMET+LogError+HWW+HZZ+DiTau+EXOHSCP',
    'DoubleMu' : 'WMu+ZMu+HighMET+LogError+HWW+HZZ+EXOHSCP',
    'SingleElectron' : 'WElectron+HighMET+LogError+HWW+HZZ+Tau',
    'DoubleElectron' : 'ZElectron+LogError+HWW+HZZ',
    'MuEG' : 'LogError+HWW+HZZ',
    'METBTag': 'HighMET+LogError+EXOHSCP',
    'BTag': 'LogError+EXOHSCP',
    'MET': 'HighMET+LogError+EXOHSCP',

    'HT': 'HighMET+LogError',

    'Tau': 'LogError',
    'PhotonHad': 'LogError',
    'MuHad': 'LogError',
    'MultiJet': 'LogError',
    'MuOnia': 'LogError',
    'ElectronHad': 'LogError',
    'TauPlusX': 'LogError',
"""

autoSkimPDWG = {
    
    }

autoSkimDPG = {

    }

def mergeMapping(map1,map2):
    merged={}
    for k in list(set(map1.keys()+map2.keys())):
        items=[]
        if k in map1: 
            items.append(map1[k])
        if k in map2:
            items.append(map2[k])
        merged[k]='+'.join(items)
    return merged
    
#autoSkim = mergeMapping(autoSkimPDWG,autoSkimDPG)
#print autoSkim
