

class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency   


class MinHeap:
    def __init__(self):
        self.data = []  
    def print_heap(self):
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        return self.data[0] if self.data else None

    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop() 
        self.heapify_down(0)
        return root

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest == index:
                break  

            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest



p1 = Patient("Genesis", 2)
print(p1.name)       
print(p1.urgency)    

heap = MinHeap()
heap.insert(Patient("Michael", 3))
heap.insert(Patient("Marc", 1))
heap.insert(Patient("Evan", 5))
heap.print_heap()

next_up = heap.peek()
print(next_up.name, next_up.urgency)

served = heap.remove_min()
print(served.name)
heap.print_heap()
