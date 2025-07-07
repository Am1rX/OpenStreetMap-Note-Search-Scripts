📜 Interactive OpenStreetMap Note Searcher
A simple yet powerful command-line tool to interactively search for notes on OpenStreetMap by text content. Just run the script, enter your query, and get instant results directly in your terminal.
✨ Key Features
Interactive Search: Prompts the user to enter a search term.
Text-Based Query: Finds notes containing any word or phrase.
Clear & Concise Output: Displays essential details for each found note, including ID, status, description, and location.
Lightweight: No external libraries needed besides requests.
🚀 Getting Started
Follow these simple steps to get the script up and running on your local machine.
Prerequisites
Ensure you have Python 3.7 or a newer version installed.
Installation
Clone the repository:
git clone <YOUR_REPOSITORY_URL>
cd <your-repo-folder>


Install the necessary package:
This script requires the requests library to communicate with the OSM API. Install it using pip:
pip install requests


🛠️ How to Use
Running the script is straightforward:
Execute the script from your terminal:
python search_notes.py 

(Assuming you have named the file search_notes.py)
When prompted, type the word or phrase you want to search for and press Enter:
Enter the word or phrase to search for >> guest room


The script will then fetch and display the results.
Sample Session
$ python search_notes.py
Enter the word or phrase to search for >> coffee shop

Searching for: 'coffee shop'...

--- Found 25 results ---

Note ID: 3465890
Status: open
Description: There is a coffee shop here called "The Daily Grind"
Location (Lat, Lon): 40.7128, -74.0060
--------------------

Note ID: 3465891
Status: closed
Description: old coffee shop, now a bookstore
Location (Lat, Lon): 51.5074, -0.1278
--------------------

...and so on.


📄 License
This project is distributed under the MIT License. See the LICENSE file for more information.

