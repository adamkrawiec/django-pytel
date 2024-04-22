from datetime import datetime

from ..constants import DATE_FORMAT

def parse_date(date):
    """Parse time string into datetime object."""
    if date is None:
      return None
    return datetime.strptime(date, DATE_FORMAT)