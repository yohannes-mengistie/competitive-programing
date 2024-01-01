class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks = sorted(tasks,reverse=True)
        processorTime.sort()

        j,res = 0 , []
        for i in range(len(processorTime)):
            res.append(processorTime[i]+tasks[j])
            j +=4

        return max(res)