class Solution:

    def knapSack(self, W, wt, val):
        
        return self.checkKnapSack(W, 0, wt, val)
       
    def checkKnapSack(self, W, V, wt, val):
        
        if len(wt) < 1:
            return V
        if W - wt[0] >= 0:
            return max(self.checkKnapSack(W-wt[0], V+val[0], wt[1:], val[1:]), self.checkKnapSack(W, V, wt[1:], val[1:]))
        else:
            print("Excluded object:", val[0], wt[0])
            return self.checkKnapSack(W, V, wt[1:], val[1:])

    def carAssembly(self, assembly, tswitch, entry, exit):
      
        N = len(assembly[0])
        time1 = [0 for _ in range(N)]
        time2 = [0 for _ in range(N)]
        
        time1[0] = entry[0] + assembly[0][0]
        time2[0] = entry[1] + assembly[1][0]
        print("Step\tT1\tT2")
        for i in range(1, N):
            time1[i] = min(time1[i-1] + assembly[0][i],
                        time2[i-1] + tswitch[1][i] + assembly[0][i])
            time2[i] = min(time2[i-1] + assembly[1][i],
                        time1[i-1] + tswitch[0][i] + assembly[1][i] )
            print(f"{i}\t{time1[i - 1]}\t{time2[i - 1]}")
    
        print(f"{i}\t{time1[N - 1] + exit[0]}\t{time2[N - 1] + exit[1]}")
        return min(time1[N - 1] + exit[0],
                time2[N - 1] + exit[1])

fin = Solution()
assembly = [[7, 9, 3, 4, 8, 4], 
        [8, 5, 6, 4, 5, 7]]
entry = [2, 4]
exit = [3, 2]
tswitch = [[0, 2, 3, 1, 3, 4],
        [0, 2, 1, 2, 2, 1]]

capacity = 10
val = [7, 2, 1, 6, 12]
weight = [3, 1, 2, 4, 6]

print(f"KnapSack value: {fin.knapSack(W=capacity, wt=weight, val=val)}")
print(f"Car assembly minimum time: {fin.carAssembly(assembly=assembly, tswitch=tswitch, entry=entry, exit=exit)}")