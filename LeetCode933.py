class RecentCounter:

    def __init__(self):
        self.requestQueue = []

    def ping(self, t: int) -> int:
        counter  = 0 
        self.requestQueue.append(t) 
        for i in self.requestQueue:
          if(  t - 3000 <= i <= t):
              counter += 1
                
        return counter
requests = [1,100,3001,3002]
a = RecentCounter()
for i in requests:
    
    print(a.ping(i))