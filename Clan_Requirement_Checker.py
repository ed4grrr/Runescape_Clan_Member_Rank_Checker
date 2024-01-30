import UsefulLists

class clan_Requirement_Checker:

    def __init__(self):
        self.experience_needed_for_Rank = UsefulLists.TCK_Default_Experience



    def change_experience_for_rank(self,rank,xp):
        """
        This will allow for the default minimum rank experience values to be changed.

        :param rank: The name of the rank in a string
        :param xp: The experienc required in an int
        :return: None/updates rank dict for new values.
        """
        self.experience_needed_for_Rank.update(rank,xp)


    def check_for_rank_up(self,player_name,clan_list):

