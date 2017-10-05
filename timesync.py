#!/usr/bin/python
# Requires python 3.5+
'Module to report whether host is time synced'
# Mark Blakeney, May 2017.

import time
from datetime import date
from pathlib import Path

_UPTIME = Path('/proc/uptime')
_SYSTIME = Path('/var/lib/systemd/clock')
_TIMEBOOT = time.time() - float(_UPTIME.read_text().split()[0])

if _SYSTIME.exists() and _UPTIME.exists():
    _SYSTIME = _SYSTIME.resolve()
else:
    _SYSTIME = None

def _crudeInSync():
    'Do a crude check if not running systemd'
    return date.today().year > 2000

def inSyncAtBoot():
    'Return whether we have time synced since boot or not'
    return _SYSTIME.stat().st_mtime >= _TIMEBOOT \
            if _SYSTIME else _crudeInSync()

def inSync(timeout):
    'Returns True if host is currently synced to a time server'
    return ((time.time() - _SYSTIME.stat().st_mtime) < timeout) \
            if _SYSTIME else _crudeInSync()

if __name__ == '__main__':
    print(inSyncAtBoot())
