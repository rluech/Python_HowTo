"""
ShoeCo Inc., a shoe manufacturer, wants to understand if their newest shoe, the ​RunPro 3000​, makes runners faster. In order to do so, they convinced a nearby marathon to provide 50% of runners with a free pair of ​RunPro3000​s as long as they wore them during the race. ShoeCo Inc. has now asked you to analyze their data and see if the shoes actually made a difference.

Attached are two csv files and below are the file names and fields included therein:
runner_attributes.csv

    ageClass: The decade corresponding to the runner’s age (e.g., 20, 30, 40)
    sex: The runner’s gender
    nationality: A 3-letter code corresponding to the runner’s nationality
    treatment: Whether the runner was given the ​RunPro 3000​s (Treatment) or not (Control)
    unique_id: The runner’s unique ID

marathon_times.csv

    netTime: The number of seconds between the runner’s race start and race finish
    clockTime: The marathon clock time (from official race start to runner's race finish)

Please use the attached data and let ShoeCo Inc. know whether or not the ​RunPro 3000​s actually had a statistically significant impact on runner performance. If so, is the impact on performance the same for all runners? If not, how does the impact of the shoes vary as a function of the runner’s attributes. Can you use the runner’s attributes (including whether or not they are wearing ​RunPro3000​s) to predict how quickly they will finish the marathon?

Answer the questions. Try to explain your results as well as you can with plain english, equations, and data visualizations. 
"""

# Minimum sufficient libraries and data are loaded for you
import pandas as pd
import matplotlib.pyplot as plt

# Load runner attributes

orig_url='https://drive.google.com/file/d/1EJFQMCVp4ctvI8VX6Zi9dlyhWiGJlm0y/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url='https://drive.google.com/uc?export=download&id=' + file_id

df_attributes = pd.read_csv(dwn_url)
df_attributes

orig_url='https://drive.google.com/file/d/1M8_m7ECPKhMohapbfzOoT3Ptf_7gpD8T/view?usp=sharing'
file_id = orig_url.split('/')[-2]
dwn_url='https://drive.google.com/uc?export=download&id=' + file_id

df_times = pd.read_csv(dwn_url)
df_times

"""
Perform simple descriptive data analysis: check how many rows and columns in both data files. Are there any missing values, duplicates, etc. 
"""


"""
Merge the dataframes, show first 5 rows
"""

"""
Check The Average Times from the Runners with and without RunPro 3000. Which group is faster?
"""


"""
Is there any age category that benefits the most by using RunPro 3000?
"""

"""
Do men or women benefit the most by using RunPro 3000?
"""

"""
Is there any improvement with RunPro 3000 runners based on nationality?
"""

"""
Find the effect of RunPro 3000 on the top-5 most populated groups based on nationality
"""


"""
Make a histogram of net times for lucky owners of RunPro 3000 and those in control group on the same figure.
How would you interpret the plot?

Hint: use plt.hist 
"""

"""
Run statistical test to compare netTimes for treatment and control groups 
"""


"""
Can you use the runner’s attributes (including whether or not they are wearing ​RunPro3000​s) to predict how quickly they will finish the marathon
"""
