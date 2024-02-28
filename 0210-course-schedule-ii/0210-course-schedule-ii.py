class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        dic=defaultdict(list)
        for course,prereq in prerequisites:
            dic[prereq].append(course)
            indegree[course]+=1
            
        tmp=collections.deque([])
        for i in range(len(indegree)):
            if indegree[i]==0:
                tmp.append(i)
        res=[]
        while tmp:
            tmp_node=tmp.popleft()
            res.append(tmp_node)
            for course in dic[tmp_node]:
                indegree[course]-=1
                if indegree[course]==0:
                    tmp.append(course)
        for i in range(len(indegree)):
            if indegree[i]!=0:
                return []
        return res