import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("CHIA_ROOT", "~/.chia/ips-2022-08-31"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("CHIA_KEYS_ROOT", "~/.chia_keys"))).resolve()
