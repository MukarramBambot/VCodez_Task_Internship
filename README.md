# 📘 Task 15 – Difference Between map(), filter(), and reduce() (Python)

This task explains the difference between **map**, **filter**, and **reduce** using a real-world example from **online shopping**.  
Each function processes a list of prices and performs a different type of transformation.

---

## 1️⃣ map() – Apply a Function to Every Element  

`map()` is used to **transform** each item in an iterable.

### ✔️ Real-Time Example: Add 10% GST to Every Product  
Input List:  
`[250, 450, 120, 999, 75, 300]`

- Adds 10% GST to all prices  
- Returns a list of updated prices  

### 🧠 Learned  
- `map()` always returns the **same number of elements**  
- Used when you want to modify or transform each item  

---

## 2️⃣ filter() – Select Elements Based on a Condition  

`filter()` is used to **pick only certain items** from a list.

### ✔️ Real-Time Example: Find Premium Products Above ₹300

- Checks each price  
- Returns only items that match the condition  

### 🧠 Learned  
- Output may be **smaller** than input  
- Used for conditional selection  

---

## 3️⃣ reduce() – Reduce All Elements Into One Value  

`reduce()` (from `functools`) combines all items into a **single result**.

### ✔️ Real-Time Example: Calculate Total Cart Amount  

- Repeatedly adds prices  
- Returns final total  

### 🧠 Learned  
- reduce() always outputs **one value**  
- Used for totals, averages, cumulative operations  

---

## 🔑 Summary: map vs filter vs reduce

| Function | Purpose | Output Size | Use Case |
|---------|----------|-------------|----------|
| **map()** | Transform each element | Same as input | Apply GST, convert values |
| **filter()** | Keep only elements that meet condition | Smaller or equal | Find premium items, filter data |
| **reduce()** | Combine all elements into one output | Always 1 | Total price, sum, product |

---

## 📂 File Included

### 📝 Sample.py  
Contains:
- Example list of product prices  
- map() for GST calculation  
- filter() for selecting premium products  
- reduce() for total cart value  
- Summary explanation printed at the end  

---

## 📌 Internship Tasks  

0. **Main Repo Overview**  
   🔗 https://github.com/MukarramBambot/VCodez_Task_Internship.git  
1. [Task 01: Basic HTML Structure](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-1-&-2)  
2. [Task 02: Invoice Table Layout using HTML](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-1-&-2)  
3. [Task 03: Table Styling with CSS](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-3)  
4. [Task 04: Creating a Radial Gradient in CSS](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-4-&-5)  
5. [Task 05: Applying Image Filters with CSS](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-4-&-5)  
6. [Task 06: Designing an Event Webpage](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-6)  
7. [Task 07: If-Else Statement in JavaScript](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-7)  
8. [Task 08: Else-If Statement in JavaScript](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-8)  
9. [Task 09: Python Program for Arithmetic Operations](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-9)  
   - Function without argument & without return type  
   - Function with argument & without return type  
   - Function without argument & with return type  
   - Function with argument & with return type  
10. [Task 10: Python Real-Time Examples](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-10)  
    - Elif Example → Grading System  
    - Nested If Example → ATM Withdrawal System  
11. [Task 11: Pattern Programs](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-11)  
    - Right Triangle  
    - Inverted Right Triangle  
    - Full Pyramid  
    - Inverted Full Pyramid  
    - Parallelogram  
12. [Task 12 - List and Tuple Operations](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-12)
- List:-
    - Write a program to sum all the items in a list
    - Write a program to multiply all the items in a list
    - Write a program to get the largest number from a list
    - Write a program to get the smallest number from a list
    - Write a program to remove duplicates from a list
    - Write a program to check if a list is empty or not
- Tuple:-
    - program to create a tuple with different datatypes
    - program to create a tuple with numbers and print one item
    - program to unpack a tuple in several variables
    - program to add an item in a tuple
    - program to get 5th element from a tuple and also the 5th element from the last
    - program to find repeated elements in a tuple

13. [Task 13 - Set Programs in Python](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-13)
- Set:-
    - Write a Python program to create a set.
    - Write a Python program to iterate over sets. 
    - Write a Python program to add elements to a set.
    -  Write a Python program to remove item from a given set.
    - Write a Python program to remove an item from a set if it is present in the set.
    - Write a Python program to create an intersection of sets.
    - Write a Python program to create a union of sets.
14. [Task 14: File Handling in Python (r+, w+, a+)](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-14)  
15. [Task 15: Difference between map, filter, and reduce (with real-time examples)](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-15)  
16. [Task 16: Multiple & Multilevel Inheritance in Python (User Input Version)](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-16)  
17. [Task 17: Arithmetic Operations Page using Tkinter](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-17)  
18. [Task 18: Creating an "Traffic Light Simulator" using tkinter in python program](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-18)  
19. [Task 19: Creating an Tkinter + MySQL Employee Database app](https://github.com/MukarramBambot/VCodez_Task_Internship/tree/Task-19)  

---

## 📑 Assessments  

1. Assessment 01: Event Website using HTML & CSS  
2. Assessment 02: JavaScript Q & A  
3. Assessment 03: ReactJS  
4. Assessment 04: Python Q & A Part 1  
5. Assessment 05: MySQL Q&A

---

## 🔗 About This Repository  

This repository is maintained as part of my internship at **VCodez** where I am working as a **Full Stack Developer (Python)**.  
Each branch represents a separate task/assessment with the complete code and implementation details.  

---
