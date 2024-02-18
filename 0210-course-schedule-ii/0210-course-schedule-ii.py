class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=defaultdict(int)
        neighs=defaultdict(list)
        for course,prereq in prerequisites:
            indegree[course]+=1
            indegree[prereq]+=0
            neighs[prereq].append(course)
        
        q=collections.deque()
        res=[]
        for i in range(numCourses):
            if i not in indegree:
                res.append(i)
        
        for key in indegree:
            if indegree[key]==0:
                q.append(key)
                res.append(key)   
        # print(q)
        while q:
            tmp=q.popleft()
            for neigh in neighs[tmp]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
                    res.append(neigh)
        # print(indegree)
        # print(q)
        for key in indegree:
            if indegree[key]>0:
                return []
        return res