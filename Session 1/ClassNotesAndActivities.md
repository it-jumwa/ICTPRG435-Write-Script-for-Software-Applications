# Session 1

---
## Session1 slides.pdf
Class Example: <br>
A user is required to enter 2 decimal numbers into a Python program. 
The Python program will calculate the multiplication of these 2 numbers and print the 
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

Program: [Multiply.py](Multiply.py)

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
Problem Definition: <br>
Design a Python Script that allows a network engineer to enter their
rate of pay and hours worked. The script calculates the network
engineer's pay and prints it to the computer screen.
pay = hours * rate

**IPO Chart**

| Input | Process            | Output |
|-------|--------------------|--------|
| hours | pay = hours * rate | pay    |
| rate  |                    |        |

---

**Pseudocode**
- Get hourly rate
- Get hours worked
- Check if `hours` and `rate` are:
  - `float` values
  - Greater than 0
- Calculate pay
- Output/Print calculated pay rate

---

**Variable List**

| Variable | Datatype |
|----------|----------|
| hours    | float    |
| rate     | float    |
| pay      | float    |

---

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

Program: [CalculatePay.py](CalculatePay.py)

---
## Worksheet 1
### 1) Evaluate each of the following: <br>
(a) 3 % 5 = 3 <br>
(b) 6 – 2 = 4 <br>
(c) 4 * 6  = 24 <br>
(d) 7 / 3 = 2.3333333333333335 <br>
(e) 5 / 7 = 0.7142857142857143 <br>


### 2) Which command shows us all the processes running in the Windows Operating 
system?

via cmd: tasklist <br>
via PowerShell: get-process

<sub>sdwheeler (2025). Get-process (microsoft.PowerShell.Management) - PowerShell. [online] Microsoft.com. Available at: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process?view=powershell-7.6 [Accessed 5 Oct. 2026].
<sub>JasonGerend (2023). Tasklist. [online] learn.microsoft.com. Available at: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tasklist [Accessed 5 Oct. 2026].</sub>


### 3) A network client requires you to develop a shell script to allow the user to enter any 2 integer numbers and then print their product and modulus results. 
You are expected to produce:
(a) an IPO chart <br>
(b) a solution method (algorithm) <br>
(c) the script <br>

**IPO Chart**

| Input  | Process                    | Output   |
| ------ | -------------------------- | -------- |
| value1 | product = value1 * value2  | product  |
| value2 | modulus1 = value1 % value2  | modulus1 |
|        | modulus2 = value2 % value1 | modulus2 |

**Pseudocode**
 - Receive `value1` from user
 - Receive `value2` from user
 - Validate `value1` and `value2` are `integers`
 - Calculate the product
 - Calculate `modulus1` and `modulus2`
 - Output the product, `modulus1` and `modulus2`

**Program:** [CalculateProductAndModulus.py](CalculateProductAndModulus.py)

### 4) A network client requires you to develop a shell script to accept from 4 
   Windows commands and then to execute each in turn
You are expected to produce: <br>
(a) an IPO chart <br>
(b) a solution method (algorithm) <br>
(c) the script <br>

---
## Worksheet 2.
### 1.What do each of the following evaluate to?
(a) 3 * 2 = 6 <br>
(b) 6 – 4 = 2 <br>
(c) 9 % 4 = 1 <br>
(d) 9 / 2 = 4.5 <br>

### 2. What is wrong with following code?
```python
   punt Enter your name:”)
```

Design and execute a Python program that will allow a user to enter the internet service
provider (ISP) internet connectivity value kbps (example 512).  

The Python program will then calculate a file's download speed based on the following formula

Download_KBps_speed = ((kbps value * 1000)/8)/1024
   
The Python program will finally print the file's download KBps speed to the computer
   screen.

You are required to produce: 

(a) an IPO chart <br>
(b) variable list <br>
(c) solution method <br>
(d) script

### 3. Write down 2 windows commands
 - cls
 - help

### 4. What will this python command print out?
```python
print("firstname")
```