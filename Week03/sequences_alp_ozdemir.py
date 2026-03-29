def remove_duplicates(seq):
    res = set(seq)
    return res


def list_counts(seq):
    counts = {}
    for i in seq:
        counts[i] = counts.get(i,0) + 1
    return counts


def reverse_dict(d):    
    return reversed(d)
