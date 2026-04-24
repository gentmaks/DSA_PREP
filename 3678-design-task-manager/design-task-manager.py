class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.counter = 1
        self.state = {} 
        self.heap = []
        for uid, tid, prio in tasks:
            self.state[tid] = [uid, prio]
            self.heap.append([-prio, -tid, -self.counter, uid])
            self.counter += 1
        heapq.heapify(self.heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.state[taskId] = [userId, priority]
        heapq.heappush(self.heap, [-priority, -taskId, -self.counter, userId, ])
        self.counter += 1

    def edit(self, taskId: int, newPriority: int) -> None:
        uid = self.state[taskId][0]
        self.state[taskId] = [uid, newPriority]
        heapq.heappush(self.heap, [-newPriority, -taskId, -self.counter, uid])
        self.counter += 1
        

    def rmv(self, taskId: int) -> None:
        self.state.pop(taskId)

    def execTop(self) -> int:
        while self.heap:
            prio, tid, _, uid = heapq.heappop(self.heap)
            if -tid not in self.state:
                continue
            cmp_prio = self.state[-tid][1]
            if (-prio) == cmp_prio:
                self.state.pop(-tid)
                return uid
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()