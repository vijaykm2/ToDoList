def tallest_people(**persons):
    temp_record = dict()
    max_height = max(persons.values())
    for name, height in persons.items():
        if max_height == height:
            temp_record[name] = height

    for name in sorted(temp_record.keys()):
        print(f'{name} : {temp_record[name]}')