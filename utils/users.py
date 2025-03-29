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


def edit_field_employee(msg, field, value):
    data = msg.from_user
    msg_text = ""
    with open("data/employee.json", "r") as file:
        emp = json.load(file)

    for user in emp:
        if user["id"] == data.id:
            user[field] = value["edit_desc"]
            msg_text = (f"Your {field} was successfully updated! \n"
                        f"\n\n{field.capitalize()}: {value['edit_desc']}\n"
                        f"Name: {data.full_name}\n"
                        f"Username: {data.username}\n"
                        f"Language code: {data.language_code}\n"
                        f"Status: {user['status']}\n"
                        f"Role: {user['role']}\n"
                        f"Profile image: {user['profile_img']}\n"
                        f"Description: {user['description']}\n"
                        f"Skills: {user['skills']}\n"
                        f"Locations: {user['locations']}\n"
                        f"Experience: {user['experience']}\n"
                        f"Direction: {user['direction']}\n"
                        f"Salary: {user['salary']}\n")

    with open("data/employee.json", "w") as f:
        json.dump(emp, f, indent=4)

    return msg_text
