# Hebbian Song -> Happiness Model
learning_rate = 0.15
weight = 0.0
experiences = [
    (1,1),  # heard song, felt happy
    (1,0),  # heard song, not happy
    (0,1),  # didn't hear song, felt happy
    (1,1),  # heard song, felt happy
    (0,0),  # didn't hear song, not happy
    (1,1)   # heard song, felt happy
]

print("Hebbian Learning : Song -> Happiness")
print("-"*55)
print("day | heard song | happiness | weight")
print("-"*55)

for day, (heard_song, happiness) in enumerate(experiences, start=1):
    delta_w = learning_rate * heard_song * happiness
    weight += delta_w
    print(f"{day:^3} | {heard_song:^10} | {happiness:^9} | {weight:.2f}")
    print("-"*55)

# Testing new input
print("\nTesting New Input")
test_input = int(input("Did the person hear the song? (1=yes, 0=no): "))

# Hebbian prediction: output = input * weight
predicted_happiness = test_input * weight
print(f"Predicted 'Happiness' value = {predicted_happiness:.2f}")
