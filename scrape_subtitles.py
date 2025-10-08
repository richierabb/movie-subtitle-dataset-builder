from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
from pathlib import Path

def fetch_subtitles(video_id, lang='en'):
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    transcript = YouTubeTranscriptApi.list_transcripts(video_id, languages=[lang])
    df = pd.DataFrame(transcript)
    df['text'] = df['text'].str.replace('\n', ' ')
    df.to_csv(f"data/raw/{video_id}_{lang}.csv", index=False)
    print(f"✅ Saved: {video_id}_{lang}.csv")

if __name__ == "__main__":
    videos = ['n2dVFdqMYGA', 'h5ql62tF014']  # sample IDs
    for vid in videos:
        fetch_subtitles(vid)
