def can_place_cows(stalls, k, min_dist):
    count = 1  # Place the first cow at the first stall
    last_pos = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_pos >= min_dist:
            count += 1
            last_pos = stalls[i]  # Place next cow here

        if count >= k:
            return True  # All cows placed successfully

    return False  # Not enough cows placed


def aggressive_cows(stalls, k):
    stalls.sort()  # Step 1: Sort the stall positions

    low = 1  # Minimum possible distance
    high = stalls[-1] - stalls[0]  # Maximum possible distance
    result = 0  # To store the best (maximum minimum) distance

    while low <= high:
        mid = (low + high) // 2  # Try this as the minimum distance

        if can_place_cows(stalls, k, mid):
            result = mid  # This distance is possible, try for a bigger one
            low = mid + 1
        else:
            high = mid - 1  # Distance too big, try smaller one

    return result
