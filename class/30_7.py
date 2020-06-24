korean, english, mathmatics, science = map(int, input().split())

def get_min_max_score(*dataList):
    return [min(dataList), max(dataList)]

def get_average(korean=0, english=0, mathmatics=0, science=0):
    scoreList = [korean, english, mathmatics, science]
    return sum(scoreList)/len(scoreList)

min_score, max_score = get_min_max_score(korean, english, mathmatics, science)
average_score = get_average(korean=korean, english=english, mathmatics=mathmatics, science=science)
print('낮은 점수: {0:2f}, 높은 점수: {1:.2f}, 평균 점수 : {2:.2f}'.format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:2f}, 높은 점수: {1:.2f}, 평균 점수 : {2:.2f}'.format(min_score, max_score, average_score))