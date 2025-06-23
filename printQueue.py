class PrintQueue:
      def __init__(self, capacity=10, aging_interval=5, expiry_time=30):
         self.queue = [None] * capacity
         self.capacity = capacity
         self.front = 0
         self.rear = 0
         self.size = 0
         self.aging_interval = aging_interval
         self.expiry_time = expiry_time
         
         
         
          
        
        