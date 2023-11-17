best_value = {}

def change_making_recursive(coins: list[int], total: int) -> list[int]:
    """Returns the best possible total value for the provided instance of the Change-Making Problem.
    Arguments:
    coins   --   the list of the values of the items
    total   --   the target total value
    """

    # Base Case
    if total == 0:return []

    # Return cached results
    if total in best_value:return best_value[total]

    # Iterate over all coins
    best = None
    for coin in coins:

        # Accept coins that aren't over the total
        if coin <= total:
            current = change_making_recursive(coins, total - coin)
        
            # Check if current is longer or equal to best (Equal check means the final result will be sorted)
            if current != None:
                current = current + [coin]
                if best is None:best = current
                elif len(current) <= len(best):best = current
            
            del current

    best_value[total] = best
    return best

if __name__ == "__main__":
    total = 173
    coins = [1, 5, 10, 25, 50, 100, 500, 1000, 2000, 5000, 10000]
    print(sorted(change_making_recursive(coins, total), reverse = True))