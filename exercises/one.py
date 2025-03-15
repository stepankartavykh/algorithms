def convert(numbers: list[int]) -> str:
    if len(numbers) == 0:
        return ''
    numbers.sort()
    
    pairs = []
    current = numbers[0]
    start = numbers[0]
    
    for i in range(1, len(numbers)):
        if numbers[i] == current + 1:
            current = numbers[i]
            continue
        else:
            if start == current:
                pairs.append(str(current))
            else:
                pairs.append(f"{start}-{current}")
            start = current = numbers[i]
    
    if start == current:
        pairs.append(str(start))
    else:
        pairs.append(f"{start}-{current}")
    
    return ','.join(pairs)


if __name__ == '__main__':
    print(convert([1, 4, 5, 2, 3, 9, 8, 11, 0]))
    print(convert([1, 4, 3, 2]))
    print(convert([1, 4]))
