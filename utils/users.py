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
        "company_name": None,
        "username": data.username,
        "is_bot": data.is_bot,
        "language_code": data.language_code,
        "status": "new",
        "role": "company",
        "profile_img": None,
        "description": None,
        "locations": None,
        "search": None,
        "salary": None
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


def edit_field_company(msg, field, value):
    data = msg.from_user
    msg_text = ""
    with open("data/company.json", "r") as file:
        emp = json.load(file)

    for user in emp:
        if user["id"] == data.id:
            user[field] = value["new_value"]

            # msg answer
            msg_text = (f"Your {field} was successfully updated! \n"
                        f"\n\n{field.capitalize()}: {value['new_value']}\n"
                        f"Company_name: {user['company_name']}\n"
                        f"username: {data.username}\n"
                        f"language code: {data.language_code}\n"
                        f"Status: {user['status']}\n"
                        f"Role: {user['role']}\n"
                        f"Profile image: {user['profile_img']}\n"
                        f"description: {user['description']}\n"
                        f"locations: {user['locations']}\n"
                        f"Search: {user['search']}\n"
                        f"Salary: {user['salary']}\n")

    with open("data/company.json", "w") as f:
        json.dump(emp, f, indent=4)

    return msg_text


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
                        f"locations: {user['locations']}\n"
                        f"Experience: {user['experience']}\n")

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


    if employee['status']:
        txt += f"📌 Status: {employee['status']}\n"
    else:
        txt += "📌 Status: Not specified\n"

    return txt


def get_company_text(company):
    txt = f"🔖 Username: {company.get('username', 'Not specified')}\n"

    txt += f"🏢 Company Name: {company.get('company_name', 'Not specified')}\n"

    txt += f"📝 Description: {company.get('description', 'Not specified')}\n"

    txt += f"📍 Locations: {company.get('locations', 'Not specified') or 'Not specified'}\n"

    txt += f"🖼️ Profile Image: {company.get('profile_img', 'Not specified') or 'Not specified'}\n"

    txt += f"📌 Status: {company.get('status', 'Not specified')}\n"

    txt += f"🔎 Search Tag: {company.get('search', 'Not specified')}\n"

    txt += f"💲 Salary : {company.get('salary', 'Not specified')}\n"

    return txt
