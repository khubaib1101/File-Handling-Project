def new_application():

    print("\nPersonal Information:")

    name = input("Enter your Full Name:")
    Fname = input("Enter your Father's Name:")
    Mname = input("Enter your Mother's Name:")
    date_of_birth = input("Enter your Date of Birth (DD/MM/YYYY):")
    gender = input("Enter your Gender (Male/Female/Other):")
    cncic = int(input("Enter your CNIC/B-Form Number:"))
    nationality = input("Enter your Nationality:")
    religion = input("Enter your Religion:")
    mob_number = int(input("Enter your Mobile Number:"))
    whattsapp_number = int(input("Enter your WhatsApp Number:"))
    email = input("Enter your Email Address:")
    domicile = input("Enter your Domicile Province:")
    domicile_district = input("Enter your Domicile District:")
    blood_group = input("Enter your Blood Group:")
    disability_status = input("Do you have any disability? (Yes/No):")

    with open("personal.txt", "a") as file:
        file.write("Name:" + name + "\n")
        file.write("Father's Name:" + Fname + "\n")
        file.write("Mother's Name:" + Mname + "\n")
        file.write("Date of Birth:" + date_of_birth + "\n")
        file.write("Gender:" + gender + "\n")
        file.write("CNIC/B-Form Number:" + str(cncic) + "\n")
        file.write("Nationality:" + nationality + "\n")
        file.write("Religion:" + religion + "\n")
        file.write("Mobile Number:" + str(mob_number) + "\n")
        file.write("WhatsApp Number:" + str(whattsapp_number) + "\n")
        file.write("Email Address:" + email + "\n")
        file.write("Domicile Province:" + domicile + "\n")
        file.write("Domicile District:" + domicile_district + "\n")
        file.write("Blood Group:" + blood_group + "\n")
        file.write("Disability Status:" + disability_status + "\n")
        file.write("\n")


    print("\nEnter your Guardian's Information:")

    name2 = input("Enter your Guardian's Full Name:")
    cnic2 = int(input("Enter your Guardian's CNIC Number:"))
    mob_number2 = int(input("Enter your Guardian's Mobile Number:"))
    occupation = input("Enter your Guardian's Occupation:")
    income = int(input("Enter your Guardian's Monthly Income:"))
    relationship = input("Enter your Relationship with Guardian:")

    with open("guardian.txt", "a") as file:
        file.write("Guardian's Name:" + name2 + "\n")
        file.write("Guardian's CNIC Number:" + str(cnic2) + "\n")
        file.write("Guardian's Mobile Number:" + str(mob_number2) + "\n")
        file.write("Guardian's Occupation:" + occupation + "\n")
        file.write("Guardian's Monthly Income:" + str(income) + "\n")
        file.write("Relationship with Guardian:" + relationship + "\n")
        file.write("\n")


    print("\nAddress Information:")

    permanent_address = input("Enter your Permanent Address(House/Street):")
    area = input("Enter your Area/Colony:")
    city = input("Enter your City:")
    district = input("Enter your District:")
    tehsil = input("Enter your Tehsil:")
    province = input("Enter your Province:")
    postal_code = int(input("Enter your Postal Code:"))

    same_address = input(
        "Is your Permanent Address same as your Correspondence Address? (Yes/No):"
    )

    if same_address.lower() == "yes":

        current_address = permanent_address
        current_city = city
        current_district = district
        current_tehsil = tehsil
        current_province = province
        current_postal_code = postal_code

    else:

        current_address = input(
            "Enter your Correspondence Address(House/Street):"
        )
        current_city = input("Enter your Correspondence City:")
        current_district = input("Enter your Correspondence District:")
        current_tehsil = input("Enter your Correspondence Tehsil:")
        current_province = input("Enter your Correspondence Province:")
        current_postal_code = int(
            input("Enter your Correspondence Postal Code:")
        )

    with open("address.txt", "a") as file:
        file.write("Permanent Address:" + permanent_address + "\n")
        file.write("Area/Colony:" + area + "\n")
        file.write("City:" + city + "\n")
        file.write("District:" + district + "\n")
        file.write("Tehsil:" + tehsil + "\n")
        file.write("Province:" + province + "\n")
        file.write("Postal Code:" + str(postal_code) + "\n")
        file.write("Correspondence Address:" + current_address + "\n")
        file.write("Correspondence City:" + current_city + "\n")
        file.write("Correspondence District:" + current_district + "\n")
        file.write("Correspondence Tehsil:" + current_tehsil + "\n")
        file.write("Correspondence Province:" + current_province + "\n")
        file.write("Correspondence Postal Code:" + str(current_postal_code) + "\n")
        file.write("\n")


    print("\nEducation Records:")

    education_records = []

    while True:

        qualification = input("Enter your Qualification:")
        board = input("Enter your Board/University:")
        institute = input("Enter your Institute Name:")
        year_of_passing = int(input("Enter your Year of Passing:"))
        total_marks = int(input("Enter your Total Marks:"))
        obtained_marks = int(input("Enter your Obtained Marks:"))

        percentage = (obtained_marks / total_marks) * 100

        print("Percentage:", percentage)

        grade = input("Enter your Grade:")
        roll_number = input("Enter your Roll Number:")

        records = {
            "Qualification": qualification,
            "Board/University": board,
            "Institute Name": institute,
            "Year of Passing": year_of_passing,
            "Total Marks": total_marks,
            "Obtained Marks": obtained_marks,
            "Percentage": percentage,
            "Grade": grade,
            "Roll Number": roll_number
        }

        education_records.append(records)

        another = input(
            "Do you want to add another education record? (Yes/No):"
        )

        if another.lower() != "yes":
            break

    with open("education.txt", "a") as file:

        for record in education_records:
            file.write(str(record) + "\n")

        file.write("\n")


    print("\nPrograms:")

    programs = [
        "BS Computer Science",
        "BS Software Engineering",
        "BS Information Technology",
        "BS Artificial Intelligence",
        "BS Accounting and Finance",
        "BS English",
        "BS Mathematics"
    ]

    for i in range(len(programs)):
        print(i + 1, programs[i])

    choice1 = input("Enter your First Choice Program (1-7):")
    choice2 = input("Enter your Second Choice Program (1-7):")
    choice3 = input("Enter your Third Choice Program (1-7):")

    campus = input("Enter your Preferred Campus (Main/City):")
    shift = input("Enter your Preferred Shift (Morning/Evening):")
    admission_category = input(
        "Enter your Admission Type (Regular/Self-Finance):"
    )

    with open("programs.txt", "a") as file:

        file.write(
            "First Choice Program:" + programs[int(choice1) - 1] + "\n"
        )

        file.write(
            "Second Choice Program:" + programs[int(choice2) - 1] + "\n"
        )

        file.write(
            "Third Choice Program:" + programs[int(choice3) - 1] + "\n"
        )

        file.write("Preferred Campus:" + campus + "\n")
        file.write("Preferred Shift:" + shift + "\n")
        file.write("Admission Type:" + admission_category + "\n")
        file.write("\n")


    print("\nDocuments:")

    documents = [
        "CNIC/B-Form",
        "Father/Guardian CNIC",
        "Matric Certificate",
        "Matric DMC",
        "Intermediate Certificate",
        "Intermediate DMC",
        "Domicile",
        "Passport Photograph",
        "Character Certificate",
        "Equivalence Certificate, if applicable",
        "Migration Certificate, if applicable"
    ]

    document_status = []

    for dcoment in documents:

        status = input(
            f"Have you submitted {dcoment}? (Yes/No):"
        )

        document_status.append(status)

    with open("documents.txt", "a") as file:

        file.write(
            "Document Submission Status:" +
            str(document_status) +
            "\n"
        )

        file.write("\n")


def search_application():

    cnic = input(
        "Enter your CNIC/B-Form Number to search your application:"
    )

    with open("personal.txt", "r") as file:
        personal_info = file.readlines()

    found = False

    for line in personal_info:

        if "CNIC/B-Form Number:" + cnic in line:

            found = True

            print("\nApplication Found!")
            print("----------------------")

            print("Personal Information:")
            for line in personal_info:
                print(line)

            break

    if found == False:
        print("Application not found.")


def declare_application():

    print(
        "Your application has been successfully submitted."
    )

    review = input(
        "Do you want to review your application before submission? (Yes/No):"
    )

    if review.lower() == "yes":
        search_application()

    else:
        print(
            "Thank you for submitting your application. "
            "We will contact you soon."
        )


def main():

    while True:

        print("\nWelcome to the University Admission System")
        print("1. Start New Application")
        print("2. Search Application")
        print("3. Exit")

        choice = input("Enter your choice (1-3):")

        if choice == "1":

            new_application()
            declare_application()

        elif choice == "2":

            search_application()

        elif choice == "3":

            print("Exiting the system. Goodbye!")
            break

        else:

            print("Invalid choice. Please try again.")


main()