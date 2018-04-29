from src.homework.homework11.score_entry import ScoreEntry

class GameLog:

    def __init__(self):

        self.score_entries = []

    def add_score_entry(self, score_entry):

        self.score_entries.append(score_entry)

    def display_log(self):

        print('Id', 'Die 1', 'Die 2')
        for score_entry in self.score_entries:
            print(score_entry.score_entry_id, format(score_entry.die1_value, '4d'), \
                  format(score_entry.die2_value, '4d'))
