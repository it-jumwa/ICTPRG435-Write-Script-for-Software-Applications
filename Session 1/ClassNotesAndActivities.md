---
### Session 1
#### Session1 slides.pdf
Class Example: <br>
A user is required to enter 2 decimal numbers into a Python program. The Python 
program will calculate the multiplication of these 2 numbers and print the 
result to the computer screen.

result = number1 * number2

| Input   | Process                    | Output |
|---------|----------------------------|--------|
| number1 | result = number1 * number2 | result |
| number2 |                            |        |

| Variable | Datatype |
|----------|----------|
| number1  | float    |
| number2  | float    |
| result   | float    |

Program: [multiply.py](Session 1\Multiply.py)

---
**Program Development Life Cycle** (PDLC) <br>
→ Define the problem definition <br>
→ Create an IPO chart <br>
→ Develop a method (pseudocode) <br>
→ Create a variable list <br>
→ Desk-check <br>
→ Develop a script <br>
---

#### Session1Slides2b.pdf
Problem Definition:
Design a Python Script that allows a network engineer to enter their
rate of pay and hours worked. The script calculates the network
engineer's pay and prints it to the computer screen.
pay = hours * rate

**IPO Chart**

| Input | Process            | Output |
|-------|--------------------|--------|
| hours | pay = hours * rate | pay    |
| rate  |                    |        |

**Pseudocode**
- Get hourly rate
- Get hours worked
- Calculate pay
- Output/Print calculated pay rate

**Variable List**

| Variable | Datatype |
|----------|----------|
| hours    | float    |
| rate     | float    |
| pay      | float    |

#### Desk Check
[Network Engineer Hourly Rate:](https://au.seek.com/career-advice/role/network-engineer/salary):
$110 - $130

### Values to Test:
Hours:
- -1
- 0
- 5
- 10
- 10.10
- ten
- X
- ,./

Rate:
- -1
- 0
- 110
- 130
- 110.10
- one hundred and ten
- CX
  <sub>110 in roman numerals</sub>
- ,./

___
#### Test 1: Negative values
hours = -1 <br>
rate = -1 <br>
pay = -1 × -1 = $1

Result: Invalid inputs, hours and rate must be greater than 0

---
#### Test 2: Zero values
hours = 0 <br>
rate = 0 <br>
pay = 0 × 0 = $0

Result: Invalid inputs, hours and rate must be greater than 0

---
#### Test 3: Whole numbers
hours = 5 <br>
rate = 110 <br>
pay = 5 × 110 = $550

Result: Valid

---

#### Test 4: Boundary value
hours = 10 <br>
rate = 130 <br>
pay = 10 × 130 = $1,300

Result: Valid

---

#### Test 5: Decimal values
hours = 10.10 <br>
rate = 110.10 <br>
pay = 10.10 × 110.10 = $1,112.01

Result: Valid

---

#### Test 6: Written words
hours = ten <br>
rate = one hundred and ten <br>
pay = **Invalid input / calculation cannot be performed**

Result: Invalid inputs, hours and rates must be <u>float values</u> <br>
Although it is possible to create an application that accepts values received
as written words, this would go beyond the scope of the needs of the client,
while creating an application that is unnecessarily more complex.

---

#### Test 7: Alphabetic / Roman numeral input
hours = X  <br>
rate = CX <br>
pay = **Invalid input / calculation cannot be performed**

Result: Invalid inputs, hours and rates must be <u>float values</u>

---

#### Test 8: Special characters
hours = ,./ <br>
rate = ,./ <br>
pay = **Invalid input / calculation cannot be performed**

---

Program: 
