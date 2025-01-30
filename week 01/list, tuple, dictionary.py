# Task 01 - Lists
numbers = [23,63,52,35,66]
numbers.append(89)
numbers.remove(numbers[1])
sum = 0
for x in numbers:
    sum += x
print(sum)

# Task 02 - Tuples
cities = ("Dhaka", "Sylhet", "Cumilla", "Barishal", "Rajshahi")
print(cities[2])
cities = list(cities)
cities.append("Chittagong")
cities = tuple(cities)
print(cities)

# Task 03 - Dictionaries
results = { "Math": 85, 
            "Physics": 76, 
            "Chemistry": 69 }
results["English"] = 65 
results["Physics"] = 80
sum = 0
for x in results:
    sum += results.get(x)
avg = sum / len(results)
print(avg)
