import pandas as pd

df = pd.read_csv('reservations.csv')

# Question 0
# Generate a new csv file (excluding all cancelations)
df_filtered = df[df['Status'] != 'C']

# Convert string to datetime
df_filtered['BookTime'] = df_filtered['BookTime'].astype('datetime64[ns]')
df_filtered['Arrival'] = df_filtered['Arrival'].astype('datetime64[ns]')
df_filtered['Booking Window'] = df_filtered['Arrival'] - df_filtered['BookTime']

df_reservations = df_filtered.groupby('Reservation ID', as_index=False).agg('sum')
df_reservations.to_dense().to_csv("reservations_by_revenue.csv", index=False, sep=',', encoding='utf-8')

# Question 1
# Find top 10 paying customers excluding Blocks.
top_paying_customers = \
df_filtered[df_filtered['Block ID'] == 0].groupby(['Guest ID', 'FirstName', 'LastName'], as_index=False)[
    'Room Revenue'].agg('sum').sort_values('Room Revenue', ascending=False).head(10)

# Question 2
# Find top 10 block reservations (Block ID > 0)
top_block_reservations = df_filtered[df_filtered['Block ID'] > 0].groupby(['Block ID', 'Nights'], as_index=False)[
    'Room Revenue'].agg('sum').sort_values('Room Revenue', ascending=False).head(10)

# Question 3
# top 10 reservations which have long booking window.
top_booking_windows = df_filtered.sort_values('Booking Window', ascending=False).reset_index().head(10)

# Question 4
# Find top 10 countries within each country top 5 cities within each city top 5 zipcodes.
df_region_grouped = df_filtered.groupby(['GstCountryCode', 'GstCity', 'GstZip'], as_index=False)['Room Revenue'].agg('sum')
df_top_regions = df_region_grouped.sort_values('Room Revenue', ascending=False).head(10)
