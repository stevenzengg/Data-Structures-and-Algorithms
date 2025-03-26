# STEVEN IMPLEMENTATION
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ballot = defaultdict(lambda: [0] * len(votes[0]))

        for voter in votes:
            for i, vote in enumerate(voter):
                ballot[vote][i] += 1

        sorted_teams = sorted(ballot.keys(), key = lambda x: (ballot[x], -ord(x)), reverse = True)
        return "".join(sorted_teams)
        

