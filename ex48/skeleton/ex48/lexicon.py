lexi = {
    'north': 'direction',
    'south': 'direction',
    'west': 'direction',
    'east': 'direction',
    'up': 'direction',
    'down': 'direction',
    'left': 'direction',
    'right': 'direction',
    'back': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'stop': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'from': 'stop',
    'at': 'stop',
    'the': 'stop',
    'door': 'noun',
    'bear': 'noun',
    'princess': 'noun',
    'cabinet': 'noun',
    }


def scan(word):
    out = []
    words = word.split()
    for i in words:
        try:
            out.append(('number', int(i)))

        except ValueError:
            if i in lexi.keys():
                out.append((lexi.get(i), i))

            else:
                out.append(('error', i))

    return out
