class Solution:
    def reorganizeString(self, s: str) -> str:
        dic=defaultdict(int)
        for st in s:
            # print(st)
            dic[st]+=1
        arr=[]
        for key in dic:
            arr.append([-dic[key],key])
        # print(arr)
        heapq.heapify(arr)
        res=''
        while arr and len(arr)>1:
            out1=heapq.heappop(arr)
            out2=heapq.heappop(arr)
            #print(out[1])
            if res!='' and res[-1]==out1[1]:
                #out=out2
                res=res+out2[1]
                if out2[0]==-1:
                    heapq.heappush(arr,[out1[0],out1[1]])
                    continue
                else:
                    heapq.heappush(arr,[out2[0]+1,out2[1]])
                    heapq.heappush(arr,[out1[0],out1[1]])
            else:
                res=res+out1[1]
                if out1[0]==-1:
                    heapq.heappush(arr,[out2[0],out2[1]])
                    continue
                else:
                    heapq.heappush(arr,[out1[0]+1,out1[1]])
                    heapq.heappush(arr,[out2[0],out2[1]])
            #print(out)
            # print(res)
            # print(arr)
            
        if arr:
            if arr[0][0]<-1:
                return ''
            else:
                if res=='':
                    return arr[0][1]
                elif arr[0][1]==res[-1]:
                    return ''
                else:
                    return res+arr[0][1]
            
        