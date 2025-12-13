class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sweeping_line = []
        for start, end in intervals:
            sweeping_line.append((start, 1))
            sweeping_line.append((end, 0))
        room_tally = 0
        max_rooms = 0
        sweeping_line.sort(key = lambda x: (x[0], x[1]))
        for time, type_ in sweeping_line:
            if type_ == 1:
                room_tally += 1
                max_rooms = max(max_rooms, room_tally)
            else:
                room_tally -= 1
        return max_rooms

        
        
        