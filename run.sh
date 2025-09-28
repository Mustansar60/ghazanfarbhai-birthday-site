#!/bin/bash

echo "🎉 Starting Laraib Zahra's Birthday Website! 🎂"
echo ""
echo "To run the website:"
echo "1. Make sure Python and Flask are installed"
echo "2. Install dependencies: pip install flask"
echo "3. Run: python app.py"
echo "4. Open: http://localhost:5000"
echo ""
echo "Add photos to static/images/ and music to static/music/"
echo ""
echo "Happy Birthday Laraib! 💕✨"

# Try to run the app if Flask is available
if python3 -c "import flask" 2>/dev/null; then
    echo "Flask found! Starting the website..."
    python3 app.py
else
    echo "Please install Flask first: pip install flask"
fi