class Node:
    def __init__(self,value = None,next=None):
        self.value = value
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0
       

    def get(self, index: int) -> int:
        if index < 0 or index>=self.size:
            return -1

        cur = self.head
        while index >= 0:
            cur = cur.next
            index -=1

        return cur.value


        

               

        

    def addAtHead(self, val: int) -> None:
        prev,curr = self.head,self.head.next
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size +=1
        

    def addAtTail(self, val: int) -> None:
        prev = self.head
        cur = self.head.next

        while cur:
            prev = cur
            cur = cur.next

        new_node = Node(val)
        prev.next = new_node
        self.size +=1


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        prev = self.head
        cur = self.head

        while index >= 0:
            prev = cur
            cur = cur.next
            index -=1
        new_node = Node(val)
        prev.next = new_node
        new_node.next = cur
        self.size +=1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return

        prev,cur = self.head,self.head

        while index >= 0:
            prev = cur
            cur = cur.next
            index -=1

        prev.next = cur.next
        self.size -=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)