import googleapiclient.discovery
from googleapiclient.errors import HttpError

def get_channel_videos(api_key, channel_id):
  youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

  request = youtube.search().list(
      part="snippet",
      channelId=channel_id,
      order="date",
      maxResults=50
  )

  response = request.execute()

  video_ids = []
  for item in response['items']:
      video_id = item['id']['videoId']
      video_ids.append(video_id)

  return video_ids




# Replace with your API key and channel ID
api_key = "AIzaSyBnqG4_Vo7r8DgrwkAnoi1SntGNAarPYgw"
channel_id = "eeonv3"

video_ids = get_channel_videos(api_key, channel_id)

# Construct video URLs
video_urls = [f"https://www.youtube.com/watch?v={video_id}" for video_id in video_ids]

print(video_urls)

# All Videos
#######################
# To get all videos, 
# implement pagination 
# and 
# handle potential rate limits.