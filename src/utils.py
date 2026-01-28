import pandas as pd
from datetime import datetime
import os

def add_timestamp(records):
    """Add a timestamp to each record"""
    timestamp = datetime.utcnow().isoformat()
    for r in records:
        r["scraped_at"] = timestamp
    return records

def save_csv(records, path):
    """
    Save records to CSV file
    Automatically creates directory if it doesn't exist
    """
    # Create directory if it doesn't exist
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
    
    df = pd.DataFrame(records)
    df.to_csv(path, index=False)