def is_increasing_rec(sequence):
    assert len(sequence) >= 2

    is_bigger = sequence[1] - sequence[0] >= 0

    if len(sequence) == 2 or not is_bigger:
        return is_bigger
    
    return is_increasing_rec(sequence[1:])
