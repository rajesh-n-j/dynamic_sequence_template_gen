def dynamic_sequence_template_gen(number):
    static_template = {"0":"A","1": "B", "2":"C", "3":"D","4":"E","5":"F","6":"G","7":"H","8":"I","9":"J"}
    created_temp = {}
    for idx in range(1,number+1):
        created_number_temp = ""
        for idn in str(idx):
            created_number_temp += static_template[idn]
        created_temp[idx]= created_number_temp   
    return created_temp

print(dynamic_sequence_template_gen(25))
