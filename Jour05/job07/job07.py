def function(grades):
    round = []
    for i in grades:
        if i < 40:
            round.append(i)
        else:
            multiple_5 = ((i // 5) + 1) * 5
            if multiple_5 - i < 3:
               round.append(multiple_5)
            else:
                round.append(i) 
    return round
grades_list = [37, 82, 56, 91., 94.5]
round= function(grades_list)
print(round)
