class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        n = len(people)
        people.sort(key = lambda x: -x)
        people = collections.deque(people)
        boats = 0
        while people:
            if len(people) == 1:
                boats += 1
                return boats
            if people[0] + people[-1] <= limit:
                people.popleft()
                people.pop() 
            else:
                people.popleft()
            boats += 1
        return boats