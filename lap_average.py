# Lap time data (in seconds)
lap_times = [88.4, 88.7, 89.0, 87.9, 88.2]

# Calculate average lap time
total = 0
for time in lap_times:
    total = total + time

average = total / len(lap_times)

print("Average lap time:", average, "seconds")
