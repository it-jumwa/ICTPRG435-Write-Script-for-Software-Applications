# Session 2

---
**Program Development Life Cycle** (PDLC) <br>
→ Define the problem definition <br>
→ Create an IPO chart <br>
→ Create a variable list <br>
→ Develop a method (pseudocode) <br>
→ Desk-check <br>
→ Develop a script <br>
---
## Moodle Activity: Basic Calculator

**Problem Definition:**
Calculator that accepts 2 numbers and can perform functions
such as add, subtract, multiply and division. 
The output is displayed in the GUI. 
There is a button to clear the entry boxes and result, as well as a button to 
exit the application

**IPO Chart**

| Input                        | Process                                             | Output                                           |  
|------------------------------|-----------------------------------------------------|--------------------------------------------------|  
| First value                  | Add both values                                     | The sum of both values                           |  
| Second value                 | Subtract the second value from the first <br/>value | The second value subtracted from the first value |  
| Selection to add or subtract | Multiply both values together                       | The product of both values                       |
|                              | Divide the first value by the second value          | The first value divided by the second value      |

**Variable List**

| Variable     | Datatype |  
|--------------|----------|  
| First value  | float    |  
| Second value | float    |  
|              |          |

**Pseudocode**

Start Program
 - Receive first value
 - Receive second value
 - If `Add` button is clicked
   - Sum the two values together
 - If the `Subtract` button is clicked
   - Subtract the second value from the first value
   - Display the result
 - If the `Multiply` button is clicked
   - Multiply both values together
   - Display the result
 - If the `Division` button is clicked
   - Divide the first value by the second value
   - Display the result
 - If the `Clear` button is clicked
   - Clear the entry boxes
   - Reset the result label
 - If the `Exit` button is clicked
   - Exit the application
 
End Program

---

**Desk Check**

---
#### Test Case 1: Negative Values

First Value: -1 <br>
Second Value: -1

Add: -1 + -1 = -2
Subtract: -1 - -1 = 0

---
#### Test Case 2: Zero Values

First Value: 0 <br>
Second Value: 0

Add: 0 + 0 = 0
Subtract: 0 - 0 = 0

---
#### Test Case 3: Whole Numbers

First Value: 1 <br>
Second Value: 1

Add: 1 + 1 = 2
Subtract: 1 - 1 = 0

---
#### Test Case 4: Float Values

First Value: 1.5 <br>
Second Value: 2.5

Add: 1.5 + 2.5 = 4
Subtract: 1.5 - 2.5 = -1

---
#### Test Case 5: String input

First Value: zero <br>
Second Value: one

Add: **Invalid input**
Subtract: **Invalid input**

---

**Program:** [BasicCalculator.py](BasicCalculator.py)
