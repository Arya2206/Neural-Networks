# Hebbian Traffic Light -> Accelerator Model
learning_rate = 0.1
weight = 0.0
trials = [
    (1,1),  # green light, pressed accelerator
    (1,0),  # green light, did not press
    (0,1),  # not green light, pressed accelerator
    (1,1),  # green light, pressed accelerator
    (0,0)   # not green light, did not press
]

print("Hebbian Learning : Traffic Light -> Accelerator")
print("-"*60)
print("trial | green light | accelerator | weight")
print("-"*60)

for trial, (green_light, accelerator) in enumerate(trials, start=1):
    delta_w = learning_rate * green_light * accelerator
    weight += delta_w
    print(f"{trial:^5} | {green_light:^11} | {accelerator:^11} | {weight:.2f}")
    print("-"*60)

# Testing new input
print("\nTesting New Input")
test_input = int(input("Is the traffic light green? (1=yes, 0=no): "))

# Hebbian prediction: output = input * weight
predicted_action = test_input * weight
print(f"Predicted 'Accelerator Press' value = {predicted_action:.2f}")
