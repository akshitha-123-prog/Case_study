from flask import Flask, render_template, request

app = Flask(__name__)

mood_songs = {
    "happy": ["Happy - Pharrell Williams", "Good Vibes - Chris Janson", "Best Day of My Life - American Authors"],
    "sad": ["Someone Like You - Adele", "Let Her Go - Passenger", "Fix You - Coldplay"],
    "energetic": ["Stronger - Kanye West", "Can’t Hold Us - Macklemore", "Eye of the Tiger - Survivor"],
    "calm": ["Weightless - Marconi Union", "Let It Be - The Beatles", "River Flows In You - Yiruma"]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form['mood'].lower()
    songs = mood_songs.get(mood, ["No recommendations available for this mood."])
    return render_template('result.html', mood=mood.capitalize(), songs=songs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
