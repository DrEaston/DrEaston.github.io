import pandas as pd

# URL of the CSV file
url = 'https://flunky.github.io/cars2017.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(url)


# Grouping by Make and Fuel, and counting the occurrences
make_fuel_counts = df.groupby(['Make', 'Fuel']).size().unstack(fill_value=0)

# Finding the makes with the most rows for each fuel type
max_gasoline = make_fuel_counts['Gasoline'].idxmax()
max_diesel = make_fuel_counts['Diesel'].idxmax()
max_electric = make_fuel_counts['Electricity'].idxmax()

# Creating tables for each fuel type
gasoline_table = make_fuel_counts.loc[[max_gasoline], ['Gasoline']]
diesel_table = make_fuel_counts.loc[[max_diesel], ['Diesel']]
electric_table = make_fuel_counts.loc[[max_electric], ['Electricity']]

print("Gasoline Table:")
print(gasoline_table)
print("\nDiesel Table:")
print(diesel_table)
print("\nElectric Table:")
print(electric_table)