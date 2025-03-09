import bisect
class interval:
    def __init__(self):
        self.intr=[]
        self.in_min=0
        self.in_max=0
    def addinterval(self,x,y):
        new_intr=[x,y]
        i = bisect.bisect_left(self.intr, new_intr)
        self.intr.insert(i, new_intr)
        self._merge(self.intr)

    def _merge(self, intervals):
        merged = []
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval
        merged.append(prev)
        self.intr=merged
    def retrieve(self):
        return self.intr
# given test case 
intr_m= interval()
intr_m.addinterval(1,5)
intr_m.addinterval(6,8)
intr_m.addinterval(4,7)
print(intr_m.retrieve())
#getting an output as [[1,8]]
#Another test cases: 
intr_2=interval()
intr_2.addinterval(1,2)
intr_2.addinterval(3,4)
intr_2.addinterval(4,8)
print(intr_2.retrieve())
#getting an output [[1,2],[3,8]]
intr_2.addinterval(1,8)
print(intr_2.retrieve())
#getting an output [[1,8]]
#
