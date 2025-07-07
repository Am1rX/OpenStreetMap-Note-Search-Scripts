<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive OpenStreetMap Note Searcher</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .badge {
            display: inline-block;
            margin-right: 4px;
            margin-bottom: 4px;
        }
        pre {
            background-color: #1f2937; /* gray-800 */
            color: #f3f4f6; /* gray-200 */
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            font-family: 'Courier New', Courier, monospace;
        }
        code {
            font-family: 'Courier New', Courier, monospace;
        }
        h1, h2, h3 {
            font-weight: 700;
            border-bottom: 1px solid #e5e7eb; /* gray-200 */
            padding-bottom: 0.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        h1 { font-size: 2.25rem; }
        h2 { font-size: 1.875rem; }
        h3 { font-size: 1.5rem; border-bottom: none;}
    </style>
</head>
<body class="bg-gray-50 text-gray-800">

    <main class="max-w-4xl mx-auto p-4 sm:p-6 md:p-8 bg-white rounded-lg shadow-md my-10">
        
        <h1>📜 Interactive OpenStreetMap Note Searcher</h1>

        <div class="my-4">
            <a href="https://www.python.org/" class="badge">
                <img src="https://img.shields.io/badge/Python-3.7%2B-blue.svg" alt="Python 3.7+">
            </a>
            <a href="https://opensource.org/licenses/MIT" class="badge">
                <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
            </a>
        </div>

        <p class="text-lg text-gray-600 mb-6">
            A simple yet powerful command-line tool to interactively search for notes on <a href="https://www.openstreetmap.org/" class="text-blue-600 hover:underline">OpenStreetMap</a> by text content. Just run the script, enter your query, and get instant results directly in your terminal.
        </p>

        <h2>✨ Key Features</h2>
        <ul class="list-disc list-inside space-y-2 text-gray-700 mb-6">
            <li><strong>Interactive Search:</strong> Prompts the user to enter a search term.</li>
            <li><strong>Text-Based Query:</strong> Finds notes containing any word or phrase.</li>
            <li><strong>Clear & Concise Output:</strong> Displays essential details for each found note.</li>
            <li><strong>Lightweight:</strong> Relies only on the standard <code>requests</code> library.</li>
        </ul>

        <h2>🚀 Getting Started</h2>
        <p class="text-gray-700 mb-4">Follow these simple steps to get the script up and running on your local machine.</p>
        
        <h3>Prerequisites</h3>
        <p class="text-gray-700 mb-4">Ensure you have Python 3.7 or a newer version installed.</p>

        <h3>Installation</h3>
        <ol class="list-decimal list-inside space-y-4 text-gray-700">
            <li>
                <strong>Clone the repository:</strong>
                <pre><code>git clone &lt;YOUR_REPOSITORY_URL&gt;
cd &lt;your-repo-folder&gt;</code></pre>
            </li>
            <li>
                <strong>Install the necessary package:</strong>
                <p class="mt-2">This script requires the <code>requests</code> library. Install it using pip:</p>
                <pre><code>pip install requests</code></pre>
            </li>
        </ol>

        <h2>🛠️ How to Use</h2>
        <p class="text-gray-700 mb-4">Running the script is straightforward:</p>
        <ol class="list-decimal list-inside space-y-4 text-gray-700">
            <li>
                <strong>Execute the script from your terminal:</strong>
                <pre><code>python search_notes.py</code></pre>
                <p class="text-sm text-gray-500 mt-1">*(Assuming you have named the file `search_notes.py`)*</p>
            </li>
            <li>
                <strong>Enter your query when prompted:</strong>
                <pre><code>Enter the word or phrase to search for >> coffee shop</code></pre>
            </li>
            <li>The script will then fetch and display the results.</li>
        </ol>

        <h3>Sample Session</h3>
        <pre><code>$ python search_notes.py
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
...and so on.</code></pre>

        <h2>📄 License</h2>
        <p class="text-gray-700">
            This project is distributed under the MIT License. See the <code>LICENSE</code> file for more information.
        </p>

        <h2>🤝 Contributing</h2>
        <p class="text-gray-700">
            Contributions, issues, and feature requests are welcome! Feel free to check the 
            <a href="#" class="text-blue-600 hover:underline">issues page</a>.
        </p>

    </main>

</body>
</html>
