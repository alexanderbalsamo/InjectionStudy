# Comparing second best Antenna Factors with 50% and 90% 
# exclusion distances for PyGRB Workflows in O3

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# GRBs and their respective offtrial exclusion distances
grb190407788Ex90 = [58.0739684979, 58.0739684979, 57.8582407059, 57.8367294722, 57.582307283, 57.7639043439]
grb190407788Ex90Ave = np.mean(grb190407788Ex90)
grb190407788Ex50 = [95.1075546321, 95.0590004058, 95.069934546, 94.794141491, 95.1156949319, 95.0052482579]
grb190407788Ex50Ave = np.mean(grb190407788Ex50)

grb190420981Ex90 = [78.9189782209, 78.9347588971, 79.0624982419, 79.1015907893, 78.8601544349, 78.9680838613]
grb190420981Ex90Ave = np.mean(grb190420981Ex90)
grb190420981Ex50 = [144.196384024, 143.53257576, 143.955000619, 143.929941906, 143.854410956, 143.668717867]
grb190420981Ex50Ave = np.mean(grb190420981Ex50)

grb190427AEx90 = [125.290661493, 125.162669452, 125.23363378, 125.185202361, 125.186835581, 125.230840673]
grb190427AEx90Ave = np.mean(grb190427AEx90)
grb190427AEx50 = [167.421552379, 168.385586992, 165.023221877, 166.824095138, 167.298456604, 165.772849882]
grb190427AEx50Ave = np.mean(grb190427AEx50)

grb190504678Ex90 = [84.7970065683, 85.6394057924, 74.9306450764, 83.8168216099, 84.4453804373, 84.4733882894]
grb190504678Ex90Ave = np.mean(grb190504678Ex90)
grb190504678Ex50 = [130.968184656, 141.978022816, 114.17174205, 127.188891061, 130.128475765, 130.424610977]
grb190504678Ex50Ave = np.mean(grb190504678Ex50)

grb190505051Ex90 = [59.2650693324, 58.9938460961, 58.8761077617, 59.1041681574, 59.2424362519, 58.983036454]
grb190505051Ex90Ave = np.mean(grb190505051Ex90)
grb190505051Ex50 = [90.8523804074, 90.0808373656, 90.2551729781, 91.0024951644, 90.9480688876, 90.1013151282]
grb190505051Ex50Ave = np.mean(grb190505051Ex50)

grb190510430Ex90 = [140.788006414, 140.672076357, 146.615053051, 140.723804459, 139.507397903, 146.893801366]
grb190510430Ex90Ave = np.mean(grb190510430Ex90)
grb190510430Ex50 = [204.368585557, 204.60417658, 204.491964182, 203.917170216, 201.605975919, 204.397186686]
grb190510430Ex50Ave = np.mean(grb190510430Ex50)

grb190525032Ex90 = [175.666156463, 176.289669494, 179.220402909, 176.375084822, 176.303664093, 176.125667288]
grb190525032Ex90Ave = np.mean(grb190525032Ex90)
grb190525032Ex50 = [248.274677669, 248.087036138, 251.406929983, 248.454198727, 248.052331468, 247.555019585]
grb190525032Ex50Ave = np.mean(grb190525032Ex50)

grb190531568Ex90 = [35.0456329094, 35.0743163292, 35.1358308549, 35.0397784944, 35.037751305, 35.0042293797]
grb190531568Ex90Ave = np.mean(grb190531568Ex90)
grb190531568Ex50 = [81.4922076577, 81.5613669226, 81.564405448, 81.6078477463, 81.6083137856, 81.5909433837]
grb190531568Ex50Ave = np.mean(grb190531568Ex50)

grb190601325Ex90 = [140.00708691, 140.337347994, 165.402512783, 164.659130229, 139.803252806, 165.287503212]
grb190601325Ex90Ave = np.mean(grb190601325Ex90)
grb190601325Ex50 = [209.563141145, 203.459023376, 216.845688259, 216.872718702, 209.253849518, 216.642409649]
grb190601325Ex50Ave = np.mean(grb190601325Ex50)

grb190610AEx90 = [47.0337110827, 47.1246822252, 47.0478595917, 47.0023691352, 47.1449571779, 47.0767943548]
grb190610AEx90Ave = np.mean(grb190610AEx90)
grb190610AEx50 = [76.8327247615, 76.9949609029, 77.0208069499, 76.8028523793, 76.8963655462, 77.1317001995]
grb190610AEx50Ave = np.mean(grb190610AEx50)

grb190610834Ex90 = [58.5210670071, 58.6285952842, 56.0169730722, 56.0806722495, 58.2647814324, 56.0490345085]
grb190610834Ex90Ave = np.mean(grb190610834Ex90)
grb190610834Ex50 = [95.6078055509, 95.4941694612, 95.2606717454, 95.2822389402, 95.423131478, 95.3991233954]
grb190610834Ex50Ave = np.mean(grb190610834Ex50)

grb190923617Ex90 = [70.7934707695, 70.7475332236, 70.7651863329, 70.8399378201, 70.6572973534, 70.7524014977]
grb190923617Ex90Ave = np.mean(grb190923617Ex90)
grb190923617Ex50 = [124.703967018, 125.14976635, 125.007522407, 125.289738169, 124.537547896, 124.604477681]
grb190923617Ex50Ave = np.mean(grb190923617Ex50)

grb190830264Ex90 = [201.629840863, 243.757112603, 201.468484686, 245.37314732, 202.025176469, 201.667515891]
grb190830264Ex90Ave = np.mean(grb190830264Ex90)
grb190830264Ex50 = [363.709170248, 380.299062461, 373.556339521, 381.327884153, 374.296516215, 363.646685019]
grb190830264Ex50Ave = np.mean(grb190830264Ex50)

grb190810675Ex90 = [72.5523257801, 72.5772311531, 67.2729618409, 72.5307173763, 72.6462394817, 72.4995151665]
grb190810675Ex90Ave = np.mean(grb190810675Ex90)
grb190810675Ex50 = [133.450928141, 134.18284622, 131.174220234, 132.605193643, 133.323083282, 133.823593273]
grb190810675Ex50Ave = np.mean(grb190810675Ex50)

grb190804058Ex90 = [95.1660641801, 94.3851561156, 95.1446587501, 95.0455621528, 94.96818856, 95.0309406605]
grb190804058Ex90Ave = np.mean(grb190804058Ex90)
grb190804058Ex50 = [156.134247396, 154.531272714, 151.815778051, 152.128553103, 157.523373674, 155.469427378]
grb190804058Ex50Ave = np.mean(grb190804058Ex50)

grb190712018Ex90 = [164.563340999, 164.413460377, 196.340004062, 164.346134717, 163.693189387, 194.70976841]
grb190712018Ex90Ave = np.mean(grb190712018Ex90)
grb190712018Ex50 = [310.521241229, 313.363710565, 318.008571456, 309.584920689, 310.623511914, 317.609431939]
grb190712018Ex50Ave = np.mean(grb190712018Ex50)

grb190630257Ex90 = [18.7478032145, 18.7317942818, 18.7748688184, 18.7695467427, 18.7411067987, 18.8207082041]
grb190630257Ex90Ave = np.mean(grb190630257Ex90)
grb190630257Ex50 = [56.4430628056, 56.4161573669, 56.4723272449, 56.4583530779, 56.5087388118, 55.9429713745]
grb190630257Ex50Ave = np.mean(grb190630257Ex50)

grb190627AEx90 = [83.8898857804, 82.8455319013, 83.2343667531, 83.4348118318, 82.881823252, 83.2118666278]
grb190627AEx90Ave = np.mean(grb190627AEx90)
grb190627AEx50 = [129.502740138, 129.266097925, 129.533891581, 129.27508026, 129.521696702, 129.361246287]
grb190627AEx50Ave = np.mean(grb190627AEx50)

grb190606080Ex90 = [39.9553023055, 41.3924648021, 41.3132117043, 41.875382478, 46.9149000392, 41.2000847792]
grb190606080Ex90Ave = np.mean(grb190606080Ex90)
grb190606080Ex50 = [76.6242650259, 77.8203279611, 78.2143056709, 78.6147960866, 78.9679943512, 77.2008839935]
grb190606080Ex50Ave = np.mean(grb190606080Ex50)

grb190515190Ex90 = [51.7566934254, 51.5332477596, 51.5124825964, 51.938127326, 51.4767634104, 51.4481488493]
grb190515190Ex90Ave = np.mean(grb190515190Ex90)
grb190515190Ex50 = [80.0835722045, 80.1329221853, 80.0196807774, 80.1781682271, 80.0941606553, 79.9877131221]
grb190515190Ex50Ave = np.mean(grb190515190Ex50)

# Lists of information with all GRBs
name = 		 ["GRB190407788",      	"GRB190420981", "GRB190427A", "GRB190504678", "GRB190505051", "GRB190510430", "GRB190525032", "GRB190601325", "GRB190610A", "GRB190610834", "GRB190830264", "GRB190810675", "GRB190804058", "GRB190712018", "GRB190630257", "GRB190627A", "GRB190606080", "GRB190515190"]
antenna1Best = [0.919, 0.772, 0.983, 0.946, 0.525, 0.582, 0.813, 0.690, 0.302, 0.880, 0.953, 0.645, 0.800, 0.971, 0.448, 0.452, 0.613, 0.488]
antenna2Best = [0.506, 0.720, 0.504, 0.315, 0.500, 0.500, 0.651, 0.523, 0.202, 0.511, 0.915, 0.501, 0.760, 0.800, 0.285, 0.316, 0.199, 0.412]
exclu90Ave = [grb190407788Ex90Ave, 	grb190420981Ex90Ave, grb190427AEx90Ave, grb190504678Ex90Ave, grb190505051Ex90Ave, grb190510430Ex90Ave, grb190525032Ex90Ave, grb190601325Ex90Ave, grb190610AEx90Ave, grb190610834Ex90Ave, grb190830264Ex90Ave, grb190810675Ex90Ave, grb190804058Ex90Ave, grb190712018Ex90Ave, grb190630257Ex90Ave, grb190627AEx90Ave, grb190606080Ex90Ave, grb190515190Ex90Ave]
exclu90err = [4.905496342543896,    10.1477956793,		 7.72280287013,		4.044501064003285,   2.66183424, 		  15.137899695517495,  4.800286616443967,	7.860245624562807,	 2.88789821644,	 	5.70422303245,		 15.22435768238921,	  3.7141618209116625,  24.726406802, 		5.78848165687765,	 3.3543675352,		  5.7933757022362995,2.2537173332640363,  4.19587506617	   ]
exclu50Ave = [grb190407788Ex50Ave, 	grb190420981Ex50Ave, grb190427AEx50Ave, grb190504678Ex50Ave, grb190505051Ex50Ave, grb190510430Ex50Ave, grb190525032Ex50Ave, grb190601325Ex90Ave, grb190610AEx50Ave, grb190610834Ex50Ave, grb190830264Ex50Ave, grb190810675Ex50Ave, grb190804058Ex50Ave, grb190712018Ex50Ave, grb190630257Ex50Ave, grb190627AEx50Ave, grb190606080Ex50Ave, grb190515190Ex50Ave]
exclu50err = [4.937500505876478,    5.04894308235,		 6.30382394612,		2.9702652116037744,  3.87321224862, 	  3.8807160072599536,  6.373142326368604,   6.836912226751878,	 2.54026431952,	 	3.66778590264,		 6.405721498179706,	  4.688381167905543,   11.4561972396,		6.170499188231567,	 2.32210715364,		  2.1957950900444163,3.4492449785291357,  3.06047056018	   ]
slope1_90, intercept1_90, r1_90, p1_90, stdErr1_90 = stats.linregress(antenna1Best, exclu90Ave)
slope2_90, intercept2_90, r2_90, p2_90, stdErr2_90 = stats.linregress(antenna2Best, exclu90Ave)
slope1_50, intercept1_50, r1_50, p1_50, stdErr1_50 = stats.linregress(antenna1Best, exclu50Ave)
slope2_50, intercept2_50, r2_50, p2_50, stdErr2_50 = stats.linregress(antenna2Best, exclu50Ave)
print "r-squared (antenna1xExclu90): ", r1_90**2
print "r-squared (antenna2xExclu90): ", r2_90**2
print "r-squared (antenna1xExclu50): ", r1_50**2
print "r-squared (antenna2xExclu50): ", r2_50**2

# Plots
fig90, ax90 = plt.subplots()
ax90.errorbar(antenna1Best, exclu90Ave, yerr=exclu90err, fmt='o')
ax90.set(xlabel='antenna Factors', ylabel='Exclusion Distance 90% (Mpc)',
       title='1st Best Antenna Factors vs Offtrial Exclusion Distance 90%')
ax90.grid()
fig90.savefig(fname='antFact1vsExDist90.png')

fig90_2, ax90_2 = plt.subplots()
ax90_2.errorbar(antenna2Best, exclu90Ave, yerr=exclu50err, fmt='o')
ax90_2.set(xlabel='antenna Factors', ylabel='Exclusion Distance 90% (Mpc)',
       title='2nd Best Antenna Factors vs Offtrial Exclusion Distance 90%')
ax90_2.grid()
fig90_2.savefig(fname='antFact2vsExDist90.png')

fig50, ax50 = plt.subplots()
ax50.errorbar(antenna1Best, exclu50Ave, yerr=exclu90err, fmt='o')
ax50.set(xlabel='antenna Factors', ylabel='Exclusion Distance 50% (Mpc)',
       title='1st Best Antenna Factors vs Offtrial Exclusion Distance 50%')
ax50.grid()
fig50.savefig(fname='antFact1vsExDist50.png')

fig50_2, ax50_2 = plt.subplots()
ax50_2.errorbar(antenna2Best, exclu50Ave, yerr=exclu50err, fmt='o')
ax50_2.set(xlabel='antenna Factors', ylabel='Exclusion Distance 50% (Mpc)',
       title='2nd Best Antenna Factors vs Offtrial Exclusion Distance 50%')
ax50_2.grid()
fig50_2.savefig(fname='antFact2vsExDist50.png')

# Show Plots
plt.show()