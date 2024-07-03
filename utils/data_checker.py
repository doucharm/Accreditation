def unique_instance(list):
    data= []
    full_data = []
    for item in list:
        item_important={
            'semester_id': item['semester_id'],
            'student_id' : item['student_id'],
            "classificationlevel_id" : item[ "classificationlevel_id"],
            "order": item['order']
        }
        if item_important not in data:
            data.append(item_important)
            full_data.append(item)
    print('Number of duplicated instances',len(list)-len(data))
    return full_data


    

