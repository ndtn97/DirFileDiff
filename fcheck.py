from hashlib import md5
from pathlib import Path
import sys


def dir_hash(dir, ext):
    hasher = md5()
    pathes = sorted(list(Path(dir).rglob('*.{}'.format(ext))))
    assert len(pathes) > 0
    for path in pathes:
        with open(path, mode='rb') as f:
            data = f.read()
            hasher.update(data)

    return hasher.hexdigest()


def compare_hash(dir, ext, orig_hash):
    target_hash = dir_hash(dir, ext)
    assert target_hash == orig_hash
    return


if __name__=='__main__':
    if len(sys.argv) == 3:
        dir, ext = sys.argv[1], sys.argv[2]
        print(dir_hash(dir, ext))
    else:
        dir, ext, orig_hash = sys.argv[1], sys.argv[2], sys.argv[3]
        compare_hash(dir, ext, orig_hash)
