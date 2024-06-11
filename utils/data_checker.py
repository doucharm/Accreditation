from sqlalchemy import select
def consistency_classification(classification,type_classification):
    if type_classification not in ['Z','z','zapocet','započet']:
        if classification not in ['A','B','C','D','E','F']:
            return False
    return True
def consistency_group(group):
    sample=group[0]
    for student in group:
        if sample['type_classification'] != student['type_classification']:
            return False
    return True
def unique_instance(list):
    data= []
    for item in list:
        if item not in data:
            data.append(item)
    print('Number of duplicated instances',len(list)-len(data))
    return data


    

