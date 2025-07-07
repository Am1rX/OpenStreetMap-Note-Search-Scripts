# 📜 Interactive OpenStreetMap Note Searcher

A simple yet powerful command-line tool to **interactively search for notes on OpenStreetMap (OSM)** by text content. Just run the script, enter your query, and get instant results — right in your terminal.

---

## ✨ Key Features

* 🔍 **Interactive Search** – Prompts the user to enter a search term.
* 📝 **Text-Based Query** – Finds notes containing any word or phrase.
* 📌 **Clear & Concise Output** – Displays essential details:
  • Note ID
  • Status (open/closed)
  • Description
  • Location (Latitude, Longitude)
* ⚡ **Lightweight** – Requires only the built-in `requests` library.

---

## 🚀 Getting Started

Follow these simple steps to get the script running on your local machine.

### ✅ Prerequisites

* Python **3.7** or newer installed.

### 📦 Installation

Clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
cd <your-repo-folder>
```

Install the required package:

```bash
pip install requests
```

---

## 🛠️ How to Use

Simply run the script from your terminal:

```bash
python search_notes.py
```

When prompted, enter the word or phrase you'd like to search:

```
Enter the word or phrase to search for >> coffee shop
```

The script will then fetch and display the results.

---

## 💡 Sample Session

```bash
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
...
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open an issue or submit a pull request.
