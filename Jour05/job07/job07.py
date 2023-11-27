def function(grades):
    notes_arrondies = []
    for i in grades:
        if i < 40:
            notes_arrondies.append(i)
        else:
            prochain_multiple_de_5 = ((i // 5) + 1) * 5
            if prochain_multiple_de_5 - i < 3:
                notes_arrondies.append(prochain_multiple_de_5)
            else:
                notes_arrondies.append(i) 
    return notes_arrondies
grades_list = [37, 82, 56, 91., 94.5]
notes_arrondies = function(grades_list)
print(notes_arrondies)
