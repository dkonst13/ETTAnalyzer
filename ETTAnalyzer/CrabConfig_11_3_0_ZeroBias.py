"""
16 August 2021 
Abraham Tishelman-Charny 

The purpose of this crab configuration file is to run the ETTAnalyzer over many CMSSW data files in parallel. 
"""

"""
If running over files based on run number or blocks:
"""

Nblocks = 11 ##-- Max: 11 
oneFile = 0 ##-- Run over one file as a test 

##-- https://twiki.cern.ch/twiki/bin/view/CMS/AbrahamTishelmanCharnyHomepage#Checking_Dataset_Luminosity
# export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.1.7/bin:$PATH
# pip install --install-option="--prefix=$HOME/.local" brilws
# voms 
##-- brilcalc lumi -r 320038

CMS_files = []

print "Adding CMS files..."

"""
##-- By run number 
for run in runs:
     print "Run",run
     text_file_path = "RunsAndFiles/Files_Run_%s.txt"%(run)
     with open(text_file_path) as f: ##--- https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
         content = f.readlines()
         content = [x.strip() for x in content] 
         for file in content:
             CMS_files.append(file)
"""

##-- By block number 
for block_i in range(0, Nblocks):
    print "On block",block_i
    text_file_path = "RunsAndFiles/Files_Block_%s.txt"%(block_i)
    with open(text_file_path) as f: 
        content = f.readlines()
        content = [x.strip() for x in content] 
        for file in content:
            CMS_files.append(file)            

if(oneFile):
  CMS_files = ["/store/data/Run2018C/ZeroBias/RAW/v1/000/319/759/00000/8AC0ADC0-9689-E811-8E0B-FA163E2F2CF9.root"] 

print "Number of input files:",len(CMS_files) ##-- 4511 files for all 11 blocks 

"""
CRAB configuration parameters 
"""

inDir = "/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ETTAnalyzer/ETTAnalyzer/"

from CRABClient.UserUtilities import config
config = config()
 
config.General.requestName = 'ZeroBias_2018_EBOnly_FixedOccProportion_Multifit'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True ##-- Need this True to transfer output files!! at least with eos output.
config.General.transferLogs = False 
 
##-- Set cmssw configuration file parameters 
config.JobType.pyCfgParams = [
                                'OverrideWeights=True', 
                                'UserGlobalTag=113X_dataRun2_relval_v1',
                                'RecoMethod=Multifit'
                             ] 
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '%s/conf_11_3_0.py'%(inDir)

"""Analysis job type with user input files only supports file-based splitting"""
config.Data.splitting = 'FileBased'
# config.Data.splitting = 'Automatic'
# config.Data.unitsPerJob = 1
# config.Data.unitsPerJob = 100 ##-- 100 files per job 
config.Data.unitsPerJob = 25 

config.Data.outputPrimaryDataset = 'ZeroBias_2018_EBOnly_FixedOccProportion_Multifit'
config.Data.outputDatasetTag = 'ETTAnalyzer_CMSSW_11_3_0_StripZeroing_Multifit'
config.Data.outLFNDirBase = '/store/group/dpg_ecal/alca_ecalcalib/Trigger/DoubleWeights/' 
config.Data.publication = False 

config.Data.userInputFiles = CMS_files 

config.Site.whitelist = ['T2_CH_CERN'] ##-- Eventually had to change from 'T2_FR_GRIF_LLR' whitelist to this 
config.Site.storageSite = 'T2_CH_CERN'
# config.Site.storageSite = 'T3_CH_CERNBOX' ##-- CERNBOX, takes outLFNDirBase and changes '/store/user' in outLFNDirBase to /eos/user/

##-- Run 2 mode 
# config.JobType.inputFiles = ['/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ECALDoubleWeights/ETTAnalyzer/EcalTPGOddWeightGroup.db',
                            #  '/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ECALDoubleWeights/ETTAnalyzer/ZeroCandidateSet.db',
                            #  '/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ECALDoubleWeights/ETTAnalyzer/EcalTPG_TPMode_Run2_default.db']

##-- Strip zeroing 
config.JobType.inputFiles = ['%s/EcalTPGOddWeightGroup.db'%(inDir),
                             '%s/ZeroCandidateSet.db'%(inDir),
                             '%s/EcalTPG_TPMode_Run3_zeroing.db'%(inDir),
                             '%s/ConfigParams.py'%(inDir) ##-- For cmssw config options 
                             ]                             