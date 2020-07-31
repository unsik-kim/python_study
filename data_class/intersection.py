def intersection(inA, inB):
    result = set()

    if type(inA) == set:
        if type(inB) == set:
            for i in inA:
                for j in inB:
                    if i == j:
                        result.add(i)
            return result

    return 0


print(intersection({1, 2, 3, 4, 5}, {3, 4, 5}))

