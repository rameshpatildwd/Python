temperatures = [25, 28, 32, 35, 27, 23, 33]
highest_temperature = max(temperatures)
print(f"Highest temperature: {highest_temperature}")
print()


for index, temp in enumerate(temperatures):
    if temp > 30:
        print(f"Day {index} (index {index}): {temp} degrees")
print()


last_three_days_temperatures = temperatures[-3:]
print("Last three days' temperatures:", last_three_days_temperatures)
