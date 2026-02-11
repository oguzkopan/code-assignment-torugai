# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

def count_valid_emails(emails):
    """
    Count the number of valid email addresses in the input list.
    
    A valid email must contain exactly one '@' symbol with text before and after it.
    
    Args:
        emails: List of email strings (may contain None or non-string values)
        
    Returns:
        int: Count of valid email addresses
    """
    if not emails:
        return 0
    
    count = 0
    
    for email in emails:
        if email and isinstance(email, str) and "@" in email:
            # Check for exactly one @ and non-empty local/domain parts
            if email.count("@") == 1:
                local, domain = email.split("@")
                if local and domain:
                    count += 1
    
    return count
