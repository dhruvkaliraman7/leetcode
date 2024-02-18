class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=collections.defaultdict(list)
        indegree=[0 for i in range(numCourses)]
        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course]+=1
        q=collections.deque()
        for i,n in enumerate(indegree):
            if n==0:
                q.append(i)
        while q:
            curr=q.popleft()
            for course in graph[curr]:
                indegree[course]-=1
                if indegree[course]==0:
                    q.append(course)
                    
        for n in indegree:
            if n>0:
                return False
        return True