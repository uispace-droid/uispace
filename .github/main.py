import os
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

BLOG_ID = os.environ.get('BLOG_ID')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REFRESH_TOKEN = os.environ.get('REFRESH_TOKEN')

def main():
    creds = Credentials(
        None,
        refresh_token=REFRESH_TOKEN,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        token_uri="https://oauth2.googleapis.com/token"
    )
    service = build('blogger', 'v3', credentials=creds)

    response = requests.get('https://gamemonetize.com/feed.php?format=json')
    games = response.json()

    print(f"تم العثور على {len(games)} لعبة. جارٍ النشر بدون فلترة...")

    for game in games:
        title = game.get('title')
        description = game.get('description', '')
        game_url = game.get('url', '')

        html_content = f'''
        <div class="game-container">
            <p>{description}</p>
            <div style="text-align:center; margin:20px 0;">
                <iframe src="{game_url}" width="100%" height="600px" frameborder="0" scrolling="no" allowfullscreen="true"></iframe>
            </div>
        </div>
        '''

        post_body = {
            'title': title,
            'content': html_content,
            'labels': ['Games', game.get('category', 'Arcade')]
        }

        try:
            request = service.posts().insert(blogId=BLOG_ID, body=post_body)
            request.execute()
            print(f"تم نشر اللعبة بنجاح: {title}")
        except Exception as e:
            print(f"خطأ أثناء نشر اللعبة {title}: {e}")

if __name__ == '__main__':
    main()
