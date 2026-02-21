# Hebbian Exercise -> Energy Model
learning_rate = 0.2
weight = 0.0
daily_data = [
    (1,1),  # exercised, felt energetic
    (0,1),  # no exercise, still energetic
    (1,0),  # exercised, but not energetic
    (1,1),  # exercised, felt energetic
    (0,0)   # no exercise, no energy
]

print("Hebbian Learning : Exercise -> Energy")
print("-"*55)
print("day | exercised | energy | weight")
print("-"*55)

for day, (exercise, energy) in enumerate(daily_data, start=1):
    delta_w = learning_rate * exercise * energy
    weight += delta_w
    print(f"{day:^3} | {exercise:^9} | {energy:^6} | {weight:.2f}")
    print("-"*55)

# Testing new input
print("\nTesting New Input")
test_input = int(input("Did the person exercise? (1=yes, 0=no): "))

# Hebbian prediction: output = input * weight
predicted_energy = test_input * weight
print(f"Predicted 'Energy' value = {predicted_energy:.2f}")
