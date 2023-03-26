
import pandas as pd

import matplotlib.pyplot as plt

d = pd.read_csv('data/air_quality.csv', index_col=0, parse_dates=True)
d.head()  # first column to index, dates as timestamp objects.

d.plot() # by default numeric data as lines.
d.station_paris.plot()
d.plot.scatter(x='station_london', y='station_paris', alpha=0.5)
d.plot.box()
# there are more type of plots available:
[
    method_name
    for method_name in dir(d.plot)
    if not method_name.startswith("_")
]

# Separate subplots for each of the data columns:
d.plot.area(figsize=(12, 4), subplots=True)

# further customize and save plot
fig, axs = plt.subplots(figsize=(12, 4))  # Create an empty Matplotlib Figure and Axes
d.plot.area(ax=axs)  # Use pandas to put the area plot on the prepared Figure/Axes
axs.set_ylabel("NO$_2$ concentration")  # Do any Matplotlib customization you like
fig.savefig('data/airquality_plot.png')  # Save the Figure/Axes using the existing Matplotlib method.
plt.show()  # Display the plot