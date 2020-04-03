import matplotlib.pyplot as plt
import numpy as np

def errorCalc(mean, std, DIST):
	dummyList = []
	for i in range(len(mean)):
		d = mean[0] - DIST
		e = std[i]
		newErr = (d**2+e**2)**(1./2.)
		dummyList.append(newErr)
	return dummyList

#test
################## NSNS #####################
# NSNS values 90% Exclusion Distance
injcontrolNSNS_90 = [78.9189782209, 78.9347588971, 79.0624982419, 79.1015907893, 78.8601544349, 78.9680838613]
inj100NSNS_90 = [94.9438081033, 95.2376446743, 94.7819281981, 94.7663454159, 94.8923562341, 95.4277095035]
inj90NSNS_90 = [92.9165926058, 94.3025193943, 94.0469681411, 94.5478369454, 94.3640703452, 94.5839047136]
inj80NSNS_90 = [94.0069271597, 94.2031136452, 93.5605162563, 94.0053867499, 94.2461926244, 94.346149776]
inj70NSNS_90 = [100.434236299, 100.585763286, 100.129131498, 100.142645371, 100.448732085, 100.025351176]
inj60NSNS_90 = [87.0269604652, 86.9341466085, 87.1095673338, 87.1081618228, 87.1429810745, 87.0062476161]
inj50NSNS_90 = [72.9300087041, 72.7428773732, 73.0010302719, 72.8377582871, 72.5678715571, 72.6968309418]
inj40NSNS_90 = [84.5630374059, 83.5577502632, 83.7293114455, 83.6737690712, 83.3168917721, 83.0745571151]
inj30NSNS_90 = [45.6759170704, 46.1483939185, 46.3503417378, 46.5123626662, 46.5367393911, 47.1773016398]
inj20NSNS_90 = [21.7569936113, 21.7243006899, 21.72824956, 21.6071384198, 21.5124136015, 21.5534630033]

# NSNS values 50% Exclusion Distance
injcontrolNSNS_50 = [144.196384024, 143.53257576, 143.955000619, 143.929941906, 143.854410956, 143.668717867]
inj100NSNS_50 = [140.746955652, 140.852561997, 140.613756358, 140.253626339, 140.595961996, 140.433665792]
inj90NSNS_50 = [154.547375392, 154.419120006, 155.558067461, 154.898771144, 155.561762223, 155.626543739]
inj80NSNS_50 = [152.568418535, 152.687889745, 152.680025048, 153.09578581, 152.358705009, 152.691744584]
inj70NSNS_50 = [134.897211186, 134.909775946, 135.34890953, 135.852284649, 135.351269819, 134.992696178]
inj60NSNS_50 = [147.028421516, 146.951405519, 147.002903404, 146.690418345, 147.40972375, 147.273277901]
inj50NSNS_50 = [137.995878226, 138.630390394, 138.747549894, 138.533578744, 138.453785474, 138.467605938]
inj40NSNS_50 = [134.707229672, 134.695638869, 134.705626548, 134.863320032, 135.080932747, 134.732276292]
inj30NSNS_50 = [132.090838733, 132.332561132, 132.061494494, 132.116456628, 132.511220957, 132.375702208]
inj20NSNS_50 = [131.005586137, 130.889204683, 130.838763353, 130.842364151, 130.753977592, 130.608941518]
inj10NSNS_50 = [169.164853127, 172.803736053, 167.152872584, 166.230209599, 167.708701474, 167.319411121]


############## NSBH Align ###################
# NSBH Align values 90% Exclusion Distance
injcontrolNSBHAlign_90 = [160.86881326, 160.68696424, 160.960200364, 160.573390316, 161.185777892, 160.2643286]
inj100NSBHAlign_90 = [170.546104743, 170.693962943, 170.767397277, 170.625265781, 170.715042494, 170.81619003]
inj95NSBHAlign_90 = [166.591174158, 166.091603646, 166.359440313, 166.128574857, 166.119115893, 166.125553561]
inj90NSBHAlign_90 = [121.317462921, 121.414330282, 121.230589511, 121.638331433, 121.475590308, 120.958011617]
inj85NSBHAlign_90 = [156.709190679, 157.053546857, 157.466613771, 157.033615861, 156.446903864, 157.235943722]
inj80NSBHAlign_90 = [134.3886325, 133.735584967, 133.840012002, 132.995695628, 133.294492079, 133.460211603]
inj75NSBHAlign_90 = [114.140237297, 114.166683341, 114.141612019, 114.102475657, 114.743108379, 114.11919726]
inj70NSBHAlign_90 = [168.358604117, 168.346301326, 168.28775431, 168.31662285, 168.255323875, 168.591390597]
inj65NSBHAlign_90 = [141.907273216, 142.415684391, 142.139697006, 141.774343112, 142.014776864, 142.313758361]
inj60NSBHAlign_90 = [157.429672296, 157.575053542, 156.689224179, 156.875195586, 157.219274753, 157.205556119]
inj55NSBHAlign_90 = []
inj50NSBHAlign_90 = [95.9897934818, 95.991710212, 96.0710748837, 96.0876973685, 96.1263858524, 96.0416594833]

# NSBH Align values 50% Exclusion Distance
injcontrolNSBHAlign_50 = [255.465800518, 256.188320438, 256.354669215, 256.196380005, 255.597874487, 256.673287845]
inj100NSBHAlign_50 = [263.771339203, 263.829231385, 263.608903423, 263.925529938, 263.754612308, 264.327239833]
inj95NSBHAlign_50 = [269.319731386, 269.441853121, 268.694646179, 269.110023808, 268.531815415, 268.681358188]
inj90NSBHAlign_50 = [253.67608349, 253.869224331, 253.332072341, 253.970907972, 253.927776798, 253.288728357]
inj85NSBHAlign_50 = [259.407024144, 259.606025422, 259.341036459, 259.692875034, 259.502456784, 259.365432203]
inj80NSBHAlign_50 = [264.545677791, 263.460035374, 263.033317078, 263.842930221, 264.636577087, 263.497175047]
inj75NSBHAlign_50 = [253.866551685, 253.448838673, 252.419096833, 253.430877641, 253.475991818, 253.556063152]
inj70NSBHAlign_50 = [241.0425643, 241.405041037, 241.151984904, 241.328950835, 241.316205913, 241.261647237]
inj65NSBHAlign_50 = [249.133777533, 248.774567077, 249.261592959, 248.972028909, 248.748127528, 249.382974208]
inj60NSBHAlign_50 = [248.80917153, 249.706502398, 249.395092323, 249.181214875, 248.914051105, 249.268473867]
inj55NSBHAlign_50 = []
inj50NSBHAlign_50 = [228.976784795, 229.204054574, 228.881380385, 229.427981036, 229.093677321, 229.081976188]


############## NSBH Precess #################
# NSBH Precess values 90% Exclusion Distance
injcontrolNSBHPrecess_90 = [143.153572038, 142.534796467, 143.069365793, 142.528709605, 142.734505243, 143.05024251]
inj100NSBHPrecess_90 = [110.674653605, 110.482226622, 110.708038496, 110.582831001, 110.128173993, 110.740310794]
inj95NSBHPrecess_90 = [115.137747459, 114.44096906, 109.410922495, 109.715321309, 109.617922471, 109.388621958]
inj90NSBHPrecess_90 = [49.2944921555, 49.5644721691, 49.3362856761, 49.6773247507, 49.5398661328, 49.5240325102]
inj85NSBHPrecess_90 = [115.712311069, 115.737523699, 115.923619243, 116.113475158, 115.875926262, 116.055555176]
inj80NSBHPrecess_90 = [73.4678799491, 73.6016576262, 73.480217801, 73.6684552412, 73.717399801, 73.6591445504]
inj75NSBHPrecess_90 = [132.319632063, 134.972218812, 132.847411902, 132.95587726, 132.815854872, 132.761058784]
inj70NSBHPrecess_90 = [111.750086406, 112.607375163, 111.085905848, 111.001119869, 112.762547703, 111.694401821]
inj65NSBHPrecess_90 = [102.799582707, 102.818548177, 102.504357699, 102.636198195, 102.901005601, 103.198587757]
inj60NSBHPrecess_90 = [117.463282587, 117.173727313, 117.44886845, 117.353896649, 117.533948566, 117.867635299]
inj55NSBHPrecess_90 = []
inj50NSBHPrecess_90 = [41.4477585094, 41.5584046895, 41.4561050812, 41.3990758685, 41.583526891, 41.4832734575]

# NSBH Precess values 50% Exclusion Distance
injcontrolNSBHPrecess_50 = [200.264134725, 200.455270271, 200.469943686, 200.560334116, 200.723492269, 200.114008841]
inj100NSBHPrecess_50 = [206.764778991, 206.550112434, 206.56373623, 206.411632091, 206.564207116, 206.733428984]
inj95NSBHPrecess_50 = [230.217143222, 229.95352822, 229.635230369, 230.013637882, 230.146358413, 229.997410035]
inj90NSBHPrecess_50 = [229.076115063, 229.824143363, 229.485469227, 229.290808875, 230.254034613, 229.110928524]
inj85NSBHPrecess_50 = [237.428890094, 237.167405732, 236.493366616, 236.457322927, 236.405691677, 236.420163565]
inj80NSBHPrecess_50 = [223.51161644, 222.69842809, 223.40982496, 223.016935308, 222.828368896, 223.178595771]
inj75NSBHPrecess_50 = [231.947970648, 231.942876541, 231.767103927, 231.659578728, 232.517420501, 232.058782819]
inj70NSBHPrecess_50 = [219.475721679, 216.816784008, 216.908322284, 217.019302192, 219.275759198, 218.069638064]
inj65NSBHPrecess_50 = [208.875462535, 209.951957656, 210.732083491, 210.213960886, 209.144535521, 208.812319468]
inj60NSBHPrecess_50 = [206.818873182, 206.376572899, 206.493992063, 206.767272214, 206.392497512, 206.77742594]
inj55NSBHPrecess_50 = []
inj50NSBHPrecess_50 = [216.431939253, 216.100003704, 215.894891021, 216.838876715, 216.141174189, 216.749881009]

############### Injections ################
nsnsInj = 4000
nsbhAlignInj = 12500
nsbhPrecessInj = 12500

################ Values #################
nsns_90_mean = [np.mean(inj100NSNS_90), np.mean(inj90NSNS_90), np.mean(inj80NSNS_90), np.mean(inj70NSNS_90), np.mean(inj60NSNS_90), np.mean(inj50NSNS_90), np.mean(inj40NSNS_90), np.mean(inj30NSNS_90), np.mean(inj20NSNS_90)]
nsns_90_std = [11.063479404361873, 3.700565758284695, 3.6692927735743956, 6.65511020741, 10.6678190601, 9.72355054478, 6.34528534050268, 5.865938840354687, 10.64974986085202]
nsns_90_err = errorCalc(nsns_90_mean, nsns_90_std, np.mean(injcontrolNSNS_90))
nsnsNumInj_90 = [1*nsnsInj, 0.9*nsnsInj, 0.8*nsnsInj, 0.7*nsnsInj, 0.6*nsnsInj, 0.5*nsnsInj, 0.4*nsnsInj, 0.3*nsnsInj, 0.2*nsnsInj]
nsns_50_mean = [np.mean(inj100NSNS_50), np.mean(inj90NSNS_50), np.mean(inj80NSNS_50), np.mean(inj70NSNS_50), np.mean(inj60NSNS_50), np.mean(inj50NSNS_50), np.mean(inj40NSNS_50), np.mean(inj30NSNS_50), np.mean(inj20NSNS_50), np.mean(inj10NSNS_50)]
nsns_50_std = [6.738043973967401, 4.711676157772397, 5.301722593946216, 10.7553460849, 4.97605303394, 33.5169350083, 4.829679075135576, 4.176415388028511, 5.89478930396605, 3.341110625402934]
nsns_50_err = errorCalc(nsns_50_mean, nsns_50_std, np.mean(injcontrolNSNS_50))
nsnsNumInj_50 = [1*nsnsInj, 0.9*nsnsInj, 0.8*nsnsInj, 0.7*nsnsInj, 0.6*nsnsInj, 0.5*nsnsInj, 0.4*nsnsInj, 0.3*nsnsInj, 0.2*nsnsInj, 0.1*nsnsInj]

nsbhAlign_90_mean = [np.mean(inj100NSBHAlign_90), np.mean(inj95NSBHAlign_90), np.mean(inj90NSBHAlign_90), np.mean(inj85NSBHAlign_90), np.mean(inj80NSBHAlign_90), np.mean(inj75NSBHAlign_90), np.mean(inj70NSBHAlign_90), np.mean(inj65NSBHAlign_90), np.mean(inj60NSBHAlign_90), np.mean(inj50NSBHAlign_90)]
nsbhAlign_90_std = [13.3514417736463, 6.763015800603423, 10.816517042851002, 11.343711654851754, 10.276219128, 31.0497580382, 9.75870059841632, 14.110640287440887, 7.52688093747872, 9.27830349471]
nsbhAlign_90_err = errorCalc(nsbhAlign_90_mean, nsbhAlign_90_std, np.mean(injcontrolNSBHAlign_90))
nsbhAlign_50_mean = [np.mean(inj100NSBHAlign_50), np.mean(inj95NSBHAlign_50), np.mean(inj90NSBHAlign_50), np.mean(inj85NSBHAlign_50), np.mean(inj80NSBHAlign_50), np.mean(inj75NSBHAlign_50), np.mean(inj70NSBHAlign_50), np.mean(inj65NSBHAlign_50), np.mean(inj60NSBHAlign_50), np.mean(inj50NSBHAlign_50)]
nsbhAlign_50_std = [7.761793772040417, 12.684935353607644, 9.207894303406931, 10.026442593547355, 9.53740464565, 11.5537125999, 6.56585706910925, 17.679110365465252, 41.704807443853305, 99.1745945704]
nsbhAlign_50_err = errorCalc(nsbhAlign_50_mean, nsbhAlign_50_std, np.mean(injcontrolNSBHAlign_50))
nsbhAlignNumInj = [1*nsbhAlignInj, 0.95*nsbhAlignInj, 0.9*nsbhAlignInj, 0.85*nsbhAlignInj, 0.8*nsbhAlignInj, 0.75*nsbhAlignInj, 0.7*nsbhAlignInj, 0.65*nsbhAlignInj, 0.6*nsbhAlignInj, 0.5*nsbhAlignInj]

nsbhPrecess_90_mean = [np.mean(inj100NSBHPrecess_90), np.mean(inj95NSBHPrecess_90), np.mean(inj90NSBHPrecess_90), np.mean(inj85NSBHPrecess_90), np.mean(inj80NSBHPrecess_90), np.mean(inj75NSBHPrecess_90), np.mean(inj70NSBHPrecess_90), np.mean(inj65NSBHPrecess_90), np.mean(inj60NSBHPrecess_90), np.mean(inj50NSBHPrecess_90)]
nsbhPrecess_90_std = [11.380450987844023, 9.288725373870486, 3.9526855403372867, 6.5316522005021405, 21.5440835645, 12.0579867157, 6.8773294132981055, 10.118444773002604, 19.30353658535733, 10.8410448196]
nsbhPrecess_90_err = errorCalc(nsbhPrecess_90_mean, nsbhPrecess_90_std, np.mean(injcontrolNSBHPrecess_90))
nsbhPrecess_50_mean = [np.mean(inj100NSBHPrecess_50), np.mean(inj95NSBHPrecess_50), np.mean(inj90NSBHPrecess_50), np.mean(inj85NSBHPrecess_50), np.mean(inj80NSBHPrecess_50), np.mean(inj75NSBHPrecess_50), np.mean(inj70NSBHPrecess_50), np.mean(inj65NSBHPrecess_50), np.mean(inj60NSBHPrecess_50), np.mean(inj50NSBHPrecess_50)]
nsbhPrecess_50_std = [7.079303364544146, 5.317147012680572, 11.604404282417994, 10.925635874610593, 11.0296778531, 15.9578893375, 8.399006032298338, 11.222149670766692, 17.063995734044685, 11.84361285]
nsbhPrecess_50_err = errorCalc(nsbhPrecess_50_mean, nsbhPrecess_50_std, np.mean(injcontrolNSBHPrecess_50))
nsbhPrecessNumInj = [1*nsbhPrecessInj, 0.95*nsbhPrecessInj, 0.9*nsbhPrecessInj, 0.85*nsbhPrecessInj, 0.8*nsbhPrecessInj, 0.75*nsbhPrecessInj, 0.7*nsbhPrecessInj, 0.65*nsbhPrecessInj, 0.6*nsbhPrecessInj, 0.5*nsbhPrecessInj]

# NSNS Plot
x1 = [0,4200]
figNSNS=plt.figure()
axNSNS=figNSNS.gca()

axNSNS.errorbar(nsnsNumInj_90, nsns_90_mean, yerr=nsns_90_err, fmt='o', color='r', label='90% Exclusion Distances')
line90 = axNSNS.axhline(np.mean(injcontrolNSNS_90), dashes=[6,2], label='Accepted 90% Exclusion Distance', color='r')
axNSNS.fill_between(x1, 0.1*np.mean(injcontrolNSNS_90)+np.mean(injcontrolNSNS_90), np.mean(injcontrolNSNS_90) - 0.1*np.mean(injcontrolNSNS_90), alpha=0.1, color='r')

axNSNS.errorbar(nsnsNumInj_50, nsns_50_mean, yerr=nsns_50_err, fmt='o', color='b', label='50% Exclusion Distance')
line50 = axNSNS.axhline(np.mean(injcontrolNSNS_50), dashes=[6,2], label='Accepted 50% Exclusion Distance', color='b')
axNSNS.fill_between(x1, 0.1*np.mean(injcontrolNSNS_50)+np.mean(injcontrolNSNS_50), np.mean(injcontrolNSNS_50) - 0.1*np.mean(injcontrolNSNS_50), alpha=0.1, color='b')

axNSNS.set_xlabel('Number of Injections')
axNSNS.set_ylabel('Exclusion Distance (Mpc)')
axNSNS.set_title('Exclusion Distance vs. Injections for NSNS')
axNSNS.legend(loc='lower right')
axNSNS.set_xlim(0,4200)

figNSNS.savefig(fname='InjVsExDist_NSNS.png')

#NSBHAlign Plot
x2 = [6000,13000]
figNSBHAlign=plt.figure()
axNSBHAlign=figNSBHAlign.gca()

axNSBHAlign.errorbar(nsbhAlignNumInj, nsbhAlign_90_mean, yerr=nsbhAlign_90_err, fmt='o', color='k', label='90% Exclusion Distances')
line90 = axNSBHAlign.axhline(np.mean(injcontrolNSBHAlign_90), dashes=[6,2], label='Accepted 90% Exclusion Distance', color='k')
axNSBHAlign.fill_between(x2, 0.1*np.mean(injcontrolNSBHAlign_90)+np.mean(injcontrolNSBHAlign_90), np.mean(injcontrolNSBHAlign_90) - 0.1*np.mean(injcontrolNSBHAlign_90), alpha=0.1, color='k')

axNSBHAlign.errorbar(nsbhAlignNumInj, nsbhAlign_50_mean, yerr=nsbhAlign_50_err, fmt='o', color='m', label='50% Exclusion Distance')
line50 = axNSBHAlign.axhline(np.mean(injcontrolNSBHAlign_50), dashes=[6,2], label='Accepted 50% Exclusion Distance', color='m')
axNSBHAlign.fill_between(x2, 0.1*np.mean(injcontrolNSBHAlign_50)+np.mean(injcontrolNSBHAlign_50), np.mean(injcontrolNSBHAlign_50) - 0.1*np.mean(injcontrolNSBHAlign_50), alpha=0.1, color='m')

axNSBHAlign.set_xlabel('Number of Injections')
axNSBHAlign.set_ylabel('Exclusion Distance (Mpc)')
axNSBHAlign.set_title('Exclusion Distance vs. Injections for NSBH Aligned')
axNSBHAlign.legend(loc='lower right')
axNSBHAlign.set_xlim(6000,13000)
axNSBHAlign.set_ylim(-10,350)

figNSBHAlign.savefig(fname='InjVsExDist_NSBHAlign.png')

#NSBHPrecess Plot
figNSBHPrecess=plt.figure()
axNSBHPrecess=figNSBHPrecess.gca()

axNSBHPrecess.errorbar(nsbhPrecessNumInj, nsbhPrecess_90_mean, yerr=nsbhPrecess_90_err, fmt='o', color='g', label='90% Exclusion Distances')
line90 = axNSBHPrecess.axhline(np.mean(injcontrolNSBHPrecess_90), dashes=[6,2], label='Accepted 90% Exclusion Distance', color='g')
axNSBHPrecess.fill_between(x2, 0.1*np.mean(injcontrolNSBHPrecess_90)+np.mean(injcontrolNSBHPrecess_90), np.mean(injcontrolNSBHPrecess_90) - 0.1*np.mean(injcontrolNSBHPrecess_90), alpha=0.1, color='g')

axNSBHPrecess.errorbar(nsbhPrecessNumInj, nsbhPrecess_50_mean, yerr=nsbhPrecess_50_err, fmt='o', color='c', label='50% Exclusion Distance')
line50 = axNSBHPrecess.axhline(np.mean(injcontrolNSBHPrecess_50), dashes=[6,2], label='Accepted 50% Exclusion Distance', color='c')
axNSBHPrecess.fill_between(x2, 0.1*np.mean(injcontrolNSBHPrecess_50)+np.mean(injcontrolNSBHPrecess_50), np.mean(injcontrolNSBHPrecess_50) - 0.1*np.mean(injcontrolNSBHPrecess_50), alpha=0.1, color='c')

axNSBHPrecess.set_xlabel('Number of Injections')
axNSBHPrecess.set_ylabel('Exclusion Distance (Mpc)')
axNSBHPrecess.set_title('Exclusion Distance vs. Injections for NSBH Precessing')
axNSBHPrecess.legend(loc='lower right')
axNSBHPrecess.set_xlim(6000,13000)
axNSBHPrecess.set_ylim(0,250)

figNSBHPrecess.savefig(fname='InjVsExDist_NSBHPrecess.png')

# Show Plots
plt.show()
