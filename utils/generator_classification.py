import uuid,datetime,random,json
def generate_classification(acclassificationtype_id):
    if acclassificationtype_id == "a00a0322-b095-11ed-9bd8-0242ac110002":
        pool=[
            {"id": "5fae9dd9-b095-11ed-9bd8-0242ac110002" , "name": "Zapoctovano", "name_en": "Passed"},
            {"id": "5fae9dd7-b095-11ed-9bd8-0242ac110002" , "name": "Nezapoctovano", "name_en": "Failed"}]
    else:
        pool=[
            {"id": "5fae9dd8-b095-11ed-9bd8-0242ac110002", "name": "A", "name_en": "A"},
            {"id": "5faea134-b095-11ed-9bd8-0242ac110002", "name": "B", "name_en": "B"},
            {"id": "5faea21a-b095-11ed-9bd8-0242ac110002", "name": "C", "name_en": "C"},
            {"id": "5faea2d8-b095-11ed-9bd8-0242ac110002", "name": "D", "name_en": "D"},
            {"id": "5faea332-b095-11ed-9bd8-0242ac110002", "name": "E", "name_en": "E"},
            {"id": "5faea396-b095-11ed-9bd8-0242ac110002", "name": "F", "name_en": "F"}
            ]
    return random.choice(pool)
def generate_order(student_id,semester_id,acclassificationtype_id):
    rand_num = random.randint(0,99)
    if rand_num < 90 or acclassificationtype_id == "a00a0322-b095-11ed-9bd8-0242ac110002" :  # 90% probability or if the semester is zapocet
        return [
            new_classification(student_id,semester_id,acclassificationtype_id,order=1)
        ]
    elif rand_num < 99:  # 9% probability
        return [
            new_classification(student_id,semester_id,acclassificationtype_id,order=1),
            new_classification(student_id,semester_id,acclassificationtype_id,order=2)
        ]
    else:  # 1% probability 
        return [
            new_classification(student_id,semester_id,acclassificationtype_id,order=1),
            new_classification(student_id,semester_id,acclassificationtype_id,order=2),
            new_classification(student_id,semester_id,acclassificationtype_id,order=3)
        ]
def new_classification(student_id,semester_id,acclassificationtype_id,order):
    new_classification = {
            "id": str(uuid.uuid4()),  # Generate a new unique ID 
            "student_id": student_id,
            "semester_id":  semester_id,
            "classificationlevel_id": generate_classification(acclassificationtype_id)['id'],
            "order":order,
            "date": str(datetime.datetime.now())
            }
    return new_classification
def generate():
    with open('real_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    generated_classification = []
    for group in data['groups']:
        if group['grouptype_id'] == "cd49e157-610c-11ed-9312-001a7dda7110": #check if a group is study group 
            students_id = [m['user_id'] for m in data['memberships'] if m['group_id'] == group['id']] #retrive all student inside a study group
            if not students_id:
                continue
            program_id=None
            for program in data['acprograms_students']:
                if program['student_id'] == students_id[0]: #assuming all students inside a study group will have the same program
                    program_id=program['program_id']
            if not program_id:
                continue
            for subject in data['acsubjects']:
                if subject['program_id'] == program_id:
                    for semester in data['acsemester']:
                        if semester['subject_id'] == subject['id']:
                            acclassificationtype_id = semester['classificationtype_id']
                            semester_id=semester['id']
                            for student in students_id:
                                generated_classification.extend(generate_order(semester_id=semester_id, acclassificationtype_id=acclassificationtype_id, student_id=student))
    from data_checker import unique_instance
    temp=unique_instance(generated_classification)
    temp={"acclassifications": temp}
    with open('classification_official.json', 'w', encoding='utf-8') as f:
        json.dump(temp, f, ensure_ascii=False, indent=4)

                
                

                
            
generate()
       
                


        