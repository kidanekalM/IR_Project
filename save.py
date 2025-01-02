import requests
from bs4 import BeautifulSoup

# Base URL for STEP Bible
base_url = "https://www.stepbible.org/?q=version=Geez@reference=Ps."

# Initialize an empty list to store notes
notes = []

# Custom headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Iterate from Psalm 1 to 150
for psalm_num in range(1, 151):
    # Construct the URL for the current psalm
    url = f"{base_url}{psalm_num}&options=VHNUG"
    
    # Send an HTTP request to fetch the web page content with headers
    response = requests.get(url, headers=headers)
    
    # Parse the web page content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the note from the specific div (replace 'your-div-class' with the actual class name)
    note_div = soup.find('div', class_='passageContentHolder')
    
    if note_div:
        # Get the text content of the note and add it to the list
        note_text = note_div.get_text(strip=True)
        notes.append({'doc_id': psalm_num, 'text': note_text})

# Save the notes to a Python file with utf-8 encoding
with open('psalms_notes.py', 'w', encoding='utf-8') as file:
    file.write(f"psalms_notes = {notes}")

print("Notes have been successfully extracted and saved in 'psalms_notes.py'")
