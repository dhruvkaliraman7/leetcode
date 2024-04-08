class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zeroStu , zeroSand, oneStu, oneSand = 0,0,0,0
        for i in range(len(students)):
            if students[i] == 0:
                zeroStu += 1
            else:
                oneStu += 1
            if sandwiches[i] == 0:
                zeroSand += 1
            else:
                oneSand += 1
        flag = 0
        if oneSand > oneStu:
            flag = 1
        if zeroSand > zeroStu:
            flag = 2
        if flag == 0:
            return 0
        if flag == 1:
            for i in range(len(sandwiches)):
                if sandwiches[i] == 1 and oneStu>0:
                    oneStu -= 1
                elif sandwiches[i] == 1 and oneStu==0:
                    return len(students) - i
        else:
            for i in range(len(sandwiches)):
                if sandwiches[i] == 0 and zeroStu>0:
                    zeroStu -= 1
                elif sandwiches[i] == 0 and zeroStu==0:
                    return len(students) - i
            
                
                    