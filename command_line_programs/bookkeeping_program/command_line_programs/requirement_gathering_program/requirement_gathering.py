import csv

# Define data storage dictionary
project_data = {
    "company_info": {},
    "stakeholders": {"internal": [], "external": []},
    "business_goals": [],
    "technical_goals": [],
    "gathering_techniques": [],
    "requirements": {"functional": [], "non_functional": []},
    "features": [],
    "use_cases": [],
    "validated_feedback": [],
    "project_management_questions": [],
    "technical_requirements": [],
    "branding_questions": [],
    "development_questions": [],
    "ui_ux_design_questions": [],
    "tdd_questions": []
}

# Function to modify a list with an option to go back
def modify_list(input_list, list_name, prev_step_func=None):
    while True:
        print(f"\nCurrent {list_name}: {input_list}")
        action = input("Would you like to add, edit, delete, continue, or go back? (a/e/d/c/b): ").lower()

        if action == 'a':  # Add
            item = input(f"Enter new {list_name[:-1]}: ")
            input_list.append(item)

        elif action == 'e':  # Edit
            index = int(input(f"Enter the index number of the {list_name[:-1]} to edit (0-based index): "))
            if 0 <= index < len(input_list):
                new_item = input(f"Enter new value for {list_name[:-1]}: ")
                input_list[index] = new_item
            else:
                print("Invalid index. Please try again.")

        elif action == 'd':  # Delete
            index = int(input(f"Enter the index number of the {list_name[:-1]} to delete (0-based index): "))
            if 0 <= index < len(input_list):
                input_list.pop(index)
            else:
                print("Invalid index. Please try again.")

        elif action == 'c':  # Continue
            break

        elif action == 'b' and prev_step_func:  # Go Back
            prev_step_func()
            return  # Return immediately to re-invoke the previous step

        else:
            print("Invalid choice. Please enter 'a' to add, 'e' to edit, 'd' to delete, 'c' to continue, or 'b' to go back.")

# Function to modify stakeholder details with an option to go back
def modify_stakeholders(stakeholder_list, stakeholder_type, prev_step_func=None):
    while True:
        print(f"\nCurrent {stakeholder_type.capitalize()} Stakeholders:")
        for idx, s in enumerate(stakeholder_list):
            print(f"{idx}. {s['first_name']} {s['last_name']}, {s['title']} (Email: {s['email']})")

        action = input("Would you like to add, edit, delete, continue, or go back? (a/e/d/c/b): ").lower()

        if action == 'a':  # Add
            add_stakeholder(stakeholder_list)

        elif action == 'e':  # Edit
            index = int(input("Enter the index number of the stakeholder to edit (0-based index): "))
            if 0 <= index < len(stakeholder_list):
                edit_stakeholder(stakeholder_list, index)
            else:
                print("Invalid index. Please try again.")

        elif action == 'd':  # Delete
            index = int(input("Enter the index number of the stakeholder to delete (0-based index): "))
            if 0 <= index < len(stakeholder_list):
                stakeholder_list.pop(index)
            else:
                print("Invalid index. Please try again.")

        elif action == 'c':  # Continue
            break

        elif action == 'b' and prev_step_func:  # Go Back
            prev_step_func()
            return  # Return immediately to re-invoke the previous step

        else:
            print("Invalid choice. Please enter 'a' to add, 'e' to edit, 'd' to delete, 'c' to continue, or 'b' to go back.")

# Function to add stakeholder
def add_stakeholder(stakeholder_list):
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    title = input("Title: ")

    stakeholder = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "title": title
    }

    stakeholder_list.append(stakeholder)

# Function to edit stakeholder
def edit_stakeholder(stakeholder_list, index):
    print(f"Editing Stakeholder: {stakeholder_list[index]}")
    stakeholder_list[index]['first_name'] = input("First Name: ")
    stakeholder_list[index]['last_name'] = input("Last Name: ")
    stakeholder_list[index]['email'] = input("Email: ")
    stakeholder_list[index]['title'] = input("Title: ")

# Step 1: Company Information
def step1():
    print("\n--- Step 1: Company Information ---")
    project_data['company_info']['name'] = input("Enter the company name: ")
    project_data['company_info']['url'] = input("Enter the company URL: ")

# Step 2: Understand the Project Context
def step2():
    print("\n--- Step 2: Understand the Project Context ---")
    project_data['company_info']['objective'] = input("Enter the objective of the mobile banking application: ")

    # Internal Stakeholders
    print("\nEnter Internal Stakeholders (provide details):")
    modify_stakeholders(project_data['stakeholders']['internal'], 'internal', step2)

    # External Stakeholders
    print("\nEnter External Stakeholders (provide details):")
    modify_stakeholders(project_data['stakeholders']['external'], 'external', step2)

# Step 3: Define Goals and Objectives
def step3():
    print("\n--- Step 3: Define Goals and Objectives ---")
    print("\nEnter Business Goals:")
    modify_list(project_data['business_goals'], 'Business Goals', step2)

    print("\nEnter Technical Goals:")
    modify_list(project_data['technical_goals'], 'Technical Goals', step3)

# Step 4: Plan the Requirement Gathering Process
def step4():
    print("\n--- Step 4: Plan the Requirement Gathering Process ---")
    print("Select Requirement Gathering Techniques:")
    modify_list(project_data['gathering_techniques'], 'Requirement Gathering Techniques', step3)

# Step 5: Conduct Requirement Gathering Sessions
def step5():
    print("\n--- Step 5: Conduct Requirement Gathering Sessions ---")
    print("\nEnter Functional Requirements:")
    modify_list(project_data['requirements']["functional"], 'Functional Requirements', step4)

    print("\nEnter Non-Functional Requirements:")
    modify_list(project_data['requirements']["non_functional"], 'Non-Functional Requirements', step5)

# Step 6: Document Requirements
def step6():
    print("\n--- Step 6: Document Requirements ---")
    print("\nDefine Features:")
    modify_list(project_data['features'], 'Features', step5)

    print("\nDescribe Use Cases:")
    modify_list(project_data['use_cases'], 'Use Cases', step6)

# Step 7: Validate Requirements
def step7():
    print("\n--- Step 7: Validate Requirements ---")
    print("Collect feedback on the requirements and make necessary adjustments.")
    modify_list(project_data['validated_feedback'], 'Feedback and Adjustments', step6)

# Step 8: Answer Technical Project Management Questions
def step8():
    print("\n--- Step 8: Technical Project Management Questions ---")
    questions = [
        "What are the key deliverables of this project?",
        "What are the main risks associated with this project?",
        "What is the estimated timeline for project completion?",
        "What is the budget allocated for this project?",
        "Who are the key stakeholders and their roles?",
        "What tools and technologies will be used in this project?",
        "How will project progress be tracked and reported?",
        "What are the communication protocols for the project?",
        "What are the quality assurance measures in place?",
        "How will changes to the project scope be managed?",
        "What is the project team structure?",
        "What are the dependencies and constraints of the project?",
        "What are the criteria for project success?",
        "What are the post-deployment support plans?",
        "How will knowledge transfer be handled at the end of the project?"
    ]

    for question in questions:
        answer = input(f"{question} ")
        project_data['project_management_questions'].append({"question": question, "answer": answer})

# Step 9: System Architecture Design Questions
def step9():
    print("\n--- Step 9: System Architecture Design Questions ---")

    # Technical Requirement Questions
    print("\nTechnical Requirement Questions:")
    tech_questions = [
        "What are the performance requirements?",
        "What is the expected system load?",
        "How will the system handle scalability?",
        "What are the security requirements?",
        "What databases will be used?",
        "What backup and recovery plans are in place?",
        "What are the data retention policies?",
        "What APIs need to be integrated?",
        "What network protocols will be used?",
        "What is the architecture pattern (e.g., microservices, monolithic)?",
        "How will user authentication be managed?",
        "What are the logging and monitoring requirements?",
        "What is the failover strategy?",
        "What are the requirements for data encryption?",
        "How will compliance requirements (e.g., GDPR) be met?"
    ]

    for question in tech_questions:
        answer = input(f"{question} ")
        project_data['technical_requirements'].append({"question": question, "answer": answer})

    # Branding Questions
    print("\nBranding Questions:")
    branding_questions_list = [
        "What are the primary colors for the application?",
        "What font styles will be used?",
        "How will the brand logo be integrated?",
        "What is the tone of voice for the app?",
        "What are the guidelines for brand imagery?",
        "What is the style of the icons used in the application?",
        "How should the app's navigation feel (e.g., modern, classic)?",
        "Are there specific animations or transitions to be used?",
        "How will the app differentiate itself visually from competitors?",
        "What is the brand's personality, and how should it be reflected?",
        "Are there any accessibility considerations for branding?",
        "How should the app look in dark mode versus light mode?",
        "What are the guidelines for micro-interactions in the app?",
        "What type of imagery (photography, illustrations) will be used?",
        "How should errors and alerts be branded (e.g., colors, icons)?"
    ]

    for question in branding_questions_list:
        answer = input(f"{question} ")
        project_data['branding_questions'].append({"question": question, "answer": answer})

    # Development Questions
    print("\nDevelopment Questions:")
    development_questions_list = [
        "What development frameworks and libraries will be used?",
        "How will the code be structured and organized?",
        "What are the coding standards and best practices?",
        "How will testing be integrated into the development process?",
        "What is the process for code reviews and approvals?",
        "How will version control be managed?",
        "What continuous integration and deployment tools will be used?",
        "How will development be documented?",
        "What are the key milestones in the development timeline?",
        "How will the development team communicate and collaborate?"
    ]

    for question in development_questions_list:
        answer = input(f"{question} ")
        project_data['development_questions'].append({"question": question, "answer": answer})

# Step 10: UI/UX Design Questions
def step10():
    print("\n--- Step 10: UI/UX Design Questions ---")
    ui_ux_questions = [
        "What design system will be used (e.g., Material Design, Bootstrap)?",
        "What are the core UI components required (buttons, forms, etc.)?",
        "How should the navigation be structured?",
        "What are the key user flows to design for?",
        "What accessibility standards will be followed?",
        "How should error states and feedback be handled?",
        "What are the guidelines for responsiveness across devices?",
        "What typography and font sizes will be used?",
        "What color schemes are to be implemented?",
        "How should loading states and progress indicators look?",
        "What are the micro-interactions that need to be included?",
        "What style should be used for icons and graphics?",
        "How will user onboarding be designed?",
        "What is the approach for localization and internationalization?",
        "How will the UI maintain consistency across updates?"
    ]

    for question in ui_ux_questions:
        answer = input(f"{question} ")
        project_data['ui_ux_design_questions'].append({"question": question, "answer": answer})

# Step 11: Technical Design Document (TDD) Questions
def step11():
    print("\n--- Step 11: Technical Design Document (TDD) Questions ---")
    tdd_questions_list = [
        "What are the key components of the system architecture?",
        "How will data flow between different components?",
        "What are the technical specifications for each module?",
        "What are the integration points with external systems?",
        "What are the error handling and logging strategies?",
        "How will security be implemented at different levels?",
        "What are the performance optimization strategies?",
        "What testing strategies will be used for each module?",
        "What are the database design and schema requirements?",
        "How will configuration management be handled?",
        "What are the dependencies between different modules?",
        "What are the hardware and software requirements?",
        "What is the disaster recovery plan?",
        "What are the system's scalability considerations?",
        "How will the system support multi-tenancy?"
    ]

    for question in tdd_questions_list:
        answer = input(f"{question} ")
        project_data['tdd_questions'].append({"question": question, "answer": answer})

# Step 12: Finalize and Sign-Off
def step12():
    print("\n--- Step 12: Finalize and Sign-Off ---")
    input("Press Enter to finalize requirements and obtain sign-off from stakeholders...")

# Step 13: Transition to Design and Development Phases
def step13():
    print("\n--- Step 13: Transition to Design and Development Phases ---")
    input("Press Enter to transition to the design and development phases...")

# Function to save data to a CSV file
def save_to_csv(data, filename="project_data.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Section", "Question", "Answer"])

        # Write company information
        writer.writerow(["Company Information", "Company Name", data['company_info'].get('name', '')])
        writer.writerow(["Company Information", "Company URL", data['company_info'].get('url', '')])
        writer.writerow(["Company Information", "Objective", data['company_info'].get('objective', '')])

        # Write stakeholder information
        for role, stakeholders in data['stakeholders'].items():
            for stakeholder in stakeholders:
                writer.writerow([f"{role.capitalize()} Stakeholder", "Name", f"{stakeholder['first_name']} {stakeholder['last_name']}"])
                writer.writerow([f"{role.capitalize()} Stakeholder", "Email", stakeholder['email']])
                writer.writerow([f"{role.capitalize()} Stakeholder", "Title", stakeholder['title']])

        # Write goals and objectives
        writer.writerow(["Goals and Objectives", "Business Goals", ', '.join(data['business_goals'])])
        writer.writerow(["Goals and Objectives", "Technical Goals", ', '.join(data['technical_goals'])])

        # Write requirement gathering techniques
        writer.writerow(["Requirement Gathering Techniques", "Techniques", ', '.join(data['gathering_techniques'])])

        # Write requirements
        for req_type, reqs in data['requirements'].items():
            for req in reqs:
                writer.writerow([f"{req_type.capitalize()} Requirements", "Requirement", req])

        # Write features and use cases
        writer.writerow(["Features and Use Cases", "Features", ', '.join(data['features'])])
        writer.writerow(["Features and Use Cases", "Use Cases", ', '.join(data['use_cases'])])

        # Write validated feedback
        writer.writerow(["Validated Feedback", "Feedback/Adjustments", ', '.join(data['validated_feedback'])])

        # Write all question sections
        sections = {
            "project_management_questions": "Technical Project Management Questions",
            "technical_requirements": "Technical Requirement Questions",
            "branding_questions": "Branding Questions",
            "development_questions": "Development Questions",
            "ui_ux_design_questions": "UI/UX Design Questions",
            "tdd_questions": "Technical Design Document (TDD) Questions"
        }

        for section_key, section_name in sections.items():
            for qa in data[section_key]:
                writer.writerow([section_name, qa['question'], qa['answer']])

# Function to print the final summary report
def print_summary():
    print("\n--- Summary of Requirement Gathering ---")

    print("\nCompany Information:")
    print(f"Company Name: {project_data['company_info']['name']}")
    print(f"Company URL: {project_data['company_info']['url']}")
    print(f"Objective: {project_data['company_info'].get('objective', 'N/A')}")

    print("\nInternal Stakeholders:")
    for s in project_data['stakeholders']['internal']:
        print(f"- {s['first_name']} {s['last_name']}, {s['title']} (Email: {s['email']})")

    print("\nExternal Stakeholders:")
    for s in project_data['stakeholders']['external']:
        print(f"- {s['first_name']} {s['last_name']}, {s['title']} (Email: {s['email']})")

    print("\nGoals and Objectives:")
    print(f"Business Goals: {', '.join(project_data['business_goals'])}")
    print(f"Technical Goals: {', '.join(project_data['technical_goals'])}")

    print("\nRequirement Gathering Techniques Used:")
    print(", ".join(project_data['gathering_techniques']))

    print("\nDocumented Requirements:")
    print("Functional Requirements: ")
    for req in project_data['requirements']["functional"]:
        print(f"- {req}")
    print("Non-Functional Requirements: ")
    for req in project_data['requirements']["non_functional"]:
        print(f"- {req}")

    print("\nFeatures and Use Cases:")
    print(f"Features: {', '.join(project_data['features'])}")
    print(f"Use Cases: {', '.join(project_data['use_cases'])}")

    print("\nValidated Feedback and Adjustments:")
    print(f"Feedback/Adjustments: {', '.join(project_data['validated_feedback'])}")

    print("\nTechnical Project Management Questions and Answers:")
    for qa in project_data['project_management_questions']:
        print(f"Q: {qa['question']}")
        print(f"A: {qa['answer']}")

    print("\nTechnical Requirement Questions and Answers:")
    for qa in project_data['technical_requirements']:
        print(f"Q: {qa['question']}")
        print(f"A: {qa['answer']}")

    print("\nBranding Questions and Answers:")
    for qa in project_data['branding_questions']:
        print(f"Q: {qa['question']}")
        print(f"A: {qa['answer']}")

    print("\nDevelopment Questions and Answers:")
    for qa in project_data['development_questions']:
        print(f"Q: {qa['question']}")
        print(f"A: {qa['answer']}")

    print("\nUI/UX Design Questions and Answers:")
    for qa in project_data['ui_ux_design_questions']:
        print(f"Q: {qa['question']}")
        print(f"A: {qa['answer']}")

    print("\nTechnical Design Document (TDD) Questions and Answers:")
    for qa in project_data['tdd_questions']:
        print(f"Q: {qa['question']}")
        print(f"A: {qa['answer']}")

    print("\nRequirements finalized and signed off. Ready to transition to design and development.")

# Run the steps in sequence
step1()
step2()
step3()
step4()
step5()
step6()
step7()
step8()
step9()
step10()
step11()
step12()
step13()

# Print the summary report
print_summary()

# Save the collected data to a CSV file
save_to_csv(project_data)
print("\nData has been saved to 'project_data.csv' in the current directory.")
