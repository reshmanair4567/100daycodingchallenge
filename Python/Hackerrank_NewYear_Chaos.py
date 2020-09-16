def NewYearChaos(queue):
    lastIndex = len(queue) - 1
    swaps = 0
    swaped = False
    
    # check if the queue is too chaotic
    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            return "Too chaotic"
    # bubble sorting to find the answer
    for i in xrange(0, lastIndex):
        for j in xrange(0, lastIndex):
            comps += 1
            if queue[j] > queue[j+1]:
                temp = queue[j]
                queue[j] = queue[j+1]
                queue[j+1] = temp
                swaps += 1
                swaped = True
        
        if swaped:
            swaped = False
        else:
            break
    return swaps