from my_dict import dict_result

print(dict_result())
mapping = {}

new_dict = dict_result()
for i in new_dict.items():
    #print(i)
    node = {
            'description': i[0] 
        }
        if i in mapping:
            mapping[i].append(i)