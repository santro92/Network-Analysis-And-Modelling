def answer(s):
    greater = [pos for pos, char in enumerate(s) if char == '>']
    lesser = [pos for pos, char in enumerate(s) if char == '<']
    if greater[0] > lesser[-1]:
        return 0
    shakes = 0
    for val in greater:
        shakes += 2*sum(i > val for i in lesser)
    return shakes

print answer('<<<>>>>')
