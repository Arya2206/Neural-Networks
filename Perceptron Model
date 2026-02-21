

#Disease Detection (FLu Prediction)
# Training data for Flu prediction
# Features: [fever, cough, fatigue]
# Target: 1 = Flu, 0 = No Flu
data = [
    ([1,1,1], 1),  # fever + cough + fatigue → Flu
    ([1,1,0], 1),  # fever + cough → Flu
    ([1,0,1], 1),  # fever + fatigue → Flu
    ([0,1,1], 1),  # cough + fatigue → Flu
    ([1,0,0], 0),  # only fever → No Flu
    ([0,1,0], 0),  # only cough → No Flu
    ([0,0,1], 0),  # only fatigue → No Flu
    ([0,0,0], 0)   # no symptoms → No Flu
print("\nConfusion Matrix:")
print("TP:", TP, "TN:", TN, "FP:", FP, "FN:", FN)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# --- User Test ---
print("\n--- Test Your Symptoms --- ")
print("Enter 1 if symptom is present, 0 if not.")
fever = int(input("Do you have fever? (1/0): "))
cough = int(input("Do you have cough? (1/0): "))
fatigue = int(input("Do you feel fatigue? (1/0): "))

user_input = [fever, cough, fatigue]
output = sum(weights[i] * user_input[i] for i in range(3)) + bias
prediction = 1 if output >= 0 else 0

print("\nYour symptoms:", user_input)
if prediction == 1:
    print("Prediction: FLU")
else:
    print("Prediction: NO FLU")
