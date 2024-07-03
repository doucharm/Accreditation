def unique_instance(list):
    data= []
    for item in list:
        item_important={
            'semester_id': item['semester_id'],
            'student_id' : item['student_id'],
            "classificationlevel_id" : item[ "classificationlevel_id"],
            "order": item['order']
        }
        if item_important not in data:
            data.append(item)
    print('Number of duplicated instances',len(list)-len(data))
    return data


    

