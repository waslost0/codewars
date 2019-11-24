def find_score(word):
    return [sum([ord(i)-96 for i in word])]

def high(x):
    x = x.split()
    list = []
    for word in x:
        scores = find_score(word)
        list.append(scores)
        
    return x[list.index(max(list))]