# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define the dataset
data = {
    'Model': ['Model A', 'Model B', 'Model C'],
    'Error 1': [0.5, 0.3, 0.4],
    'Error 2': [1.2, 0.9, 1.1],
    'Error 3': [0.7, 0.6, 0.5]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)
0
# Set the 'Model' column as the index
df.set_index('Model', inplace=True)

# Set the figure size for the heatmap
plt.figure(figsize=(8, 6))

# Create the heatmap with annotations and a color map
heatmap = sns.heatmap(df, annot=True, cmap='YlGnBu', linewidths=0.5)

# Add a title and labels for clarity
plt.title('Model Error Heatmap')
plt.xlabel('Error Types')
plt.ylabel('Models')

# Display the heatmap
plt.show()
