import heapq


def isNStraightHand(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size != 0:
        return False
    hand.sort()
    groups = {i: [] for i in range(len(hand) // group_size)}
    for card in hand:
        for group_i in groups:
            if card not in groups[group_i]:
                if len(groups[group_i]) == group_size:
                    continue
                if len(groups[group_i]) >= 1 and card - max(groups.get(group_i)) > 1:
                    return False
                groups[group_i].append(card)
                break
        else:
            return False
    return True


def isNStraightHand_better(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size:
        return False

    card_to_count = {}
    for card in hand:
        card_to_count[card] = 1 + card_to_count.get(card, 0)

    unique_cards = list(card_to_count.keys())
    heapq.heapify(unique_cards)

    while unique_cards:
        min_card_for_group = unique_cards[0]

        for card in range(min_card_for_group, min_card_for_group + group_size):
            if card not in card_to_count:
                return False
            card_to_count[card] -= 1
            if card_to_count[card] == 0:
                if card != unique_cards[0]:
                    return False
                heapq.heappop(unique_cards)
    return True


if __name__ == '__main__':
    print(isNStraightHand_better(hand=[1, 5], group_size=2))
    print(isNStraightHand_better(hand=[1, 2, 3, 4, 5, 6], group_size=2))
    print(isNStraightHand_better(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], group_size=3))
    print(isNStraightHand_better(
        [9, 13, 15, 23, 22, 25, 4, 4, 29, 15, 8, 23, 12, 19, 24, 17, 18, 11, 22, 24, 17, 17, 10, 23, 21, 18, 14, 18, 7,
         6, 3, 6, 19, 11, 16, 11, 12, 13, 8, 26, 17, 20, 13, 19, 22, 21, 27, 9, 20, 15, 20, 27, 8, 13, 25, 23, 22, 15,
         9, 14, 20, 10, 6, 5, 14, 12, 7, 16, 21, 18, 21, 24, 23, 10, 21, 16, 18, 16, 18, 5, 20, 19, 20, 10, 14, 26, 2,
         9, 19, 12, 28, 17, 5, 7, 25, 22, 16, 17, 21, 11],
        10
    ))
    print(isNStraightHand_better(hand=[1, 2, 3, 10, 2, 3, 4, 7, 8], group_size=3))
