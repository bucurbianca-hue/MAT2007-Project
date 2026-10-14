# Sleep Health and Lifestyle Dataset
# This script contains the code for two plots, 
# a scatter plot and a boxplot

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

# In this step, the data will be loaded and cleaned
df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv") 
#this loads the csv into a table called df

# The dataset needs to be cleaned because it contains "Normal"
# and "Normal Weight" as two separate labels for the same 
# BMI group. In this step, they will be merged into one group
df["BMI Category"] = df["BMI Category"].replace({"Normal Weight": "Normal"})
#this will rename the "Normal Weight" group to "Normal"

category_order = ["Normal", "Overweight", "Obese"] #this will put the three groups in this order on the plots
df["BMI Category"] = pd.Categorical(df["BMI Category"], category_order, ordered = True)

print(f"Rows: {len(df)}") #this will print how many people are in the dataset
print(df["BMI Category"].value_counts().reindex(category_order), "\n")
#this will print how many people are in each BMI group

# In this step, the first plot will be made
# Plot 1 (boxplot): sleep duration by BMI category 
data_by_group = [df.loc[df["BMI Category"] == cat, "Sleep Duration"].values for cat in category_order]
#this takes the sleep duration values separately for each BMI category

fig, ax = plt.subplots(figsize=(8, 5)) #this creates a new figure which is 8x5 inches
bp = ax.boxplot(data_by_group, patch_artist=True, tick_labels=category_order, medianprops={"color": "black", "linewidth": 1.5})
#this will draw one box per BMI group and make the median line black and thicker

for patch, shade in zip(bp["boxes"], ["#13EAC9", "#C79FEF", "#FF81C0"]):
    patch.set_facecolor(shade)
#this will loop over the three boxes and colors together and fill each box with its matching color

ax.set_title("Sleep Duration by BMI Category") #this plots the title
ax.set_xlabel("BMI Category") #this will plot the x-axis label
ax.set_ylabel("Sleep duration (hours)") #this will plot the y-axis label
ax.grid(axis="y", linestyle="--", alpha=0.5) #this will add a dashed horizontal grid
fig.tight_layout() #this makes sure the labels dont get cut off
fig.savefig("boxplot_sleep_by_bmi.png", dpi=200) #this saves the figure as a png file

for cat in category_order:
    print(f"Median sleep duration ({cat}): " f"{df.loc[df['BMI Category'] == cat, 'Sleep Duration'].median():.1f} h")
#this prints the median sleep duration for each BMI group


# In this step, the second plot will be made
# Plot 2 (scatter): stress level vs sleep duration
rng = np.random.default_rng(seed=1) #this is a random number generator
x_jittered = df["Stress Level"] + rng.uniform(-0.15, 0.15, size=len(df))
#makes sure overlapping dots are still visible

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(x_jittered, df["Sleep Duration"], alpha=0.5, s=35, color="#DDA0DD", edgecolors="none")
#this will plot one dot per person and it will make the dots semi transparent so overlaps are still visible

ax.set_title("Stress Level vs Sleep Duration")
ax.set_xlabel("Stress level (1-10 self-rated scale)")
ax.set_ylabel("Sleep duration (hours)")
ax.grid(linestyle="--", alpha=0.5)
fig.tight_layout()
fig.savefig("scatter_stress_vs_sleep.png", dpi=200)

rho, p_value = stats.spearmanr(df["Stress Level"], df["Sleep Duration"])
#this will compute spearman's rank correlation

print(f"\nSpearman correlation (stress vs sleep duration): "
      f"rho = {rho:.4f}, p = {p_value:.3e}, n = {len(df)}")
#this will print rho, p-value and sample size
