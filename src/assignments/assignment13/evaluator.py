class Evaluator:

    def faculty_evaluation_result(self, nev, rar, som, oft, voft, alw):
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
        total = nev + rar + som + oft + voft + alw

        alw_percent = alw / total * 100
        voft_percent = voft / total * 100
        oft_percent = oft / total * 100
        som_percent = som / total * 100
        rar_percent = rar / total * 100

        if voft_percent + alw_percent >= 90:
            return "Excellent"
        elif oft_percent + voft_percent + alw_percent >= 80:
            return "Very Good"
        elif som_percent + oft_percent + voft_percent + alw_percent >= 70:
            return "Good"
        elif rar_percent + som_percent + oft_percent + voft_percent + alw_percent >= 60:
            return "Needs Improvement"
        else:
            return "Unacceptable"

    def get_ratings(self, nev,rar,som, oft,voft, alw):
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
