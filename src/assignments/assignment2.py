def faculty_evaluation_result(nev, rar, som, oft, voft, alw):
    '''
    Write code to calculate faculty evaluation rating according to asssignment instructions

    :param nev: Never
    :param rar: Rarely
    :param som: Sometimes
    :param oft: Often
    :param voft: Very Often
    :param alw: Always
    :return: rating as a string
    '''
    total=nev+rar+som+oft+voft+alw

    if (voft+alw)/total >= 0.9:
        return "Excellent"
    elif (oft+voft+alw)/total >= 0.8:
        return "Very Good"
    elif (som+oft+voft+alw)/total >= 0.7:
        return "Good"
    elif (rar+som+oft+voft+alw)/total >= 0.6:
        return "Needs Improvement"
    else:
        return "Unacceptable"

    
def get_ratings(nev,rar,som, oft,voft, alw):
    '''
    Students aren't expected to know this material yet!
    '''
    ratings = []
    total = nev + rar + som + oft + voft + alw

    ratings.append(round(alw / total, 2))
    ratings.append(round(voft / total, 2))
    ratings.append(round(oft / total, 2))
    ratings.append(round(som / total, 2))
    ratings.append(round(rar / total, 2))
    ratings.append(round(nev / total, 2))

    return ratings
    

    
