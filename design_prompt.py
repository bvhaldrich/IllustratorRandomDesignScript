import random

# Categories
themes = [
    "Retro", "Fantasy", "80s", "Sci-Fi", "Neutral", "Fitness", "Minimalist", "Futuristic", 
    "Nature", "Cyberpunk", "Steampunk", "Luxury", "Vaporwave", "Art Deco", "Gothic", "Industrial", 
    "Bohemian", "Surrealism", "Abstract", "Pop Art"
]

products = [
    "Social Media Post", "Beverage Packaging", "Candy Branding", "Clothing Company Identity", 
    "Website Banner", "Event Poster", "App UI", "Magazine Cover", "Book Cover", "Album Cover", 
    "Business Card", "Restaurant Menu", "T-Shirt Design", "Gaming UI", "E-commerce Website", 
    "YouTube Thumbnail", "Movie Poster", "Sticker Pack"
]

color_schemes = [
    "Monochrome", "Pastel", "Neon", "Earthy Tones", "Bold Contrasts", "Muted Colors", "Black & White", 
    "Gradient-Based", "Analogous Colors", "Triadic Colors", "Minimalist Colors", "Psychedelic"
]

moods = [
    "Energetic", "Elegant", "Playful", "Mysterious", "Luxurious", "Edgy", "Calm", "Sophisticated", 
    "Whimsical", "Dark & Moody", "Vibrant & Fun", "Futuristic", "Dramatic", "Serene & Peaceful"
]

typography_styles = [
    "Bold Sans-serif", "Serif Classic", "Handwritten", "Futuristic", "Minimalist", "Calligraphic", 
    "Vintage Script", "Gothic", "Grunge", "Geometric", "Monospaced", "3D Typography", "Neon Glow"
]

target_audiences = [
    "Young Adults", "Children", "Luxury Shoppers", "Fitness Enthusiasts", "Tech Enthusiasts", 
    "Artists & Creatives", "Corporate Professionals", "Gamers", "Eco-conscious Consumers", 
    "Music Lovers", "Foodies", "Sci-Fi Fans", "Travel Enthusiasts"
]

optional_challenges = [
    "Use only 1 color", "Use exactly 10 colors", "No words allowed", "No red in the design", 
    "Must use a specific resolution (e.g., 1920x1080)", "Only use black and white", 
    "Use only hand-drawn elements", "Typography must be the main focus", "Use a pixel art style", 
    "Design must loop seamlessly (good for patterns)", "Incorporate a hidden message", 
    "Use only circles and straight lines", "The design must be animated"
]

# Generate a random design prompt
def generate_prompt():
    theme = random.choice(themes)
    product = random.choice(products)
    color_scheme = random.choice(color_schemes)
    mood = random.choice(moods)
    typography = random.choice(typography_styles)
    audience = random.choice(target_audiences)
    challenge = random.choice(optional_challenges)

    prompt = (f"🎨 Design a {product} with a {theme} theme.\n"
              f"🎨 Color Scheme: {color_scheme}\n"
              f"🎨 Mood: {mood}\n"
              f"🎨 Typography: {typography}\n"
              f"🎨 Target Audience: {audience}\n"
              f"🔥 Optional Challenge: {challenge}")

    return prompt
