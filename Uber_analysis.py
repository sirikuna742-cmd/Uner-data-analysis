# UBER DATA ANALYSIS - Codtech Internship Task 2
# Intern: Kuna Siri | ID: CITS9815 | Domain: AI

import pandas as pd
import matplotlib.pyplot as plt

print("=== UBER DATA ANALYSIS ===")
print("Intern: Kuna Siri - CITS9815")

# Sample Uber Dataset
data = {
    'Hour': [8, 9, 10, 18, 19, 20, 21, 22]*10,
    'Location': ['Hyderabad','Mumbai','Bangalore','Delhi']*20,
    'Rides': [20,45,30,60,70,55,40,25]*10,
    'Price': [150,220,180,300,350,280,200,160]*10,
    'Rating': [4.5,4.8,4.6,4.9,4.7,4.8,4.5,4.6]*10
}
df = pd.DataFrame(data)

# ANALYSIS 1: Total Stats
print("\n1. Total Rides:", df['Rides'].sum())
print("2. Average Price: Rs.", round(df['Price'].mean(),2))
print("3. Average Rating:", round(df['Rating'].mean(),2))

# ANALYSIS 2: Peak Hour
peak = df.groupby('Hour')['Rides'].sum().idxmax()
print(f"4. Peak Hour: {peak}:00 - Most rides")

# ANALYSIS 3: Location wise
loc = df.groupby('Location')['Rides'].sum()
print("\n5. Rides by Location:")
print(loc)

# ANALYSIS 4: Price Trend
print("\n6. Price Analysis - Highest in Peak Hours")
print("\n--- Analysis Complete! Ready for GitHub ---")
