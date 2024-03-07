from flask import Flask, request, redirect
import string
import random

app = Flask(__name__)

# Dictionary to store mappings between shortened URLs and original URLs
url_mapping = {}

# Function to generate a random shortened URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))  # Generate a 6-character short URL
    return short_url

# Endpoint to shorten a URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('url')
    if not original_url:
        return {'error': 'URL is required'}, 400

    short_url = generate_short_url()
    url_mapping[short_url] = original_url

    return {'shortened_url': f"http://localhost:5000/{short_url}"}

# Endpoint to redirect to the original URL
@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
    original_url = url_mapping.get(short_url)
    if not original_url:
        return {'error': 'Shortened URL not found'}, 404

    return redirect(original_url, code=302)

url_mapping = {
    'irfan': 'https://techie-irfan.godaddysites.com/',
    # Add more mappings as needed
}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)


