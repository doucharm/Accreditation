import uuid,datetime,random
def generate_classification(classification_type):
    if classification_type in ['Z','z','zapocet','započet']:
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
    return random.choice|(pool)
def generate_order():
    rand_num = random.randint(0, 99)
    if rand_num < 90:  # 90% probability
        return 1
    elif rand_num < 99:  # 9% probability
        return 2
    else:  # 1% probability 
        return 3
    
def add_credit(object):
    new_answer = {
            "id": str(uuid.uuid4()),  # Generate a new unique ID 
            "student_id": object['student_id'],
            "semester_id": object['semester_id'],
            "classificationlevel_id": generate_classification(object['classification_type'])['id'],
            "order":generate_order(),
            "date": datetime.datetime}
