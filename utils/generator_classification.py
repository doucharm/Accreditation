import uuid,datetime,random,json
def generate_classification(acclassificationtypes):
    if acclassificationtypes == "a00a0322-b095-11ed-9bd8-0242ac110002":
        pool=[
            {"id": "5fae9dd9-b095-11ed-9bd8-0242ac110002" , "name": "Zapoctovano", "name_en": "Passed"},
            {"id": "5fae9dd7-b095-11ed-9bd8-0242ac110002" , "name": "Nezapoctovano", "name_en": "Failed"}]
    else:
        pool=[
            {"id": "5fae9dd8-b095-11ed-9bd8-0242ac110002" , "name": "A", "name_en": "A"},
            {"id": "5faea134-b095-11ed-9bd8-0242ac110002" , "name": "B", "name_en": "B"},
            {"id": "5faea21a-b095-11ed-9bd8-0242ac110002" , "name": "C", "name_en": "C"},
            {"id": "5faea2d8-b095-11ed-9bd8-0242ac110002" , "name": "D", "name_en": "D"},
            {"id": "5faea332-b095-11ed-9bd8-0242ac110002" , "name": "E", "name_en": "E"},
            {"id": "5faea396-b095-11ed-9bd8-0242ac110002" , "name": "F", "name_en": "F"}] 
    return random.choice(pool)
def generate_order():
    rand_num = random.randint(0, 99)
    if rand_num < 90:  # 90% probability
        return 1
    elif rand_num < 99:  # 9% probability
        return 2
    else:  # 1% probability 
        return 3
def new_classification(student_id,semester_id,classificationtype_id):
    new_classification = {
            "id": str(uuid.uuid4()),  # Generate a new unique ID 
            "student_id": student_id,
            "semester_id": semester_id,
            "classificationlevel_id": generate_classification(classificationtype_id)['id'],
            "order":generate_order(),
            "date": str(datetime.datetime.now())
            }
    return new_classification
with open('systemdata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
generated_classification = []

for group in data['groups']:
    if group['grouptype_id'] == "cd49e157-610c-11ed-9312-001a7dda7110":
        students_id = [m['user_id'] for m in data['memberships'] if m['group_id'] == group['id']]
        if not students_id:
            continue
        program_id = next(program['program_id'] for program in data['acprograms_students'] if program['student_id'] == students_id[0])
        subjects = [subject for subject in data['acsubjects'] if subject['program_id'] == program_id]
        for subject in subjects:
            semester = next(semester for semester in data['acsemesters'] if semester['subject_id'] == subject['id'])
            classificationtype_id = semester['classificationtype_id']
            generated_classification.extend([new_classification(semester_id=semester['id'], classificationtype_id=classificationtype_id, student_id=student) for student in students_id])
with open('classification.json', 'w', encoding='utf-8') as f:
    json.dump(generated_classification, f, ensure_ascii=False, indent=4)

            

                
            

       
                


        