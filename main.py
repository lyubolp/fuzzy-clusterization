import pandas as pd

from typing import List


def parse_headers() -> List[str]:
    with open('data/spambase.names') as fp:
        result = [line.split(':')[0] for line in fp.readlines() if "|" not in line and len(line) > 1]
        return result


if __name__ == '__main__':
    headers = parse_headers() + ['is_spam']
    data = pd.read_csv('data/spambase.data', names=headers)
    print(data)

