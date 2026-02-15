class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        res = []
        on_off = {}
        for bulb in bulbs:
            on_off[bulb] = 1
        for bulb in bulbs:
            on_off[bulb] = 1 - on_off[bulb]
        for k, v in on_off.items():
            if not v:
                res.append(k)
        return sorted(res)