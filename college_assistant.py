from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

@tool
def attendance_calculator(total_classes: int, attended_classes: int):
    """
    Calculate attendance percentage and exam eligibility.
    """

    percentage = (attended_classes / total_classes) * 100

    status = (
        "Eligible for Exam"
        if percentage >= 75
        else "Not Eligible for Exam"
    )

    return {
        "attendance_percentage": round(percentage, 2),
        "exam_status": status
    }

@tool
def result_calculator(
    mark1: int,
    mark2: int,
    mark3: int,
    mark4: int,
    mark5: int
):
    """
    Calculate average marks, grade and pass status.
    """

    average = (
        mark1 + mark2 + mark3 + mark4 + mark5
    ) / 5

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    status = "Pass" if average >= 50 else "Fail"

    return {
        "average_marks": round(average, 2),
        "grade": grade,
        "result": status
    }

@tool
def fee_balance_calculator(
    total_fee: float,
    amount_paid: float
):
    """
    Calculate pending fee amount.
    """

    pending = total_fee - amount_paid

    return {
        "pending_fee": pending
    }

@tool
def library_fine_calculator(delayed_days: int):
    """
    Calculate library fine.
    """

    fine = delayed_days * 5

    return {
        "fine_amount": fine
    }

@tool
def hostel_fee_calculator(
    monthly_fee: float,
    months_stayed: int
):
    """
    Calculate hostel fee.
    """

    total = monthly_fee * months_stayed

    return {
        "hostel_fee": total
    }

student_db = {
    "101": {
        "name": "Raghav",
        "branch": "CSE",
        "year": 3
    },
    "102": {
        "name": "Aman",
        "branch": "ECE",
        "year": 2
    }
}

@tool
def student_information(student_id: str):
    """
    Retrieve student details using student id.
    """

    if student_id in student_db:
        return student_db[student_id]

    return "Student not found"

tools = [
    attendance_calculator,
    result_calculator,
    fee_balance_calculator,
    library_fine_calculator,
    hostel_fee_calculator,
    student_information
]

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a College Assistant.

            Analyze the user's request carefully.

            Use the appropriate tool whenever calculations
            are required.

            Present results in a clear numbered format.

            If multiple tasks are requested, call multiple
            tools and combine the results into a single answer.
            """
        ),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ]
)

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

while True:
    query = input("\nAsk a question (type exit to quit): ")

    if query.lower() == "exit":
        break

    response = agent_executor.invoke(
        {
            "input": query
        }
    )

    print("\nFinal Answer:")
    print(response["output"])