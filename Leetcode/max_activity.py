def sortbyendtime(activity):
    """
    Sorts a list of activities based on their end times.
    """
    n = len(activity)
    # return sorted(activity, key=lambda x: x[1])
    for i in range(n-1):
        for j in range(i+1, n):
            if activity[i][1] > activity[j][1]:
                activity[i], activity[j] = activity[j], activity[i]
    return activity

def max_activity(activity):
    """
    Finds the maximum number of activities that can be performed
    by a single person, given a list of activities.
    """
    n = len(activity)
    sorted_activity = sortbyendtime(activity)

    count, last_endtime = 0, 0
    for start, end in sorted_activity:
        if start >= last_endtime:
            count += 1
            last_endtime = end
    return count

activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
print(max_activity(activity))

# Time complexity: O(nlogn)
# Space complexity: O(1)