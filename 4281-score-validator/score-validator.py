class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        non_num = ["W", "WD", "NB"]
        score = 0
        counter = 0
        for event in events:
            if event not in non_num:
                score += int(event)
            else:
                if event == "W":
                    counter += 1
                else:
                    score += 1

            if counter == 10:
                break
        return [score, counter]
