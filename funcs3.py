def count(x, y='aeiou'):
    count = 0
    for ch in x:
        if ch in y:
            count += 1
    return count
y1 = count('wow this is nuts')
y2 = count('wow this is huch', 'abc')
