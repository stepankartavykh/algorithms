

def character_replacement(s: str, k: int) -> int:
    """
    s = 'AAEEAAABBBAACDDDED'
    distribution_letters = {
        'A': {
            0: 2,
            4: 3,
            10: 2,
        },
        'E': {
            2: 2,
            16: 1,
        }
        'B': {
            7: 3,
        }
        'C': {
            12: 1,
        }
        'D': {
            13: 3,
            17: 1
        }
    }
    """
    """
    s = 'AAEEAAABBBAACDDDED'
    
    distr = {
        (0, A): 2,
        (2, E): 2,
        (4, A): 3,
        (7, B): 3,
        (10, A): 2,
        (12, C): 1,
        (13, D): 3,
        (16, E): 1,
        (17, D): 1,
    }
    """

    distr = {}
    string_alphabet = set()
    repeating_letters = set()
    counter = 0
    for position in range(len(s)):
        pass
