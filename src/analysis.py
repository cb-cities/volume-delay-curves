import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import sys

data = pd.read_csv("../merged_data.csv")

print(data.head())

# find all sites
unique_sites = data['Site'].unique()

for site in unique_sites:
	
	print "Working on site ", str(site)

	sample = data[data.Site == site]

	# Saturation and time
	y_sat = sample['saturation'].as_matrix()

	x_time = sample['time_norm_ratio'].as_matrix()

	z = np.polyfit(x_time,y_sat, 3)

	f = np.poly1d(z)

	print type(f)
	
	print f
	
	sys.exit(1)

	# calculate new x's and y's
	x_new = np.linspace(x_time[0], x_time[-1], 50)
	y_new = f(x_new)

	plt.plot(x_time,y_sat,'o', x_new, y_new)
	plt.xlim([x_time[0]-1, x_time[-1] + 1 ])
	plt.show()
	
	sys.exit(1)

