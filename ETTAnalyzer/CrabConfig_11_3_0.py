
# runs = [320038, 320039, 320040, 320061, 320062, 320063, 320064, 320065]
# runs = [320038]
runs = [320065]
Nblocks = 11

##-- https://twiki.cern.ch/twiki/bin/view/CMS/AbrahamTishelmanCharnyHomepage#Checking_Dataset_Luminosity
# export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.1.7/bin:$PATH
# pip install --install-option="--prefix=$HOME/.local" brilws
# voms 
##-- brilcalc lumi -r 320038

CMS_files = []

print "Adding CMS files..."

##-- By run number 
for run in runs:
    print "Run",run
    text_file_path = "Files_Run_%s.txt"%(run)
    with open(text_file_path) as f: ##--- https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
        content = f.readlines()
        content = [x.strip() for x in content] 
        for file in content:
            CMS_files.append(file)

# ##-- By block number 
# for block_i in range(0, Nblocks):
#     print "On block",block_i
#     text_file_path = "Files_Block_%s.txt"%(block_i)
#     with open(text_file_path) as f: 
#         content = f.readlines()
#         content = [x.strip() for x in content] 
#         for file in content:
#             CMS_files.append(file)            

print "Number of input files:",len(CMS_files)

from CRABClient.UserUtilities import config
config = config()
 
# config.General.requestName = 'ETTAnalyzer_320038_to_320065_StripZeroing'
config.General.requestName = 'ETTAnalyzer_crab'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True ##-- Need this True to transfer output files!! at least with eos output.
config.General.transferLogs = False 
 
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ECALDoubleWeights/ETTAnalyzer/conf_11_3_0.py'
# config.JobType.outputFiles = ['root://cmsxrootd.fnal.gov//store/user/atishelm/ECAL_Trigger_Team/test.root']
# config.JobType.numCores = 8
# config.JobType.maxMemoryMB = 8000
 
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputPrimaryDataset = 'ZeroBias'
# config.Data.outLFNDirBase = '/store/user/atishelm/ntuples/ETTAnalyzer_320038_to_320065_StripZeroing/' ##-- for T2_CH_CERN storage site  ##-- 'gsiftp://eosuserftp.cern.ch/eos/user/a/atishelm/ntuples/CRAB_TEST/'
# config.Data.outLFNDirBase = '/store/user/atishelm/ntuples/EcalL1Optimization/ETTAnalyzer_320065_StripZeroing_With_3JuneETTAnalyzer/' ##-- for T2_CH_CERN storage site  ##-- 'gsiftp://eosuserftp.cern.ch/eos/user/a/atishelm/ntuples/CRAB_TEST/'
# config.Data.outLFNDirBase = '/store/user/atishelm/ntuples/EcalL1Optimization/ETTAnalyzer_320065/' ##-- for T2_CH_CERN storage site  ##-- 'gsiftp://eosuserftp.cern.ch/eos/user/a/atishelm/ntuples/CRAB_TEST/'
config.Data.outLFNDirBase = '/store/user/atishelm/ntuples/EcalL1Optimization/ETTAnalyzer/' ##-- for T2_CH_CERN storage site  ##-- 'gsiftp://eosuserftp.cern.ch/eos/user/a/atishelm/ntuples/CRAB_TEST/'
## 'gsiftp://eosuserftp.cern.ch/eos/user/a/atishelm/ntuples/CRAB_TEST/'
config.Data.outputDatasetTag = 'ETTAnalyzer_CMSSW_11_3_0'
config.Data.publication = False 
# config.Data.inputDBS = 'phys03'


config.Data.userInputFiles = CMS_files 

# config.Data.inputDataset = '/ZeroBias/Run2018C-v1/RAW#162eb239-00fd-4f18-a0ba-58e02f83a1c0'
# config.Data.inputDataset = '/ZeroBias/Run2018C-v1/RAW#162eb239-00fd-4f18-a0ba-58e02f83a1c0'
# config.Data.userInputFiles = ['/store/data/Run2018C/ZeroBias/RAW/v1/000/320/038/00000/967C6B51-AE8D-E811-A694-FA163E92389A.root']

# config.Data.userInputFiles = ['/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_1.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_10.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_11.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_12.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_13.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_14.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_15.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_16.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_17.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_18.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_19.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_2.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_20.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_21.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_22.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_23.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_24.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_25.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_26.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_27.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_28.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_29.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_3.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_30.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_31.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_32.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_33.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_34.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_35.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_36.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_37.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_38.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_39.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_4.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_40.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_5.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_6.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_7.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_8.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_9.root'] # If DR1 step, this should be GEN file(s) 
# config.Data.userInputFiles = ['/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_1.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_10.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_11.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_12.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_13.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_14.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_15.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_16.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_17.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_18.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_19.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_2.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_20.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_21.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_22.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_23.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_24.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_25.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_26.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_27.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_28.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_29.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_3.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_30.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_31.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_32.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_33.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_34.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_35.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_36.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_37.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_38.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_39.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_4.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_40.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_5.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_6.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_7.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_8.root','/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_wPU_DR2/200721_133954/0000/GluGluToHHTo_WWgg_qqlnu_nodeSM_100000events_wPU_DR2_9.root'] # If DR1 step, this should be GEN file(s) 
 
config.Site.whitelist = ['T2_FR_GRIF_LLR']
# config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T3_CH_CERNBOX' ##-- CERNBOX, takes outLFNDirBase and changes '/store/user' in outLFNDirBase to /eos/user/

# config.JobType.inputFiles = ['/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ECALDoubleWeights/ETTAnalyzer/EcalTPGOddWeightGroup.db']
# config.JobType.inputFiles = ['/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ECALDoubleWeights/ETTAnalyzer/EcalTPGOddWeightIdMap.db', 

##-- Run 2 mode 
# config.JobType.inputFiles = ['/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ECALDoubleWeights/ETTAnalyzer/EcalTPGOddWeightGroup.db',
                            #  '/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ECALDoubleWeights/ETTAnalyzer/ZeroCandidateSet.db',
                            #  '/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ECALDoubleWeights/ETTAnalyzer/EcalTPG_TPMode_Run2_default.db']

##-- Zeroing
config.JobType.inputFiles = ['/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ECALDoubleWeights/ETTAnalyzer/EcalTPGOddWeightGroup.db',
                             '/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ECALDoubleWeights/ETTAnalyzer/ZeroCandidateSet.db',
                             '/afs/cern.ch/work/a/atishelm/private/CMS-ECAL-Trigger-Group/CMSSW_11_3_0/src/ECALDoubleWeights/ETTAnalyzer/EcalTPG_TPMode_Run3_zeroing.db']                             



# config.JobType.inputFiles = ['EcalTPGOddWeightGroup.db', 'EcalTPG_TPMode_Run2_default.db']
