class LinkedNode:
    def __init__(self,val,prev=None,next=None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = LinkedNode(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = LinkedNode(url,self.cur)
        self.cur = self.cur.next
        # print(self.prev.val , self.cur.val)

    def back(self, steps: int) -> str:

        while self.cur.prev and steps > 0 :
            self.cur = self.cur.prev
            
            steps -=1

        return self.cur.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next:
            self.cur = self.cur.next
            steps -=1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)