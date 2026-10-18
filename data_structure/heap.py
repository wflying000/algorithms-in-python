
class MinHeap:
    def __init__(self):
        self.nums = []
        self.size = 0

    def __len__(self):
        return self.size
    
    def push(self, num):
        if self.size < len(self.nums):
            self.nums[self.size] = num
        else:
            self.nums.append(num)
        self.size += 1
        self.up(self.size - 1)

    def pop(self):
        res = self.nums[0]
        self.nums[0] = self.nums[self.size - 1]
        self.size -= 1
        self.down(0)
        return res 

    def peek(self):
        return self.nums[0]


    def up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.nums[idx] < self.nums[parent]:
                self.nums[idx], self.nums[parent] = self.nums[parent], self.nums[idx]
                idx = parent 
            else:
                break 

    def down(self, idx):
        while 2 * idx + 1 < self.size:
            j = 2 * idx + 1
            if j + 1 < self.size and self.nums[j + 1] < self.nums[j]:
                j += 1
            if self.nums[idx] > self.nums[j]:
                self.nums[idx], self.nums[j] = self.nums[j], self.nums[idx]
                idx = j 
            else:
                break 
         
        
            