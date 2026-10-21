class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        buy_backlog = []
        sell_backlog = []
        for price, amount, _type in orders:
            type_str = "buy" if not _type else "sell"
            # batch of buy orders
            if not _type:
                while amount > 0:
                    if not sell_backlog:
                        heapq.heappush(buy_backlog, (-price, amount))
                        break
                    other_p, other_a = heapq.heappop(sell_backlog) 
                    if other_p <= price:
                        new_amount = amount - other_a
                        other_a -= amount
                        amount = new_amount
                        if other_a > 0:
                            heapq.heappush(sell_backlog, (other_p, other_a))
                    else:
                        heapq.heappush(buy_backlog, (-price, amount))
                        heapq.heappush(sell_backlog, (other_p, other_a))
                        break

            else:
                while amount > 0:
                    if not buy_backlog:
                        heapq.heappush(sell_backlog, (price, amount))
                        break
                    other_p, other_a = heapq.heappop(buy_backlog) 
                    if (other_p * -1) >= price:
                        new_amount = amount - other_a
                        other_a -= amount
                        amount = new_amount
                        if other_a > 0:
                            heapq.heappush(buy_backlog, (other_p, other_a))
                    else:
                        heapq.heappush(sell_backlog, (price, amount))
                        heapq.heappush(buy_backlog, (other_p, other_a))
                        break
        total_backlog = 0
        for _, amount in buy_backlog:
            total_backlog += amount
        for _, amount in sell_backlog:
            total_backlog += amount
        return total_backlog % MOD