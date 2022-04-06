def MathChallenge(num: int) -> str:
    if num in [1, 7]:
        num = "true"
        return num

    _num = str(num)
    if len(_num) < 2:
        num = "false"
        return num

    sqr = [int(n) ** 2 for n in _num]

    if sum(sqr) == 1:
        num = "true"
        return num
    else:
        return MathChallenge(sum(sqr))


# keep this function call here
print(MathChallenge(input()))
