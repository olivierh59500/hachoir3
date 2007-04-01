from hachoir_core.i18n import _
from datetime import date, datetime
import re

NORMALIZE_REGEX = re.compile("[-/.: ]+")
YEAR_REGEX1 = re.compile("^([0-9]{4})$")
DATE_REGEX1 = re.compile("^([0-9]{4})-([01][0-9])-([0-9]{2})$")

# Date regex: YYYY-MM-DD (US format)
DATETIME_REGEX1 = re.compile("^([0-9]{4})-([01][0-9])-([0-9]{2})-([0-9]{2})-([0-9]{2})-([0-9]{2})$")

# Date regex: "MM-DD-YYYY HH:MM:SS" (FR format)
DATETIME_REGEX2 = re.compile("^([01]?[0-9])-([0-9]{2})-([0-9]{4})-([0-9]{2})-([0-9]{2})-([0-9]{2})$")

def parseDatetime(value):
    value = NORMALIZE_REGEX.sub("-", value.strip())
    regs = YEAR_REGEX1.match(value)
    if regs:
        try:
            year = int(regs.group(1))
            return (date(year, 1, 1), unicode(year))
        except ValueError:
            pass
    regs = DATE_REGEX1.match(value)
    if regs:
        try:
            year = int(regs.group(1))
            month = int(regs.group(2))
            day = int(regs.group(3))
            return date(year, month, day)
        except ValueError:
            pass
    regs = DATETIME_REGEX1.match(value)
    if regs:
        try:
            year = int(regs.group(1))
            month = int(regs.group(2))
            day = int(regs.group(3))
            hour = int(regs.group(4))
            min = int(regs.group(5))
            sec = int(regs.group(6))
            return datetime(year, month, day, hour, min, sec)
        except ValueError:
            pass
    regs = DATETIME_REGEX2.match(value)
    if regs:
        try:
            month = int(regs.group(1))
            day = int(regs.group(2))
            year = int(regs.group(3))
            hour = int(regs.group(4))
            min = int(regs.group(5))
            sec = int(regs.group(6))
            return datetime(year, month, day, hour, min, sec)
        except ValueError:
            pass

def setDatetime(key, value):
    if isinstance(value, (str, unicode)):
        return parseDatetime(value)
    elif isinstance(value, (date, datetime)):
        return value
    return None

NB_CHANNEL_NAME = {1: _("mono"), 2: _("stereo")}

def humanAudioChannel(value):
    return NB_CHANNEL_NAME.get(value, unicode(value))

def humanFrameRate(value):
    if isinstance(value, (int, long, float)):
        return _("%.1f fps") % value
    else:
        return value
