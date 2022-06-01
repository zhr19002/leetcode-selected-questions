from collections import defaultdict

class Solution:
    def __init__(self):
        self.path = []
        self.tickets_dict = defaultdict(list)
    
    def findItinerary(self, tickets):
        self.path = ['JFK']
        self.tickets_dict.clear()
        for item in tickets:
            self.tickets_dict[item[0]].append(item[1])
        self.backtrack(tickets, 'JFK')
        return self.path
    
    def backtrack(self, tickets, startPoint):
        if len(self.path) == len(tickets) + 1:
            return True
        self.tickets_dict[startPoint].sort()
        for i in self.tickets_dict[startPoint]:
            endPoint = self.tickets_dict[startPoint].pop(0)
            self.path.append(endPoint)
            if self.backtrack(tickets, endPoint):
                return True
            self.path.pop()
            self.tickets_dict[startPoint].append(endPoint)

s = Solution()
print(s.findItinerary([['MUC','LHR'],['JFK','MUC'],['SFO','SJC'],['LHR','SFO']]))
print(s.findItinerary([['JFK','SFO'],['JFK','ATL'],['SFO','ATL'],['ATL','JFK'],['ATL','SFO']]))