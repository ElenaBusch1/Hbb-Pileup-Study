# List of all variables to add to TTree
# NOT what you want to use for training
# or any other studies
# It's simply a dump of all jet 
# variables into a  tree
from array import array
class getVariables:
    def __init__(self):
		
         self.LeadSubjet_2Exkt_pt    =    array('f',[0])
         self.LeadSubjet_2Exkt_eta    =    array('f',[0])
         self.LeadSubjet_2Exkt_phi    =    array('f',[0])
         self.LeadSubjet_2Exkt_m    =    array('f',[0])
         self.LeadSubjet_2Exkt_mv2c100    =    array('f',[0])
         self.LeadSubjet_2Exkt_mv2c10    =    array('f',[0])
         self.LeadSubjet_3Exkt_pt    =    array('f',[0])
         self.LeadSubjet_3Exkt_eta    =    array('f',[0])
         self.LeadSubjet_3Exkt_phi    =    array('f',[0])
         self.LeadSubjet_3Exkt_m    =    array('f',[0])
         self.LeadSubjet_3Exkt_mv2c100    =    array('f',[0])
         self.LeadSubjet_3Exkt_mv2c10    =    array('f',[0])
         self.LeadSubjet_trk_pt    =    array('f',[0])
         self.LeadSubjet_trk_eta    =    array('f',[0])
         self.LeadSubjet_trk_phi    =    array('f',[0])
         self.LeadSubjet_trk_m    =    array('f',[0])
         self.LeadSubjet_trk_mv2c100    =    array('f',[0])
         self.LeadSubjet_trk_mv2c10    =    array('f',[0])
         self.LeadSubjet_2Exkt_jf_m    =      array('f',[0])
         self.LeadSubjet_2Exkt_jf_mUncorr    =      array('f',[0])
         self.LeadSubjet_2Exkt_jf_efc    =      array('f',[0])
         self.LeadSubjet_2Exkt_jf_deta    =      array('f',[0])
         self.LeadSubjet_2Exkt_jf_dphi    =      array('f',[0])
         self.LeadSubjet_2Exkt_jf_dRFlightDir    =      array('f',[0])
         self.LeadSubjet_2Exkt_jf_sig3d    =      array('f',[0])
         self.LeadSubjet_2Exkt_ip3d_pb    =    array('f',[0])
         self.LeadSubjet_2Exkt_ip3d_pc    =    array('f',[0])
         self.LeadSubjet_2Exkt_ip3d_pu    =    array('f',[0])
         self.LeadSubjet_2Exkt_ip2d_pb    =    array('f',[0])
         self.LeadSubjet_2Exkt_ip2d_pc    =    array('f',[0])
         self.LeadSubjet_2Exkt_ip2d_pu    =    array('f',[0])
         self.LeadSubjet_2Exkt_sv1_m    =    array('f',[0])
         self.LeadSubjet_2Exkt_sv1_efc    =    array('f',[0])
         self.LeadSubjet_2Exkt_sv1_normdist    =    array('f',[0])
         self.LeadSubjet_2Exkt_sv1_deltaR    =    array('f',[0])
         self.LeadSubjet_2Exkt_sv1_Lxy    =    array('f',[0])
         self.LeadSubjet_2Exkt_sv1_L3d    =    array('f',[0])
         self.LeadSubjet_2Exkt_sv1_significance3d    =    array('f',[0])
         self.LeadSubjet_3Exkt_jf_m    =      array('f',[0])
         self.LeadSubjet_3Exkt_jf_mUncorr    =      array('f',[0])
         self.LeadSubjet_3Exkt_jf_efc    =      array('f',[0])
         self.LeadSubjet_3Exkt_jf_deta    =      array('f',[0])
         self.LeadSubjet_3Exkt_jf_dphi    =      array('f',[0])
         self.LeadSubjet_3Exkt_jf_dRFlightDir    =      array('f',[0])
         self.LeadSubjet_3Exkt_jf_sig3d    =      array('f',[0])
         self.LeadSubjet_3Exkt_ip3d_pb    =    array('f',[0])
         self.LeadSubjet_3Exkt_ip3d_pc    =    array('f',[0])
         self.LeadSubjet_3Exkt_ip3d_pu    =    array('f',[0])
         self.LeadSubjet_3Exkt_ip2d_pb    =    array('f',[0])
         self.LeadSubjet_3Exkt_ip2d_pc    =    array('f',[0])
         self.LeadSubjet_3Exkt_ip2d_pu    =    array('f',[0])
         self.LeadSubjet_3Exkt_sv1_m    =    array('f',[0])
         self.LeadSubjet_3Exkt_sv1_efc    =    array('f',[0])
         self.LeadSubjet_3Exkt_sv1_normdist    =    array('f',[0])
         self.LeadSubjet_3Exkt_sv1_deltaR    =    array('f',[0])
         self.LeadSubjet_3Exkt_sv1_Lxy    =    array('f',[0])
         self.LeadSubjet_3Exkt_sv1_L3d    =    array('f',[0])
         self.LeadSubjet_3Exkt_sv1_significance3d    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_pt    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_eta    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_phi    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_m    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_mv2c100    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_mv2c10    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_pt    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_eta    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_phi    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_m    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_mv2c100    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_mv2c10    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_pt    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_eta    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_phi    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_m    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_mv2c100    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_mv2c10    =    array('f',[0])
         self.SubLeadSubjet_trk_pt    =    array('f',[0])
         self.SubLeadSubjet_trk_eta    =    array('f',[0])
         self.SubLeadSubjet_trk_phi    =    array('f',[0])
         self.SubLeadSubjet_trk_m    =    array('f',[0])
         self.SubLeadSubjet_trk_mv2c100    =    array('f',[0])
         self.SubLeadSubjet_trk_mv2c10    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_jf_m    =      array('f',[0])
         self.SubLeadSubjet_2Exkt_jf_mUncorr    =      array('f',[0])
         self.SubLeadSubjet_2Exkt_jf_efc    =      array('f',[0])
         self.SubLeadSubjet_2Exkt_jf_deta    =      array('f',[0])
         self.SubLeadSubjet_2Exkt_jf_dphi    =      array('f',[0])
         self.SubLeadSubjet_2Exkt_jf_dRFlightDir    =      array('f',[0])
         self.SubLeadSubjet_2Exkt_jf_sig3d    =      array('f',[0])
         self.SubLeadSubjet_2Exkt_ip3d_pb    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_ip3d_pc    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_ip3d_pu    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_ip2d_pb    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_ip2d_pc    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_ip2d_pu    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_sv1_m    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_sv1_efc    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_sv1_normdist    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_sv1_deltaR    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_sv1_Lxy    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_sv1_L3d    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_sv1_significance3d    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_jf_m    =      array('f',[0])
         self.SubLeadSubjet_3Exkt_jf_mUncorr    =      array('f',[0])
         self.SubLeadSubjet_3Exkt_jf_efc    =      array('f',[0])
         self.SubLeadSubjet_3Exkt_jf_deta    =      array('f',[0])
         self.SubLeadSubjet_3Exkt_jf_dphi    =      array('f',[0])
         self.SubLeadSubjet_3Exkt_jf_dRFlightDir    =      array('f',[0])
         self.SubLeadSubjet_3Exkt_jf_sig3d    =      array('f',[0])
         self.SubLeadSubjet_3Exkt_ip3d_pb    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_ip3d_pc    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_ip3d_pu    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_ip2d_pb    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_ip2d_pc    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_ip2d_pu    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_sv1_m    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_sv1_efc    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_sv1_normdist    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_sv1_deltaR    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_sv1_Lxy    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_sv1_L3d    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_sv1_significance3d    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_jf_m    =      array('f',[0])
         self.SubSubLeadSubjet_3Exkt_jf_mUncorr    =      array('f',[0])
         self.SubSubLeadSubjet_3Exkt_jf_efc    =      array('f',[0])
         self.SubSubLeadSubjet_3Exkt_jf_deta    =      array('f',[0])
         self.SubSubLeadSubjet_3Exkt_jf_dphi    =      array('f',[0])
         self.SubSubLeadSubjet_3Exkt_jf_dRFlightDir    =      array('f',[0])
         self.SubSubLeadSubjet_3Exkt_jf_sig3d    =      array('f',[0])
         self.SubSubLeadSubjet_3Exkt_ip3d_pb    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_ip3d_pc    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_ip3d_pu    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_ip2d_pb    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_ip2d_pc    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_ip2d_pu    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_sv1_m    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_sv1_efc    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_sv1_normdist    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_sv1_deltaR    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_sv1_Lxy    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_sv1_L3d    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_sv1_significance3d    =    array('f',[0])
         self.jet_2Exkt_Subjet_Pt_imbalance    =      array('f',[0])
         self.jet_2Exkt_Subjet_deltaR    =      array('f',[0])
         self.jet_3Exkt_Subjet_Pt_imbalance    =      array('f',[0])
         self.jet_3Exkt_Subjet_deltaR    =      array('f',[0])
         self.jet_3Exkt_SubSubjet_Pt_imbalance    =      array('f',[0])
         self.jet_3Exkt_SubSubjet_deltaR    =      array('f',[0])
         self.LeadSubjet_2Exkt_rnnip_pb    =    array('f',[0])
         self.LeadSubjet_2Exkt_rnnip_pc    =    array('f',[0])
         self.LeadSubjet_2Exkt_rnnip_pu    =    array('f',[0])
         self.LeadSubjet_2Exkt_rnnip_ptau    =    array('f',[0])
         self.LeadSubjet_2Exkt_ghost_b_min_dr    =    array('f',[0])
         self.LeadSubjet_3Exkt_rnnip_pb    =    array('f',[0])
         self.LeadSubjet_3Exkt_rnnip_pc    =    array('f',[0])
         self.LeadSubjet_3Exkt_rnnip_pu    =    array('f',[0])
         self.LeadSubjet_3Exkt_rnnip_ptau    =    array('f',[0])
         self.LeadSubjet_3Exkt_ghost_b_min_dr    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_rnnip_pb    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_rnnip_pc    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_rnnip_pu    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_rnnip_ptau    =    array('f',[0])
         self.SubLeadSubjet_2Exkt_ghost_b_min_dr    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_rnnip_pb    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_rnnip_pc    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_rnnip_pu    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_rnnip_ptau    =    array('f',[0])
         self.SubLeadSubjet_3Exkt_ghost_b_min_dr    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_rnnip_pb    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_rnnip_pc    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_rnnip_pu    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_rnnip_ptau    =    array('f',[0])
         self.SubSubLeadSubjet_3Exkt_ghost_b_min_dr    =    array('f',[0])
         self.jet_pt    =    array('f',[0])                     
         self.jet_eta    =    array('f',[0])                     
         self.jet_phi    =    array('f',[0])                   
         self.jet_E    =    array('f',[0])               
         self.jet_pt_orig    =    array('f',[0])                  
         self.jet_eta_orig    =    array('f',[0])                  
         self.jet_phi_orig    =    array('f',[0])                  
         self.jet_E_orig    =    array('f',[0])                
         self.jet_m    =    array('f',[0])            
         self.jet_nGhostHBoso    =    array('i',[0])
         self.jet_nBHadr  =  array('i',[0])            
         self.jet_nGhostBHadr  =  array('i',[0])            
         self.jet_nCHadr  =  array('i',[0])            
         self.jet_nGhostCHadr  =  array('i',[0])            
         self.LeadSubjet_2Exkt_ntrk    =    array('i',[0])
         self.LeadSubjet_2Exkt_jf_ntrkAtVx    =      array('i',[0])
         self.LeadSubjet_2Exkt_jf_nvtx    =      array('i',[0])
         self.LeadSubjet_2Exkt_jf_nvtx1t    =      array('i',[0])
         self.LeadSubjet_2Exkt_jf_n2t    =      array('i',[0])
         self.LeadSubjet_2Exkt_jf_VTXsize    =      array('i',[0])
         self.LeadSubjet_2Exkt_ip3d_ntrk    =    array('i',[0])
         self.LeadSubjet_2Exkt_ip2d_ntrk    =    array('i',[0])
         self.LeadSubjet_2Exkt_sv1_ntrkv    =    array('i',[0])
         self.LeadSubjet_2Exkt_sv1_n2t    =    array('i',[0])
         self.LeadSubjet_2Exkt_sv1_Nvtx    =    array('i',[0])
         self.LeadSubjet_3Exkt_ntrk    =    array('i',[0])
         self.LeadSubjet_3Exkt_jf_ntrkAtVx    =      array('i',[0])
         self.LeadSubjet_3Exkt_jf_nvtx    =      array('i',[0])
         self.LeadSubjet_3Exkt_jf_nvtx1t    =      array('i',[0])
         self.LeadSubjet_3Exkt_jf_n2t    =      array('i',[0])
         self.LeadSubjet_3Exkt_jf_VTXsize    =      array('i',[0])
         self.LeadSubjet_3Exkt_ip3d_ntrk    =    array('i',[0])
         self.LeadSubjet_3Exkt_ip2d_ntrk    =    array('i',[0])
         self.LeadSubjet_3Exkt_sv1_ntrkv    =    array('i',[0])
         self.LeadSubjet_3Exkt_sv1_n2t    =    array('i',[0])
         self.LeadSubjet_3Exkt_sv1_Nvtx    =    array('i',[0])
         self.SubLeadSubjet_2Exkt_ntrk    =    array('i',[0])
         self.SubLeadSubjet_2Exkt_jf_ntrkAtVx    =      array('i',[0])
         self.SubLeadSubjet_2Exkt_jf_nvtx    =      array('i',[0])
         self.SubLeadSubjet_2Exkt_jf_nvtx1t    =      array('i',[0])
         self.SubLeadSubjet_2Exkt_jf_n2t    =      array('i',[0])
         self.SubLeadSubjet_2Exkt_jf_VTXsize    =      array('i',[0])
         self.SubLeadSubjet_2Exkt_ip3d_ntrk    =    array('i',[0])
         self.SubLeadSubjet_2Exkt_ip2d_ntrk    =    array('i',[0])
         self.SubLeadSubjet_2Exkt_sv1_ntrkv    =    array('i',[0])
         self.SubLeadSubjet_2Exkt_sv1_n2t    =    array('i',[0])
         self.SubLeadSubjet_2Exkt_sv1_Nvtx    =    array('i',[0])
         self.SubLeadSubjet_3Exkt_ntrk    =    array('i',[0])
         self.SubLeadSubjet_3Exkt_jf_ntrkAtVx    =      array('i',[0])
         self.SubLeadSubjet_3Exkt_jf_nvtx    =      array('i',[0])
         self.SubLeadSubjet_3Exkt_jf_nvtx1t    =      array('i',[0])
         self.SubLeadSubjet_3Exkt_jf_n2t    =      array('i',[0])
         self.SubLeadSubjet_3Exkt_jf_VTXsize    =      array('i',[0])
         self.SubLeadSubjet_3Exkt_ip3d_ntrk    =    array('i',[0])
         self.SubLeadSubjet_3Exkt_ip2d_ntrk    =    array('i',[0])
         self.SubLeadSubjet_3Exkt_sv1_ntrkv    =    array('i',[0])
         self.SubLeadSubjet_3Exkt_sv1_n2t    =    array('i',[0])
         self.SubLeadSubjet_3Exkt_sv1_Nvtx    =    array('i',[0])
         self.SubSubLeadSubjet_3Exkt_ntrk    =    array('i',[0])
         self.SubSubLeadSubjet_3Exkt_jf_ntrkAtVx    =      array('i',[0])
         self.SubSubLeadSubjet_3Exkt_jf_nvtx    =      array('i',[0])
         self.SubSubLeadSubjet_3Exkt_jf_nvtx1t    =      array('i',[0])
         self.SubSubLeadSubjet_3Exkt_jf_n2t    =      array('i',[0])
         self.SubSubLeadSubjet_3Exkt_jf_VTXsize    =      array('i',[0])
         self.SubSubLeadSubjet_3Exkt_ip3d_ntrk    =    array('i',[0])
         self.SubSubLeadSubjet_3Exkt_ip2d_ntrk    =    array('i',[0])
         self.SubSubLeadSubjet_3Exkt_sv1_ntrkv    =    array('i',[0])
         self.SubSubLeadSubjet_3Exkt_sv1_n2t    =    array('i',[0])
         self.SubSubLeadSubjet_3Exkt_sv1_Nvtx    =    array('i',[0])
         self.mcwg =array('f', [0])
         self.nvtx =array('i',[0])
         self.PVx  =array('f',[0])
         self.PVy  =array('f',[0])
         self.PVz  =array('f',[0])
         self.avgmu=array('f',[0])
         self.actmu=array('f',[0])
         
                          
    def getVariableDict(self,type):
         #   define objets in dictionary
            floatSub   =   {
                "jet_2Exkt_pt_Lead":  self.LeadSubjet_2Exkt_pt,
                "jet_2Exkt_eta_Lead":  self.LeadSubjet_2Exkt_eta,
                "jet_2Exkt_phi_Lead":  self.LeadSubjet_2Exkt_phi, 
                "jet_2Exkt_m_Lead":  self.LeadSubjet_2Exkt_m,
                "jet_2Exkt_mv2c100_Lead":  self.LeadSubjet_2Exkt_mv2c100, 	
                "jet_2Exkt_mv2c10_Lead":  self.LeadSubjet_2Exkt_mv2c10, 
                "jet_3Exkt_pt_Lead":  self.LeadSubjet_3Exkt_pt,
                "jet_3Exkt_eta_Lead":  self.LeadSubjet_3Exkt_eta,
                "jet_3Exkt_phi_Lead":  self.LeadSubjet_3Exkt_phi,
                "jet_3Exkt_m_Lead":  self.LeadSubjet_3Exkt_m,
                "jet_3Exkt_mv2c100_Lead":  self.LeadSubjet_3Exkt_mv2c100,
                "jet_3Exkt_mv2c10_Lead":  self.LeadSubjet_3Exkt_mv2c10,
                "jet_trk_pt_Lead":  self.LeadSubjet_trk_pt,
                "jet_trk_eta_Lead":  self.LeadSubjet_trk_eta,
                "jet_trk_phi_Lead":  self.LeadSubjet_trk_phi, 
                "jet_trk_m_Lead":  self.LeadSubjet_trk_m,
                "jet_trk_mv2c100_Lead":  self.LeadSubjet_trk_mv2c100, 	
                "jet_trk_mv2c10_Lead":  self.LeadSubjet_trk_mv2c10, 
                "jet_2Exkt_jf_m_Lead":  self.LeadSubjet_2Exkt_jf_m,     
                "jet_2Exkt_jf_mUncorr_Lead":  self.LeadSubjet_2Exkt_jf_mUncorr,     
                "jet_2Exkt_jf_efc_Lead":  self.LeadSubjet_2Exkt_jf_efc, 
                "jet_2Exkt_jf_deta_Lead":  self.LeadSubjet_2Exkt_jf_deta, 	
                "jet_2Exkt_jf_dphi_Lead":  self.LeadSubjet_2Exkt_jf_dphi, 	
                "jet_2Exkt_jf_dRFlightDir_Lead":  self.LeadSubjet_2Exkt_jf_dRFlightDir, 	
                "jet_2Exkt_jf_sig3d_Lead":  self.LeadSubjet_2Exkt_jf_sig3d, 	
                "jet_2Exkt_ip3d_pb_Lead":  self.LeadSubjet_2Exkt_ip3d_pb,     
                "jet_2Exkt_ip3d_pc_Lead":  self.LeadSubjet_2Exkt_ip3d_pc, 	
                "jet_2Exkt_ip3d_pu_Lead":  self.LeadSubjet_2Exkt_ip3d_pu, 	
                "jet_2Exkt_ip2d_pb_Lead":  self.LeadSubjet_2Exkt_ip2d_pb, 
                "jet_2Exkt_ip2d_pc_Lead":  self.LeadSubjet_2Exkt_ip2d_pc, 
                "jet_2Exkt_ip2d_pu_Lead":  self.LeadSubjet_2Exkt_ip2d_pu, 
                "jet_2Exkt_sv1_m_Lead":  self.LeadSubjet_2Exkt_sv1_m, 
                "jet_2Exkt_sv1_efc_Lead":  self.LeadSubjet_2Exkt_sv1_efc, 
                "jet_2Exkt_sv1_normdist_Lead":  self.LeadSubjet_2Exkt_sv1_normdist, 
                "jet_2Exkt_sv1_deltaR_Lead":  self.LeadSubjet_2Exkt_sv1_deltaR, 
                "jet_2Exkt_sv1_Lxy_Lead":  self.LeadSubjet_2Exkt_sv1_Lxy, 
                "jet_2Exkt_sv1_L3d_Lead":  self.LeadSubjet_2Exkt_sv1_L3d, 
                "jet_2Exkt_sv1_significance3d_Lead":  self.LeadSubjet_2Exkt_sv1_significance3d, 
                "jet_2Exkt_pt_SubLead":  self.SubLeadSubjet_2Exkt_pt, 
                "jet_2Exkt_eta_SubLead":  self.SubLeadSubjet_2Exkt_eta, 
                "jet_2Exkt_phi_SubLead":  self.SubLeadSubjet_2Exkt_phi, 
                "jet_2Exkt_m_SubLead":  self.SubLeadSubjet_2Exkt_m, 
                "jet_2Exkt_mv2c100_SubLead":  self.SubLeadSubjet_2Exkt_mv2c100, 
                "jet_2Exkt_mv2c10_SubLead":  self.SubLeadSubjet_2Exkt_mv2c10, 
                "jet_3Exkt_jf_m_Lead":  self.LeadSubjet_3Exkt_jf_m,
                "jet_3Exkt_jf_mUncorr_Lead":  self.LeadSubjet_3Exkt_jf_mUncorr,
                "jet_3Exkt_jf_efc_Lead":  self.LeadSubjet_3Exkt_jf_efc,
                "jet_3Exkt_jf_deta_Lead":  self.LeadSubjet_3Exkt_jf_deta,
                "jet_3Exkt_jf_dphi_Lead":  self.LeadSubjet_3Exkt_jf_dphi,
                "jet_3Exkt_jf_dRFlightDir_Lead":  self.LeadSubjet_3Exkt_jf_dRFlightDir,
                "jet_3Exkt_jf_sig3d_Lead":  self.LeadSubjet_3Exkt_jf_sig3d,
                "jet_3Exkt_ip3d_pb_Lead":  self.LeadSubjet_3Exkt_ip3d_pb,
                "jet_3Exkt_ip3d_pc_Lead":  self.LeadSubjet_3Exkt_ip3d_pc,
                "jet_3Exkt_ip3d_pu_Lead":  self.LeadSubjet_3Exkt_ip3d_pu,
                "jet_3Exkt_ip2d_pb_Lead":  self.LeadSubjet_3Exkt_ip2d_pb,
                "jet_3Exkt_ip2d_pc_Lead":  self.LeadSubjet_3Exkt_ip2d_pc,
                "jet_3Exkt_ip2d_pu_Lead":  self.LeadSubjet_3Exkt_ip2d_pu,
                "jet_3Exkt_sv1_m_Lead":  self.LeadSubjet_3Exkt_sv1_m,
                "jet_3Exkt_sv1_efc_Lead":  self.LeadSubjet_3Exkt_sv1_efc,
                "jet_3Exkt_sv1_normdist_Lead":  self.LeadSubjet_3Exkt_sv1_normdist,
                "jet_3Exkt_sv1_deltaR_Lead":  self.LeadSubjet_3Exkt_sv1_deltaR,
                "jet_3Exkt_sv1_Lxy_Lead":  self.LeadSubjet_3Exkt_sv1_Lxy,
                "jet_3Exkt_sv1_L3d_Lead":  self.LeadSubjet_3Exkt_sv1_L3d,
                "jet_3Exkt_sv1_significance3d_Lead":  self.LeadSubjet_3Exkt_sv1_significance3d,
                "jet_3Exkt_pt_SubLead":  self.SubLeadSubjet_3Exkt_pt,
                "jet_3Exkt_eta_SubLead":  self.SubLeadSubjet_3Exkt_eta,
                "jet_3Exkt_phi_SubLead":  self.SubLeadSubjet_3Exkt_phi,
                "jet_3Exkt_m_SubLead":  self.SubLeadSubjet_3Exkt_m,
                "jet_3Exkt_mv2c100_SubLead":  self.SubLeadSubjet_3Exkt_mv2c100,
                "jet_3Exkt_mv2c10_SubLead":  self.SubLeadSubjet_3Exkt_mv2c10,
                "jet_3Exkt_pt_SubSubLead":  self.SubSubLeadSubjet_3Exkt_pt,
                "jet_3Exkt_eta_SubSubLead":  self.SubSubLeadSubjet_3Exkt_eta,
                "jet_3Exkt_phi_SubSubLead":  self.SubSubLeadSubjet_3Exkt_phi,
                "jet_3Exkt_m_SubSubLead":  self.SubSubLeadSubjet_3Exkt_m,
                "jet_3Exkt_mv2c100_SubSubLead":  self.SubSubLeadSubjet_3Exkt_mv2c100,
                "jet_3Exkt_mv2c10_SubSubLead":  self.SubSubLeadSubjet_3Exkt_mv2c10,
                "jet_trk_pt_SubLead":  self.SubLeadSubjet_trk_pt, 
                "jet_trk_eta_SubLead":  self.SubLeadSubjet_trk_eta, 
                "jet_trk_phi_SubLead":  self.SubLeadSubjet_trk_phi, 
                "jet_trk_m_SubLead":  self.SubLeadSubjet_trk_m, 
                "jet_trk_mv2c100_SubLead":  self.SubLeadSubjet_trk_mv2c100, 
                "jet_trk_mv2c10_SubLead":  self.SubLeadSubjet_trk_mv2c10, 
                "jet_2Exkt_jf_m_SubLead":  self.SubLeadSubjet_2Exkt_jf_m, 
                "jet_2Exkt_jf_mUncorr_SubLead":  self.SubLeadSubjet_2Exkt_jf_mUncorr, 
                "jet_2Exkt_jf_efc_SubLead":  self.SubLeadSubjet_2Exkt_jf_efc, 
                "jet_2Exkt_jf_deta_SubLead":  self.SubLeadSubjet_2Exkt_jf_deta, 
                "jet_2Exkt_jf_dphi_SubLead":  self.SubLeadSubjet_2Exkt_jf_dphi, 
                "jet_2Exkt_jf_dRFlightDir_SubLead":  self.SubLeadSubjet_2Exkt_jf_dRFlightDir, 
                "jet_2Exkt_jf_sig3d_SubLead":  self.SubLeadSubjet_2Exkt_jf_sig3d, 
                "jet_2Exkt_ip3d_pb_SubLead":  self.SubLeadSubjet_2Exkt_ip3d_pb, 
                "jet_2Exkt_ip3d_pc_SubLead":  self.SubLeadSubjet_2Exkt_ip3d_pc, 
                "jet_2Exkt_ip3d_pu_SubLead":  self.SubLeadSubjet_2Exkt_ip3d_pu, 
                "jet_2Exkt_ip2d_pb_SubLead":  self.SubLeadSubjet_2Exkt_ip2d_pb, 
                "jet_2Exkt_ip2d_pc_SubLead":  self.SubLeadSubjet_2Exkt_ip2d_pc, 
                "jet_2Exkt_ip2d_pu_SubLead":  self.SubLeadSubjet_2Exkt_ip2d_pu, 
                "jet_2Exkt_sv1_m_SubLead":  self.SubLeadSubjet_2Exkt_sv1_m, 
                "jet_2Exkt_sv1_efc_SubLead":  self.SubLeadSubjet_2Exkt_sv1_efc, 
                "jet_2Exkt_sv1_normdist_SubLead":  self.SubLeadSubjet_2Exkt_sv1_normdist, 
                "jet_2Exkt_sv1_deltaR_SubLead":  self.SubLeadSubjet_2Exkt_sv1_deltaR, 
                "jet_2Exkt_sv1_Lxy_SubLead":  self.SubLeadSubjet_2Exkt_sv1_Lxy, 
                "jet_2Exkt_sv1_L3d_SubLead":  self.SubLeadSubjet_2Exkt_sv1_L3d, 
                "jet_2Exkt_sv1_significance3d_SubLead":self.SubLeadSubjet_2Exkt_sv1_significance3d,
                "jet_3Exkt_jf_m_SubLead":  self.SubLeadSubjet_3Exkt_jf_m,
                "jet_3Exkt_jf_mUncorr_SubLead":  self.SubLeadSubjet_3Exkt_jf_mUncorr,
                "jet_3Exkt_jf_efc_SubLead":  self.SubLeadSubjet_3Exkt_jf_efc,
                "jet_3Exkt_jf_deta_SubLead":  self.SubLeadSubjet_3Exkt_jf_deta,
                "jet_3Exkt_jf_dphi_SubLead":  self.SubLeadSubjet_3Exkt_jf_dphi,
                "jet_3Exkt_jf_dRFlightDir_SubLead":  self.SubLeadSubjet_3Exkt_jf_dRFlightDir,
                "jet_3Exkt_jf_sig3d_SubLead":  self.SubLeadSubjet_3Exkt_jf_sig3d,
                "jet_3Exkt_ip3d_pb_SubLead":  self.SubLeadSubjet_3Exkt_ip3d_pb,
                "jet_3Exkt_ip3d_pc_SubLead":  self.SubLeadSubjet_3Exkt_ip3d_pc,
                "jet_3Exkt_ip3d_pu_SubLead":  self.SubLeadSubjet_3Exkt_ip3d_pu,
                "jet_3Exkt_ip2d_pb_SubLead":  self.SubLeadSubjet_3Exkt_ip2d_pb,
                "jet_3Exkt_ip2d_pc_SubLead":  self.SubLeadSubjet_3Exkt_ip2d_pc,
                "jet_3Exkt_ip2d_pu_SubLead":  self.SubLeadSubjet_3Exkt_ip2d_pu,
                "jet_3Exkt_sv1_m_SubLead":  self.SubLeadSubjet_3Exkt_sv1_m,
                "jet_3Exkt_sv1_efc_SubLead":  self.SubLeadSubjet_3Exkt_sv1_efc,
                "jet_3Exkt_sv1_normdist_SubLead":  self.SubLeadSubjet_3Exkt_sv1_normdist,
                "jet_3Exkt_sv1_deltaR_SubLead":  self.SubLeadSubjet_3Exkt_sv1_deltaR,
                "jet_3Exkt_sv1_Lxy_SubLead":  self.SubLeadSubjet_3Exkt_sv1_Lxy,
                "jet_3Exkt_sv1_L3d_SubLead":  self.SubLeadSubjet_3Exkt_sv1_L3d,
                "jet_3Exkt_sv1_significance3d_SubLead":self.SubLeadSubjet_3Exkt_sv1_significance3d,
                "jet_3Exkt_jf_m_SubSubLead":  self.SubSubLeadSubjet_3Exkt_jf_m,
                "jet_3Exkt_jf_mUncorr_SubSubLead":  self.SubSubLeadSubjet_3Exkt_jf_mUncorr,
                "jet_3Exkt_jf_efc_SubSubLead":  self.SubSubLeadSubjet_3Exkt_jf_efc,
                "jet_3Exkt_jf_deta_SubSubLead":  self.SubSubLeadSubjet_3Exkt_jf_deta,
                "jet_3Exkt_jf_dphi_SubSubLead":  self.SubSubLeadSubjet_3Exkt_jf_dphi,
                "jet_3Exkt_jf_dRFlightDir_SubSubLead":  self.SubSubLeadSubjet_3Exkt_jf_dRFlightDir,
                "jet_3Exkt_jf_sig3d_SubSubLead":  self.SubSubLeadSubjet_3Exkt_jf_sig3d,
                "jet_3Exkt_ip3d_pb_SubSubLead":  self.SubSubLeadSubjet_3Exkt_ip3d_pb,
                "jet_3Exkt_ip3d_pc_SubSubLead":  self.SubSubLeadSubjet_3Exkt_ip3d_pc,
                "jet_3Exkt_ip3d_pu_SubSubLead":  self.SubSubLeadSubjet_3Exkt_ip3d_pu,
                "jet_3Exkt_ip2d_pb_SubSubLead":  self.SubSubLeadSubjet_3Exkt_ip2d_pb,
                "jet_3Exkt_ip2d_pc_SubSubLead":  self.SubSubLeadSubjet_3Exkt_ip2d_pc,
                "jet_3Exkt_ip2d_pu_SubSubLead":  self.SubSubLeadSubjet_3Exkt_ip2d_pu,
                "jet_3Exkt_sv1_m_SubSubLead":  self.SubSubLeadSubjet_3Exkt_sv1_m,
                "jet_3Exkt_sv1_efc_SubSubLead":  self.SubSubLeadSubjet_3Exkt_sv1_efc,
                "jet_3Exkt_sv1_normdist_SubSubLead":  self.SubSubLeadSubjet_3Exkt_sv1_normdist,
                "jet_3Exkt_sv1_deltaR_SubSubLead":  self.SubSubLeadSubjet_3Exkt_sv1_deltaR,
                "jet_3Exkt_sv1_Lxy_SubSubLead":  self.SubSubLeadSubjet_3Exkt_sv1_Lxy,
                "jet_3Exkt_sv1_L3d_SubSubLead":  self.SubSubLeadSubjet_3Exkt_sv1_L3d,
                "jet_3Exkt_sv1_significance3d_SubSubLead":self.SubSubLeadSubjet_3Exkt_sv1_significance3d,
                "jet_2Exkt_rnnip_pb_Lead":  self.LeadSubjet_2Exkt_rnnip_pb, 
                "jet_2Exkt_rnnip_pc_Lead":  self.LeadSubjet_2Exkt_rnnip_pc, 
                "jet_2Exkt_rnnip_pu_Lead":  self.LeadSubjet_2Exkt_rnnip_pu, 
                "jet_2Exkt_rnnip_ptau_Lead":  self.LeadSubjet_2Exkt_rnnip_ptau, 
                "jet_3Exkt_rnnip_pb_Lead":  self.LeadSubjet_3Exkt_rnnip_pb,
                "jet_3Exkt_rnnip_pc_Lead":  self.LeadSubjet_3Exkt_rnnip_pc,
                "jet_3Exkt_rnnip_pu_Lead":  self.LeadSubjet_3Exkt_rnnip_pu,
                "jet_3Exkt_rnnip_ptau_Lead":  self.LeadSubjet_3Exkt_rnnip_ptau,
                "jet_2Exkt_rnnip_pb_SubLead":  self.SubLeadSubjet_2Exkt_rnnip_pb, 
                "jet_2Exkt_rnnip_pc_SubLead":  self.SubLeadSubjet_2Exkt_rnnip_pc, 
                "jet_2Exkt_rnnip_pu_SubLead":  self.SubLeadSubjet_2Exkt_rnnip_pu, 
                "jet_2Exkt_rnnip_ptau_SubLead":  self.SubLeadSubjet_2Exkt_rnnip_ptau,
                "jet_3Exkt_rnnip_pb_SubLead":  self.SubLeadSubjet_3Exkt_rnnip_pb,
                "jet_3Exkt_rnnip_pc_SubLead":  self.SubLeadSubjet_3Exkt_rnnip_pc,
                "jet_3Exkt_rnnip_pu_SubLead":  self.SubLeadSubjet_3Exkt_rnnip_pu,
                "jet_3Exkt_rnnip_ptau_SubLead":  self.SubLeadSubjet_3Exkt_rnnip_ptau,
                "jet_3Exkt_rnnip_pb_SubSubLead":  self.SubSubLeadSubjet_3Exkt_rnnip_pb,
                "jet_3Exkt_rnnip_pc_SubSubLead":  self.SubSubLeadSubjet_3Exkt_rnnip_pc,
                "jet_3Exkt_rnnip_pu_SubSubLead":  self.SubSubLeadSubjet_3Exkt_rnnip_pu,
                "jet_3Exkt_rnnip_ptau_SubSubLead":  self.SubSubLeadSubjet_3Exkt_rnnip_ptau
		 }
            floatVar={
                "jet_pt":  self.jet_pt,
                "jet_eta":  self.jet_eta,
                "jet_phi":  self.jet_phi,
                "jet_E":  self.jet_E,
                "jet_pt_orig":  self.jet_pt_orig,
                "jet_eta_orig":  self.jet_eta_orig,
                "jet_phi_orig":  self.jet_phi_orig,
                "jet_E_orig":  self.jet_E_orig,
                "jet_m":  self.jet_m,
                "mcwg":  self.mcwg,
                "PVx":  self.PVx,
                "PVy":  self.PVy,
                "PVz":  self.PVz,
                "actmu":  self.actmu,
                "avgmu":  self.avgmu,
                "jet_2Exkt_Subjet_Pt_imbalance":  self.jet_2Exkt_Subjet_Pt_imbalance, 
                "jet_2Exkt_Subjet_deltaR":  self.jet_2Exkt_Subjet_deltaR             
                "jet_3Exkt_Subjet_Pt_imbalance":  self.jet_3Exkt_Subjet_Pt_imbalance,
                "jet_3Exkt_Subjet_deltaR":  self.jet_3Exkt_Subjet_deltaR
                "jet_3Exkt_SubSubjet_Pt_imbalance":  self.jet_3Exkt_SubSubjet_Pt_imbalance,
                "jet_3Exkt_SubSubjet_deltaR":  self.jet_3Exkt_SubSubjet_deltaR
            }
            intVar   =  {
                "jet_nGhostHBoso":                    self.jet_nGhostHBoso,
                "jet_nBHadr":                         self.jet_nBHadr,
                "jet_nGhostBHadr":                    self.jet_nGhostBHadr,
                "jet_nGhostCHadr":                    self.jet_nGhostCHadr,
                "jet_nCHadr":                         self.jet_nCHadr,
                "nvtx":                         self.nvtx
              }
            intSub={
                "jet_2Exkt_ntrk_Lead":  self.LeadSubjet_2Exkt_ntrk, 
                "jet_2Exkt_jf_ntrkAtVx_Lead":  self.LeadSubjet_2Exkt_jf_ntrkAtVx, 
                "jet_2Exkt_jf_nvtx_Lead":  self.LeadSubjet_2Exkt_jf_nvtx, 
                "jet_2Exkt_jf_nvtx1t_Lead":  self.LeadSubjet_2Exkt_jf_nvtx1t, 
                "jet_2Exkt_jf_n2t_Lead":  self.LeadSubjet_2Exkt_jf_n2t, 
                "jet_2Exkt_jf_VTXsize_Lead":  self.LeadSubjet_2Exkt_jf_VTXsize, 
                "jet_2Exkt_ip3d_ntrk_Lead":  self.LeadSubjet_2Exkt_ip3d_ntrk, 
                "jet_2Exkt_ip2d_ntrk_Lead":  self.LeadSubjet_2Exkt_ip2d_ntrk, 
                "jet_2Exkt_sv1_ntrkv_Lead":  self.LeadSubjet_2Exkt_sv1_ntrkv, 
                "jet_2Exkt_sv1_n2t_Lead":  self.LeadSubjet_2Exkt_sv1_n2t, 
                "jet_2Exkt_sv1_Nvtx_Lead":  self.LeadSubjet_2Exkt_sv1_Nvtx, 
                "jet_3Exkt_ntrk_Lead":  self.LeadSubjet_3Exkt_ntrk,
                "jet_3Exkt_jf_ntrkAtVx_Lead":  self.LeadSubjet_3Exkt_jf_ntrkAtVx,
                "jet_3Exkt_jf_nvtx_Lead":  self.LeadSubjet_3Exkt_jf_nvtx,
                "jet_3Exkt_jf_nvtx1t_Lead":  self.LeadSubjet_3Exkt_jf_nvtx1t,
                "jet_3Exkt_jf_n2t_Lead":  self.LeadSubjet_3Exkt_jf_n2t,
                "jet_3Exkt_jf_VTXsize_Lead":  self.LeadSubjet_3Exkt_jf_VTXsize,
                "jet_3Exkt_ip3d_ntrk_Lead":  self.LeadSubjet_3Exkt_ip3d_ntrk,
                "jet_3Exkt_ip2d_ntrk_Lead":  self.LeadSubjet_3Exkt_ip2d_ntrk,
                "jet_3Exkt_sv1_ntrkv_Lead":  self.LeadSubjet_3Exkt_sv1_ntrkv,
                "jet_3Exkt_sv1_n2t_Lead":  self.LeadSubjet_3Exkt_sv1_n2t,
                "jet_3Exkt_sv1_Nvtx_Lead":  self.LeadSubjet_3Exkt_sv1_Nvtx,
                "jet_2Exkt_ntrk_SubLead":  self.SubLeadSubjet_2Exkt_ntrk, 
                "jet_2Exkt_jf_ntrkAtVx_SubLead":  self.SubLeadSubjet_2Exkt_jf_ntrkAtVx, 
                "jet_2Exkt_jf_nvtx_SubLead":  self.SubLeadSubjet_2Exkt_jf_nvtx, 
                "jet_2Exkt_jf_nvtx1t_SubLead":  self.SubLeadSubjet_2Exkt_jf_nvtx1t, 
                "jet_2Exkt_jf_n2t_SubLead":  self.SubLeadSubjet_2Exkt_jf_n2t, 
                "jet_2Exkt_jf_VTXsize_SubLead":  self.SubLeadSubjet_2Exkt_jf_VTXsize, 
                "jet_2Exkt_ip3d_ntrk_SubLead":  self.SubLeadSubjet_2Exkt_ip3d_ntrk, 
                "jet_2Exkt_ip2d_ntrk_SubLead":  self.SubLeadSubjet_2Exkt_ip2d_ntrk, 
                "jet_2Exkt_sv1_ntrkv_SubLead":  self.SubLeadSubjet_2Exkt_sv1_ntrkv, 
                "jet_2Exkt_sv1_n2t_SubLead":  self.SubLeadSubjet_2Exkt_sv1_n2t, 
                "jet_2Exkt_sv1_Nvtx_SubLead":  self.SubLeadSubjet_2Exkt_sv1_Nvtx
                "jet_3Exkt_ntrk_SubLead":  self.SubLeadSubjet_3Exkt_ntrk,
                "jet_3Exkt_jf_ntrkAtVx_SubLead":  self.SubLeadSubjet_3Exkt_jf_ntrkAtVx,
                "jet_3Exkt_jf_nvtx_SubLead":  self.SubLeadSubjet_3Exkt_jf_nvtx,
                "jet_3Exkt_jf_nvtx1t_SubLead":  self.SubLeadSubjet_3Exkt_jf_nvtx1t,
                "jet_3Exkt_jf_n2t_SubLead":  self.SubLeadSubjet_3Exkt_jf_n2t,
                "jet_3Exkt_jf_VTXsize_SubLead":  self.SubLeadSubjet_3Exkt_jf_VTXsize,
                "jet_3Exkt_ip3d_ntrk_SubLead":  self.SubLeadSubjet_3Exkt_ip3d_ntrk,
                "jet_3Exkt_ip2d_ntrk_SubLead":  self.SubLeadSubjet_3Exkt_ip2d_ntrk,
                "jet_3Exkt_sv1_ntrkv_SubLead":  self.SubLeadSubjet_3Exkt_sv1_ntrkv,
                "jet_3Exkt_sv1_n2t_SubLead":  self.SubLeadSubjet_3Exkt_sv1_n2t,
                "jet_3Exkt_sv1_Nvtx_SubLead":  self.SubLeadSubjet_3Exkt_sv1_Nvtx
                "jet_3Exkt_ntrk_SubSubLead":  self.SubSubLeadSubjet_3Exkt_ntrk,
                "jet_3Exkt_jf_ntrkAtVx_SubSubLead":  self.SubSubLeadSubjet_3Exkt_jf_ntrkAtVx,
                "jet_3Exkt_jf_nvtx_SubSubLead":  self.SubSubLeadSubjet_3Exkt_jf_nvtx,
                "jet_3Exkt_jf_nvtx1t_SubSubLead":  self.SubSubLeadSubjet_3Exkt_jf_nvtx1t,
                "jet_3Exkt_jf_n2t_SubSubLead":  self.SubSubLeadSubjet_3Exkt_jf_n2t,
                "jet_3Exkt_jf_VTXsize_SubSubLead":  self.SubSubLeadSubjet_3Exkt_jf_VTXsize,
                "jet_3Exkt_ip3d_ntrk_SubSubLead":  self.SubSubLeadSubjet_3Exkt_ip3d_ntrk,
                "jet_3Exkt_ip2d_ntrk_SubSubLead":  self.SubSubLeadSubjet_3Exkt_ip2d_ntrk,
                "jet_3Exkt_sv1_ntrkv_SubSubLead":  self.SubSubLeadSubjet_3Exkt_sv1_ntrkv,
                "jet_3Exkt_sv1_n2t_SubSubLead":  self.SubSubLeadSubjet_3Exkt_sv1_n2t,
                "jet_3Exkt_sv1_Nvtx_SubSubLead":  self.SubSubLeadSubjet_3Exkt_sv1_Nvtx
                }
                
            if(type  ==  'int'):
                return intVar
            elif(type  ==  'float'):
                return floatVar
            elif(type == 'intsub'):
                return intSub
            elif(type == 'floatsub'):
                return floatSub
