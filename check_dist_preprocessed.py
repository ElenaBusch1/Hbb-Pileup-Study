import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import h5py


from MV2_defaults import default_values

# ---- list of variables including pT, eta ---- #
varfile = open('Full_MV2_variables.txt','r')
variablelist = varfile.read().splitlines()
varfile.close()

print ('Var Number = %i' % len(variablelist))

df = h5py.File('Weight0.h5', 'r')
f = h5py.File('prepared_sample_hightpt.h5', 'r')

Traing_sample = f['X_train'][:]
Validation_sample = f['X_val'][:]
Testing_sample = f['X_test'][:]

dijet=f['dijet'][:]
bbjet=f['bbjet'][:]
#ttbar=f['ttbar'][:]
di_vs_bb_weights=df['dijet_vs_bb_weights'][:] 
bb_vs_bb_weights= df['bb_vs_bb_weights'][:]
sample = f['X'][:]

#bb_vs_bb_weights=f['bbjet_weight'][:]
#di_vs_bb_weights=f['dijet_weight'][:]
#tt_vs_bb_weights=f['ttjet_weight'][:]
dijet=dijet[:, 9:]
bbjet=bbjet[:, 9:]
#ttbar=ttbar[:, 5:]
weights = f['X_weights'][:]
training_weights = f['X_weights_train'][:]
testing_weights = f['X_weights_test'][:]
val_weights = f['X_weights_val'][:]
variablelist=variablelist[9:]


#fig, ax= plt.subplots(34, 3, figsize=(40,280))
#fig, ax = plt.subplots()
nbins = 50
varcounter = -1

from matplotlib.ticker import MultipleLocator, FormatStrFormatter 
xmajorLocator   = MultipleLocator(200) 
xmajorFormatter = FormatStrFormatter('%1d')
xminorLocator   = MultipleLocator(50)
ymajorLocator   = MultipleLocator(2000) 
ymajorFormatter = FormatStrFormatter('%1d') 
yminorLocator   = MultipleLocator(1e1)

for varcounter in range(95):
	print(variablelist[varcounter])
	if variablelist[varcounter]=="jet_pt" or variablelist[varcounter]=="jet_m":
        	nbins=100 
                plt.hist(bbjet[:,varcounter]/1e3,nbins,density=0,weights = bb_vs_bb_weights, alpha=0.8,linewidth=1.5,color='r',label='bbjets',  histtype='step' )
                plt.hist(dijet[:,varcounter]/1e3,nbins,density=0,weights = di_vs_bb_weights, alpha=0.8,linewidth=1.5,color='b',label='dijet',  histtype='step' )
		plt.title(variablelist[varcounter])
                plt.xlabel(variablelist[varcounter]+" (GeV)")
		plt.ylabel("A.U.")
		plt.legend()
		plt.savefig(variablelist[varcounter]+'_bfs.pdf')
		plt.close()
		# plt.hist(ttbar[:,varcounter]/1e3,nbins,normed=0,weights = tt_vs_bb_weights, alpha=0.3,linewidth=1.5,color='g',label='ttbar',   histtype='step' )
        elif variablelist[varcounter]=="jet_eta":
        	nbins=100
		#nbins=50
                plt.hist(bbjet[:,varcounter],nbins,density=1,weights = bb_vs_bb_weights, alpha=0.8,linewidth=1.5,color='r',label='bbjets',  histtype='step' )
                plt.hist(dijet[:,varcounter],nbins,density=1,weights = di_vs_bb_weights, alpha=0.8,linewidth=1.5,color='b',label='dijet',  histtype='step' )
                #plt.hist(ttbar[:,varcounter]/1e3,nbins,normed=1,weights = tt_vs_bb_weights, alpha=0.3,linewidth=1.5,color='g',label='ttbar',   histtype='step' )
          	#plt.set_yscale('log')
                plt.title(variablelist[varcounter])
                plt.yscale('log')
                plt.ylabel("A.U.")
                plt.legend()
                plt.savefig(variablelist[varcounter]+'_bfs.pdf')
		plt.close()
		#plt.show()
    #fig, ax = plt.subplots()
    #if 1:
