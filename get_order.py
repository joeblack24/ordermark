def get_times(times, directions):
    # People entering, exiting and results, setting default status to exiting
    # because exiting people have priority in clash.
    # Also getting initial time
    entering = []
    exiting = []
    order = []
    status = 1
    time = times[0]
    # Split to people entering and exiting
    for idx, initial_time in enumerate(times):
        if directions[idx] == 1:
            exiting.append((idx, initial_time))
        else:
            entering.append((idx, initial_time))
    prev = 0

    for original_time in times:
        # setting status back to exit if it's been more than a second
        # since gate was used
        status = 1 if original_time > time + 1 else status

        # Setting time to account for time lapses
        time = original_time if original_time > time + 1 else time

        # Getting first potential person exiting or entering based on time
        enter = entering[0] if entering and (
                    original_time in dict(entering).values() or entering[0][1] <= time) else None
        exit = exiting[0] if exiting and (original_time in dict(exiting).values() or exiting[0][1] <= time) else None

        # If people are trying to enter and priority is based on gate status
        # gate status is defaulted to exit above
        if (enter and exit and status == 1) or (exit and not enter):
            # Using original index to place time in results list
            order.insert(exit[0], time)
            status = 1
            # initially was thinking remove or list index, but I think pop is
            # more efficient complexity wise
            exiting.pop(0)
            time += 1
        else:
            order.insert(enter[0], time)
            status = 0
            entering.pop(0)
            time += 1

    return order


order = get_times([0,0,1,5], [0,1,1,0])
print(order)
# [2,0,1,5]
