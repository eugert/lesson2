school_scores = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [3,4,4,5,3,4]},
    {'school_class': '5a', 'scores': [4,5,3,5]},
    {'school_class': '5b', 'scores': [5,3,4,5,3,5]}
]
# print (school_scores)
scholl_avg_scores = []
school_scores_sum = 0
school_scores_cnt = 0

for one_class in school_scores:
    avg_scores = {}
    # print(one_class)
    class_scores_sum = 0
    class_scores_cnt = 0
    for scores in one_class['scores']:
        # print(scores)
        class_scores_sum = class_scores_sum + scores
        class_scores_cnt = class_scores_cnt + 1 
        
    avg_scores['school_class'] = one_class['school_class']
    avg_scores['avg_scores'] = class_scores_sum / class_scores_cnt
    print('Класс ' + avg_scores['school_class'] + ' - средняя оценка ' + str(avg_scores))

    school_scores_sum = school_scores_sum + class_scores_sum
    school_scores_cnt = school_scores_cnt + class_scores_cnt

school_avg = school_scores_sum / school_scores_cnt
print ('Средня оценка по школе ' + str(school_avg))
