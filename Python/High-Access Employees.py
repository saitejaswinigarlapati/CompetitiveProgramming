# High-Access Employees

from typing import List
from collections import defaultdict
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        emp=defaultdict(list)
        for name,time in access_times:
            minutes=int(time[:2])*60 + int(time[2:])
            emp[name].append(minutes)

        res=[]
        for name in emp:
            times=sorted(emp[name])
            for i in range(len(times)-2):
                if times[i+2] - times[i]<60:
                    res.append(name)
                    break
        return res
    
    
s=Solution()
access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]

print(s.findHighAccessEmployees(access_times))
    
# Input: access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]
# Output: ["a"]

# Input: access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]
# Output: ["c","d"]

# Input: access_times = [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]
# Output: ["ab","cd"]
        