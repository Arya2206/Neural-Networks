# Hebbian Learning Example
learning_rate = 0.1
weight = 0.0
data = [
    (1,1),
    (1,0),
    (0,1),
    (1,1),
    (0,0)
]

print("Hebbian learning : Study -> Good Marks")
print("-"*50)
print("day | studied | good marks | weight")
print("-"*50)

for day, (studied, good_marks) in enumerate(data, start=1):
    delta_w = learning_rate * studied * good_marks
    weight += delta_w
    print(f"{day:^3} | {studied:^7} | {good_marks:^10} | {weight:.2f}")
    print("-"*50)

# Testing new input
print("\nTesting New Input")
test_input = int(input("Did the student study? (1=yes, 0=no): "))

# Hebbian prediction: output = input * weight
predicted_output = test_input * weight
print(f"Predicted 'Good Marks' value = {predicted_output:.2f}")
