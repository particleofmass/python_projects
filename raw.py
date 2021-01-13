def solution(args):
    output, mini = [], []
    for i in args:
        val, p = 1, args.index(i)+1
        while p < len(args):
            if args[p] == i+val:
                p+=1
                val+=1
                mini.append(args[p])
            elif args[p] != i + val:
                output.append(mini)
                break
    return output

print(solution([1, 2, 3, 7, 8, 9]))
