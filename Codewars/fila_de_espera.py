def queue_time(customers, n):
    # TODO

    tills = [0 for i in range(n)]
    for customer in customers:
        tills[tills.index(min(tills))] += customer

    return max(tills)


print(queue_time([2, 3, 10], 2))
