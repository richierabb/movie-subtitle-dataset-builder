import pandas as pd
import glob
import os
import re

# Function to clean subtitle text
def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)
    # Remove timestamps (hh:mm:ss or mm:ss)
    text = re.sub(r"\d{1,2}:\d{2}(:\d{2})?", "", text)
    # Remove extra whitespace and newlines
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Function to clean all CSV files in data/raw/
def clean_all():
    os.makedirs("data/cleaned", exist_ok=True)
    
    raw_files = glob.glob("data/raw/*.csv")
    if not raw_files:
        print("No files found in data/raw/. Run scrape_subtitles.py first.")
        return
    
    for file in raw_files:
        df = pd.read_csv(file)
        # Clean the text column
        df['text'] = df['text'].apply(clean_text)
        # Save to data/cleaned/
        output_file = file.replace("raw", "cleaned")
        df.to_csv(output_file, index=False)
        print(f"✅ Cleaned: {output_file}")

# Run the cleaning process
if __name__ == "__main__":
    clean_all()
