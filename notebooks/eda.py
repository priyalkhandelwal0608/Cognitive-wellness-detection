import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/sample_dataset.csv")

# Distribution of stress levels
sns.countplot(x="StressLevel", data=df)
plt.title("Stress Level Distribution")
plt.show()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation")
plt.show()

# Pairplot
sns.pairplot(df, hue="StressLevel")
plt.show()