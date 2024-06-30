def fractionalKnapsack(wt,profit,c):
    dict={profit[i]/wt[i] : [profit[i],wt[i]] for i in range(len(wt))}
    tp=0
    rate=sorted(dict)[::-1]
    for i in rate:
        #Start with the largest possible Rate and include in knapsack
        profit,wt = dict.get(i)
        if wt<=c :
            tp = tp + profit
            c = c-wt
        else :
            # when the item wt is more than the capacity, include fraction c * rate
            # Reduce c=0
            tp = tp + i*c
            c=0
        # When the Knapsack is full, return the Total profit
        if c==0: return tp
    
    
wt=[3,4,2]
profit=[5,6,4]
c=6
print(fractionalKnapsack(wt,profit,c))
