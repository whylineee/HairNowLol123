import json

def add_new_employee(data):
    userDataItem = {
        "id": data.id,
        "full_name": data.full_name,
        "username": data.username,
        "is_bot": data.is_bot,
        "language_code": data.language_code,
        "status": "new",
        "role": "employee",
        "profile_img": None,
        "description": None,
        "skills": None,
        "locations": None,
        "experience": None,
        "direction": None,
        "salary": None,
    }

    # Read from file
    with open("data/employee.json", "r") as file:
        emp = json.load(file)

    # Check if user already exists
    for user in emp:
        if user["id"] == data.id:
            return

    # Add new user
    emp.append(userDataItem)

    # Write to file
    with open("data/employee.json", "w") as f:
        json.dump(emp, f, indent=4)

def edit_field_employee(data, field, value):
    print(data, field, value)
    # with open("data/employee.json", "r") as file:
    #     emp = json.load(file)
    #
    # for user in emp:
    #     if user["id"] == data.id:
    #         user[field] = value
    #
    # with open("data/employee.json", "w") as f:
    #     json.dump(emp, f, indent=4)
