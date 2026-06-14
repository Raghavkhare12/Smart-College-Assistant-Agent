# AI-Powered College Assistant using LangChain Tool Calling Agent

## Project Overview

The AI-Powered College Assistant is a LangChain-based intelligent assistant that automatically identifies student-related requests and invokes the appropriate tool to generate accurate responses.

The assistant uses a Tool Calling Agent powered by a locally running Large Language Model through Ollama. Based on the user's query, the agent selects the required tool(s), performs calculations, and returns the final response.

The project demonstrates the practical use of LangChain Agents, Tool Calling, Prompt Engineering, and Local LLM Integration.

---

## Objectives

* Automate common college-related calculations.
* Use LangChain Tool Calling Agent architecture.
* Automatically select and execute appropriate tools.
* Handle single-tool and multi-tool queries.
* Integrate a local LLM using Ollama.

---

## Technologies Used

### Programming Language

* Python 3.13

### Frameworks and Libraries

* LangChain 0.3.26
* LangChain Community 0.3.27
* LangChain Core 0.3.86
* LangChain Ollama 0.3.6

### LLM

* Qwen2.5:3B

### Runtime

* Ollama

---

## Package Versions Used

```text
langchain                0.3.26
langchain-community      0.3.27
langchain-core           0.3.86
langchain-ollama         0.3.6
```

---

## Features

### 1. Attendance Calculator

#### Inputs

* Total Classes
* Attended Classes

#### Output

* Attendance Percentage
* Exam Eligibility Status

#### Rule

```text
Attendance >= 75%
Eligible for Exam

Attendance < 75%
Not Eligible for Exam
```

---

### 2. Result Calculator

#### Inputs

* Marks of 5 Subjects

#### Outputs

* Average Marks
* Grade
* Pass/Fail Status

#### Grading Criteria

| Average Marks | Grade |
| ------------- | ----- |
| >= 90         | A     |
| 75 - 89       | B     |
| 60 - 74       | C     |
| < 60          | D     |

#### Pass Criteria

```text
Average >= 50
PASS

Average < 50
FAIL
```

---

### 3. Fee Balance Calculator

#### Inputs

* Total Course Fee
* Amount Paid

#### Output

```text
Pending Fee = Total Fee - Amount Paid
```

---

### 4. Library Fine Calculator

#### Input

* Number of Delayed Days

#### Formula

```text
Fine = 5 × Delayed Days
```

---

### 5. Hostel Fee Calculator

#### Inputs

* Monthly Hostel Fee
* Number of Months Stayed

#### Formula

```text
Hostel Fee = Monthly Fee × Months Stayed
```

---

### 6. Student Information Tool (Bonus)

Retrieves student information using a Student ID from a Python dictionary.

Example:

```python
student_db = {
    "101": {
        "name": "Raghav",
        "branch": "CSE",
        "year": 3
    }
}
```

---

## LangChain Components Used

### @tool

Used to create custom tools:

* attendance_calculator
* result_calculator
* fee_balance_calculator
* library_fine_calculator
* hostel_fee_calculator
* student_information

---

### ChatPromptTemplate

Used to create the agent prompt.

Responsibilities:

* Guide the LLM
* Tell the model when to use tools
* Support multi-tool execution

---

### create_tool_calling_agent()

Creates the Tool Calling Agent capable of:

* Understanding user intent
* Selecting tools automatically
* Executing one or multiple tools

---

### AgentExecutor

Executes the agent and tools.

Configuration:

```python
verbose=True
```

This displays:

* Tool selected
* Tool inputs
* Tool outputs
* Final answer

---

## Project Architecture

```text
User Query
      |
      v
Tool Calling Agent
      |
      v
Intent Detection
      |
      v
Tool Selection
      |
      v
Tool Execution
      |
      v
Final Response
```

---

## Workflow

1. User enters a query.
2. Qwen2.5:3B analyzes the request.
3. LangChain Agent determines the required tool.
4. Tool executes the calculation.
5. Agent generates the final response.
6. If multiple tasks exist, multiple tools are invoked automatically.

---

## Test Cases

### Query 1

```text
I attended 72 classes out of 90.
Am I eligible for exams?
```

Expected Result

```text
Attendance Percentage = 80%
Status = Eligible for Exam
```

---

### Query 2

```text
My marks are 95, 90, 88, 91 and 87.
What is my grade?
```

Expected Result

```text
Average = 90.2
Grade = A
Result = Pass
```

---

### Query 3

```text
My course fee is 50000 and I have paid 35000.
How much fee is pending?
```

Expected Result

```text
Pending Fee = 15000
```

---

### Query 4

```text
I returned a library book 8 days late.
What is the fine amount?
```

Expected Result

```text
Fine Amount = 40
```

---

### Query 5

```text
Hostel fee is 6000 per month and I stayed for 5 months.
Calculate my hostel fee.
```

Expected Result

```text
Hostel Fee = 30000
```

---

### Query 6

```text
Show details of student 101
```

Expected Result

```text
Final Answer:
The details of student with id 101 are as follows: 
- Name: Raghav
- Branch: CSE
- Year: 3rd Year
```

---

## Multi-Tool Challenge

### Query

```text
I attended 80 classes out of 100.

My marks are 90, 85, 88, 92 and 95.

My course fee is 60000 and I paid 45000.

Provide:
1. Attendance Status
2. Grade
3. Pending Fee
```

### Tools Invoked

```text
attendance_calculator

result_calculator

fee_balance_calculator
```

### Output

```text
Attendance Status:
Eligible for Exam

Grade:
A

Pending Fee:
15000
```

---

## Installation

Install dependencies:

```bash
pip install langchain==0.3.26
pip install langchain-community==0.3.27
pip install langchain-core==0.3.86
pip install langchain-ollama==0.3.6
```

---

## Running Ollama

Verify model:

```bash
ollama list
```

Expected:

```text
qwen2.5:3b
```

Run model:

```bash
ollama run qwen2.5:3b
```

---

## Running the Project

```bash
python college_assistant.py
```

Example:

```text
Ask a question:

I attended 72 classes out of 90.
Am I eligible for exams?
```

---

## Sample Verbose Execution

```text
> Entering new AgentExecutor chain...

Invoking: attendance_calculator

Input:
{
    "attended_classes": 72,
    "total_classes": 90
}

Output:
{
    "attendance_percentage": 80.0,
    "exam_status": "Eligible for Exam"
}

> Finished chain.
```

---

## Conclusion

This project successfully demonstrates the implementation of an AI-powered College Assistant using LangChain Tool Calling Agents and a locally hosted Qwen2.5:3B model through Ollama. The system automatically identifies user intent, invokes the appropriate tool(s), and generates accurate responses for both single-tool and multi-tool queries.
