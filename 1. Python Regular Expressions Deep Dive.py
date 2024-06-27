import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Modify the regex pattern to exclude email addresses from 'exclude.com'
exclude_domain = 'exclude.com'
pattern = r'\b[A-Za-z0-9._%+-]+@(?!' + re.escape(exclude_domain) + r')[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

emails = re.findall(pattern, text)
print(emails)