import math
import pandas as pd
from pprint import pprint
import numpy as np
from plotnine import *
import sys

results_df = pd.read_csv("../merged_data.csv")
results_df = results_df.drop('Unnamed: 0', 1)
results_df = results_df.drop("Unnamed: 0_x", 1)

results_df = results_df.rename(columns={"id":"site_id"})
results_df['type_t'] = "BPR"

unique_locations = results_df.Site.unique()
unique_ids = results_df.site_id.unique()

plot_types = ["bimodal_distribution", "capacity", "density_plot", "saturation-delay", "speed-saturation"]

third_order_poly = lambda n, p: n ** p

for site in unique_locations:
	tmp_df = results_df[results_df.Site == site]
	tmp_df.to_excel("../tmp/site_"+str(site)+".xlsx")

for location in unique_locations:
	tmp_df = results_df[results_df.site_id == location]
	tmp_df.to_excel("../tmp/location"+str(location)+".xlsx")

for site in unique_locations:

		print("Working on site: {}".format(site))
		
		tmp_df = results_df[results_df.Site == site]
		alt_df = results_df[results_df.Site == site]

		tmp_df = results_df[results_df.Site == site]
		
		# This uses a forked version of ggplot to plot a 3order polylnomial fit
		p = ggplot(aes(x="saturation",y="time_norm_ratio",color='site_id'),data =tmp_df) + geom_point() + labs(y="Time (t/to)",x="Saturation") \
		+ geom_line(aes(x="saturation",y="BPR_time_norm_ratio"),show_legend=True) \
		+ stat_smooth(method='lm') + ggtitle("Saturation delay for Site " + str(site)) \
		+ ggtitle("Saturation delay for Site " + str(location))

		p.save("../functions/saturation_delay/site/saturation_delay_site_{}.png".format(str(site)))

for location in unique_ids:	

		print("Working on location: {}".format(location))
		
		tmp_df = results_df[results_df.site_id == location]

		# This uses a forked version of ggplot to plot a 3order polylnomial fit
		p = ggplot(aes(x="saturation",y="time_norm_ratio",color='site_id'),data =tmp_df) + geom_point() + labs(y="Time (t/to)",x="Saturation") \
		+ geom_line(aes(x="saturation",y="BPR_time_norm_ratio"),show_legend=True) \
		+ stat_smooth(method='lm') + ggtitle("Saturation delay for location " + str(site)) \
		+ ggtitle("Saturation delay for Site " + str(location))
		
		p.save("../functions/saturation_delay/location/saturation_delay_location_{}.png".format(str(location)))
