# add your code here
import pandas as pd

# Read the CSV file
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

country = df['country'].value_counts()
# print(country)
Avg_points = df.groupby('country').points.mean().round(1)
# print(Avg_points)
summary = pd.merge(country, Avg_points, on='country')

print(summary)

summary.to_csv('data/reviews-per-country.csv')

# Rename columns for clarity
# summary.rename(columns={'country': 'Country', 'count': 'Number of Reviews', 'average_points': 'Average Points'}, inplace=True)

# Sort the summary data by Average Points in descending order
# summary = summary.sort_values(by='Average Points', ascending=False)
# summary['Average Points'].round(1)

# summary.to_csv('data/reviews-per-country.csv', index=False)

# print(summary)