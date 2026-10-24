 #STEP1: Stored memory
>>> memory = {
...     90: "A",
...     75: "B",
...     60: "C"
...     }
>>> 
>>> #STEP 2: New input
>>> new_marks = 55
>>> 
>>> #step 3: Find the closest marks in memory
>>> closest_marks = None
>>> minimum_distance = float('inf')
>>> 
>>> for marks in memory:
...     distance = abs(new_marks - marks)
...     if distance < minimum_distance:
...         minimum_distance = distance
...         closest_marks = marks
... 
...         
>>> #STEP 4:
...         
>>> #STEP 4: Predict output
...         
>>> predicted_grade = memory[closest_marks]
>>> 
>>> #Display result
>>> print("Memory-Based Learning Example")
Memory-Based Learning Example
>>> print("-"*50)
--------------------------------------------------
>>> print(Stored Data:", memory)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("Stored Data:", memory)
...       
Stored Data: {90: 'A', 75: 'B', 60: 'C'}
print("New Marks:", new_marks)
      
New Marks: 55
print("Closest Stored Marks:", closest_marks)
      
Closest Stored Marks: 60
print("Predicted Grades:", predicted_grades)
      
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print("Predicted Grades:", predicted_grades)
NameError: name 'predicted_grades' is not defined. Did you mean: 'predicted_grade'?
print("Predicted Grades:", predicted_grade)
      
Predicted Grades: C
