import re

def clean_text(text):
    # Remove null characters and repeated watermark strings
    cleaned = text.encode("utf-8", "ignore").decode("utf-8", "ignore")  # Remove non-UTF-8
    cleaned = re.sub(r'[\x00-\x1F\x7F]', '', cleaned)  # Remove control characters
    cleaned = re.sub(r'(Download from.*?fine\w*book.*?com)', '', cleaned, flags=re.IGNORECASE | re.DOTALL)  # Remove watermark ads
    return cleaned
