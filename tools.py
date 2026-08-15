from langchain.tools import tool


@tool
def get_course_information(course_name: str) -> str:
    """Get information about a university course."""

    courses = {
        "Artificial Intelligence": {
            "credit_hours": 3,
            "fee": 12000,
            "type": "Major"
        },
        "Database Systems": {
            "credit_hours": 3,
            "fee": 11000,
            "type": "Core"
        },
        "Computer Networks": {
            "credit_hours": 3,
            "fee": 10000,
            "type": "Core"
        },
        "Software Engineering": {
            "credit_hours": 3,
            "fee": 11500,
            "type": "Core"
        }
    }

    course = courses.get(course_name)

    if course:
        return (
            f"Course: {course_name}\n"
            f"Credit Hours: {course['credit_hours']}\n"
            f"Fee: Rs. {course['fee']}\n"
            f"Type: {course['type']}"
        )

    available_courses = ", ".join(courses.keys())

    return (
        f"Course '{course_name}' was not found.\n"
        f"Available courses: {available_courses}"
    )


@tool
def calculate_registration_fee(number_of_courses: int) -> str:
    """Calculate the estimated registration fee for a number of courses."""

    fee_per_course = 11000
    total_fee = number_of_courses * fee_per_course

    return (
        f"Number of courses: {number_of_courses}\n"
        f"Fee per course: Rs. {fee_per_course}\n"
        f"Estimated total fee: Rs. {total_fee}"
    )


@tool
def get_registration_deadline() -> str:
    """Get the university semester registration deadline."""

    return "The semester registration deadline is 30 August 2026."


@tool
def get_registration_requirements() -> str:
    """Get the requirements for university semester registration."""

    return """
Registration requirements:

1. Clear outstanding university dues.
2. Select courses according to the semester plan.
3. Check timetable conflicts.
4. Confirm selected courses.
5. Submit registration before the deadline.
"""


tools = [
    get_course_information,
    calculate_registration_fee,
    get_registration_deadline,
    get_registration_requirements
]