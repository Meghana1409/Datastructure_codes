class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printll(self):
        t=self.head
        a=[]
        while(t):
            a.append(t.data)
            t=t.next
        print("-->".join(map(str,a)))

    #insertion operations....

    def insertatstartlist(self,data):
        n=Node(data)
        n.next=self.head
        self.head=n
    
    def insertatpos(self,data,pos):
        n=Node(data)
        c=1
        p=self.head
        while(p.next is not None):
            if(c==pos-1):
                n.next=p.next
                p.next=n
                break
            p=p.next
            c+=1
    
    def insertafterpos(self,data,pos):
        n=Node(data)
        c=1
        p=self.head
        while(p.next is not None):
            if(c==pos):
                n.next=p.next
                p.next=n
                break
                
            p=p.next
            c+=1
    

    def insertbeforepos(self,data,pos):
        n=Node(data)
        c=1
        p=self.head
        while(p.next is not None):
            if(c==pos-1):
                n.next=p.next
                p.next=n
                break
                
            p=p.next
            c+=1

    def insertatend(self,data):
        n=Node(data)
        p=self.head
        while(p.next is not None):
            p=p.next
        p.next=n
        n.next=None

    # Deleting ....
    def deleteatstart(self):
        if(self.head==None):
            return
        else:
            self.head=self.head.next
        
    def deleteatpos(self,pos):
        p=self.head
        c=1
        while(p.next is not None):
            if(c==pos-1):
                p.next=p.next.next
            p=p.next
            c+=1
    
    def deleteatend(self):
        p=self.head
        while(p.next.next is not None):
            p=p.next
        p.next=None

    def deletList(self):
        self.head=None
        print("Your list became Empty")
        

    def searchele(self,key):
        if(self.head==None):
            return
        else:
            p=self.head
            c=1
            while(p is not None):
                if(p.data==key):
                    print(f"Element({key}) found at position : {c}")
                    return
                p=p.next
                c+=1
            print("Not found")


        



    
ll=LinkedList()
n1=Node(1)
n2=Node(2)
ll.head=n1
ll.head.next=n2
print("Initial List...")
ll.printll()
print("insert at given position(2)...")
ll.insertatpos(4,2)
ll.printll() 
print("insert after given position(2)...")
ll.insertafterpos(5,2)
ll.printll()
print("insert before given position(3)...") 
ll.insertbeforepos(6,3)
ll.printll() 
print("Insert element at start of linked List...")
ll.insertatstartlist(10)
ll.printll() 
print("Insert element at End of linked List...")
ll.insertatend(10)
ll.printll() 
print("delete element at start of linked List...")
ll.deleteatstart()
ll.printll()
print("delete element at given position of linked List...")
ll.deleteatpos(2)
ll.printll() 
print("delete element at end of linked List...")
ll.deleteatend()
ll.printll()
print("searching element in list...")
ll.searchele(5)
print("searching element in list if not found...")
ll.searchele(10)
print("Delete whole list")
ll.deletList()
ll.printll()