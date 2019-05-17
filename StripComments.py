def solution(string, markers):
    lines = string.split('\n')
    output = lines[:]
    j = 0
    for line in lines:
        for sym in markers:
            try:
                i = output[j].index(sym)
                if i == 0:
                    output[j] = ''
                    break
                output[j] = line[:i - 1].rstrip()
            except ValueError:
                continue
        j += 1
    return '\n'.join(output)
