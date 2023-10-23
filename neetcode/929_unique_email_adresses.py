import re
from typing import List


def num_unique_emails(emails: List[str]) -> int:
    unique_emails = set()
    for mail in emails:
        local_name, domain = re.split('@', mail)
        if '+' in local_name:
            local_name = local_name[:local_name.find('+')]
        local_name = ''.join(local_name.split('.'))
        processed_email = ''.join([local_name, '@', domain])
        if processed_email not in unique_emails:
            unique_emails.add(processed_email)
    return len(unique_emails)