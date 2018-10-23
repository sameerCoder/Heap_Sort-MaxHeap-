# This is the Heap Sort Program in Python.

class Heap(object):
    HEAP_SIZE=10
    def __init__(self):
        self.heap=[0]*Heap.HEAP_SIZE
        self.currentposition=-1

    def insert(self,item):
        if self.isFull():
            print(" Heap is full.")
            return
        self.currentposition+=1
        self.heap[self.currentposition]=item
        self.fixup(self.currentposition)
    def isFull(self):

        if self.currentposition==Heap.HEAP_SIZE:
            return True
        else:
            return False
    def fixup(self,index):
        parentindex=int((index-1)/2)
        while parentindex>=0and self.heap[parentindex]<self.heap[index]:
            temp=self.heap[index]
            self.heap[index]=self.heap[parentindex]
            self.heap[parentindex]=temp
            parentindex=int((index-1)/2)

        # putting the new inserted node value to the root , making root as greatest as it is maxheap.

    def heapsort(self):
        for i in range(0,self.currentposition+1):
            temp=self.heap[0]
            print("%d"%temp)
            self.heap[0]=self.heap[self.currentposition-i]
            self.heap[self.currentposition-i]=temp
            self.fixdown(0,self.currentposition-i-1)

    def fixdown(self,index,upto):
        while index<=upto:
            leftchild=2*index+1
            rightchild=2*index+2
            if leftchild<upto:
                childToswap=None
                if rightchild>upto:
                    childToswap=leftchild
                else:
                    if self.heap[leftchild]>self.heap[rightchild]:
                        childToswap=leftchild
                    else:
                        childToswap=rightchild
                if self.heap[index]<self.heap[childToswap]:
                    temp=self.heap[index]
                    self.heap[index]=self.heap[childToswap]
                    self.heap[childToswap]=temp

                else:
                    break
                index=childToswap

            else:
                break

if __name__=="__main__":
    heap=Heap()
    heap.insert(10)
    heap.insert(20)
    heap.insert(-20)
    heap.insert(0)
    heap.insert(2)
    heap.heapsort()


