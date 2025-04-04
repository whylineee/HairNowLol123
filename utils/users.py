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

def add_new_company(data):
    userDataItem = {
        "id": data.id,
        "full_name": data.full_name,
        "username": data.username,
        "is_bot": data.is_bot,
        "language_code": data.language_code,
        "status": "new",
        "role": "company",
        "profile_img": None,
        "description": None,
        "locations": None,
        "vacancies": []
    }

    # Read from file
    with open("data/company.json", "r") as file:
        emp = json.load(file)

    # Check if user already exists
    for user in emp:
        if user["id"] == data.id:
            return

    # Add new user
    emp.append(userDataItem)

    # Write to file
    with open("data/company.json", "w") as f:
        json.dump(emp, f, indent=4)


def edit_field_employee(msg, field, value):
    data = msg.from_user
    msg_text = ""
    with open("data/employee.json", "r") as file:
        emp = json.load(file)

    for user in emp:
        if user["id"] == data.id:
            user[field] = value["new_value"]

            # msg answer
            msg_text = (f"Your {field} was successfully updated! \n"
                        f"\n\n{field.capitalize()}: {value['new_value']}\n"
                        f"Name: {data.full_name}\n"
                        f"Username: {data.username}\n"
                        f"Language code: {data.language_code}\n"
                        f"Status: {user['status']}\n"
                        f"Role: {user['role']}\n"
                        f"Profile image: {user['profile_img']}\n"
                        f"Description: {user['description']}\n"
                        f"Skills: {user['skills']}\n"
                        f"Experience: {user['experience']}\n"
                        f"Direction: {user['direction']}\n")

    with open("data/employee.json", "w") as f:
        json.dump(emp, f, indent=4)

    return msg_text


def get_employee_text(employee):
    txt = (
        f"👤 Name: {employee['full_name']}\n"
        f"🔖 Username: {employee['username']}\n"
    )

    if employee['skills']:
        txt += f"🛠️ Skills: {employee['skills']}\n"
    else:
        txt += "🛠️ Skills: Not specified\n"

    if employee['experience']:
        txt += f"💼 Experience: {employee['experience']}\n"
    else:
        txt += "💼 Experience: Not specified\n\n"

    if employee['description']:
        txt += f"📝 Description: {employee['description']}\n"
    else:
        txt += "📝 Description: Not specified\n"

    if employee['locations']:
        txt += f"📍 Locations: {employee['locations']}\n"
    else:
        txt += "📍 Locations: Not specified\n"

    if employee['profile_img']:
        txt += f"🖼️ Profile Image: {employee['profile_img']}\n"
    else:
        txt += "🖼️ Profile Image: Not specified\n\n"

    if employee['status']:
        txt += f"📌 Status: {employee['status']}\n"
    else:
        txt += "📌 Status: Not specified\n"

    return txt
