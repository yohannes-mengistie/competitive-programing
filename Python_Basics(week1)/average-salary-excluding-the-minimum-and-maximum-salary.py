class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)-1
        ans = sum(salary[1:n])
        ava = ans/(n-1)
        return ava