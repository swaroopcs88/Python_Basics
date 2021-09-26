def countVowels(x):
    count = 0
    vowels = 'aeiou'
    x = 'bedee'
    for ch in x:
        if ch in vowels:
            count += 1
    return count
y = countVowels('abracadabra')

