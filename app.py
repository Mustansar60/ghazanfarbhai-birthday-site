from flask import Flask, render_template, request, jsonify
import os
import glob

app = Flask(__name__)

# Store wishes in memory (will reset when server restarts)
visitor_wishes = []

# Predefined family wishes
family_wishes = [
    {
        "name": "Ghazanfar Maqsood (Husband)",
        "message": "My dearest Laraib, you are the light of my life and the beating of my heart. Every day with you is a blessing, and today we celebrate the amazing woman you are. Happy Birthday, my love! ❤️",
        "emoji": "💕"
    },
    {
        "name": "Hurain Zahra (Child)",
        "message": "Happy Birthday Mama! You're the best mom in the whole world! I love your hugs, your stories, and how you make everything better. Love you so much! 🥰",
        "emoji": "🌟"
    },
    {
        "name": "Nalain Zahra (Child)",
        "message": "Mama, you're my superhero! Thank you for always being there and making me smile. I hope your birthday is as amazing as you are! 🦸‍♀️",
        "emoji": "🎈"
    },
    {
        "name": "Adan Zahra (Child)",
        "message": "Happy Birthday to the most wonderful mama! You make every day special with your love and care. I love you to the moon and back! 🌙",
        "emoji": "⭐"
    }
]

@app.route('/')
def home():
    # Get list of images and music files
    image_files = []
    music_files = []
    
    # Get images from static/images directory
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.webp']
    for extension in image_extensions:
        image_files.extend(glob.glob(os.path.join('static/images', extension)))
        image_files.extend(glob.glob(os.path.join('static/images', extension.upper())))
    
    # Get music files from static/music directory
    music_extensions = ['*.mp3', '*.wav', '*.ogg']
    for extension in music_extensions:
        music_files.extend(glob.glob(os.path.join('static/music', extension)))
        music_files.extend(glob.glob(os.path.join('static/music', extension.upper())))
    
    # Convert to relative paths for the template
    image_files = [f.replace('\\', '/') for f in image_files]
    music_files = [f.replace('\\', '/') for f in music_files]
    
    return render_template('index.html', 
                         family_wishes=family_wishes,
                         visitor_wishes=visitor_wishes,
                         image_files=image_files,
                         music_files=music_files)

@app.route('/add_wish', methods=['POST'])
def add_wish():
    data = request.get_json()
    name = data.get('name', '').strip()
    message = data.get('message', '').strip()
    
    if name and message:
        wish = {
            'name': name,
            'message': message,
            'emoji': '💖'
        }
        visitor_wishes.append(wish)
        return jsonify({'success': True, 'wish': wish})
    
    return jsonify({'success': False, 'error': 'Name and message are required'})

@app.route('/get_wishes')
def get_wishes():
    return jsonify({
        'family_wishes': family_wishes,
        'visitor_wishes': visitor_wishes
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)