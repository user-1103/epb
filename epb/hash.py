'''
The module responsible for reproducible and immutability.
'''

from typing import List, Tuple, Union
from json import dump, load
from checksumdir import dirhash
# What seals are currently being concidered
SEALS = list()

def mk_seal(p: str, do_record: bool =True) -> Tuple[str, str]:
    """
    'Seals' a path and returns the corasponding hash.

    :param p: the path to seal, should be absoult
    :param do_record: Should the seal be saved
    :retrun: a tuple of the path and the hash
    """
    hash = dirhash(p, 'md5')
    tmp = (p, hash)
    if (do_record):
        SEALS.append(tmp)
    return tmp

def check(seal: Union[Tuple[str, str], List[str]]) -> bool:
    """
    Checks the validity of a seal.

    :pram seal: The seal outputed by seal
    :return: If the seal is valid
    """
    tmp = mk_seal(seal[0], do_record=False)
    if (tmp[1] == seal[1]):
        return True
    else:
        return False

def save_seals() -> None:
    """
    Save all seals.
    """
    with open("seals.json", 'w') as f:
        dump(SEALS, f)

def load_seals() -> None:
    """
    Load all seals.
    """
    with open("seals.json", 'r') as f:
        tmp = load(f)
        SEALS.extend(tmp)
