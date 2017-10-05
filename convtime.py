#!/usr/bin/env python
'Module to convert configuration time values'

import sys
from datetime import timedelta
import logging as log

def todelta(time_str):
    'Convert time "nn[.d][smdhw]" string to timedelta'

    # Ensure passed value is string
    timestr = str(time_str).lower()

    # Default is secs if no extension
    if not timestr[-1].isalpha():
        timestr += 's'

    nums = timestr[:-1]

    # Can accept float or int
    if nums.replace('.', '', 1).isdigit():
        num = float(nums) if '.' in nums else int(nums)

        if timestr.endswith('s'):
            return timedelta(seconds=num)
        elif timestr.endswith('m'):
            return timedelta(minutes=num)
        elif timestr.endswith('h'):
            return timedelta(hours=num)
        elif timestr.endswith('d'):
            return timedelta(days=num)
        elif timestr.endswith('w'):
            return timedelta(weeks=num)

    log.error('Do not understand "%s" time format', time_str)
    sys.exit(1)

def tosec(time_str):
    'Convert time "nn[.d][smdhw]" string to secs'
    return todelta(time_str).total_seconds()
