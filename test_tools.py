from tools import (
    get_course_information,
    calculate_registration_fee,
    get_registration_deadline,
    get_registration_requirements
)


print("----- COURSE INFORMATION -----")

print(
    get_course_information.invoke(
        {"course_name": "Artificial Intelligence"}
    )
)


print("\n----- FEE CALCULATOR -----")

print(
    calculate_registration_fee.invoke(
        {"number_of_courses": 4}
    )
)


print("\n----- REGISTRATION DEADLINE -----")

print(
    get_registration_deadline.invoke({})
)


print("\n----- REGISTRATION REQUIREMENTS -----")

print(
    get_registration_requirements.invoke({})
)