Restaurant Data Mining and AI Chatbot for Macapá
Project Overview
This project aims to build a web scraper to collect restaurant information in Macapá, including their menus, popular dishes, and customer reviews. The data is stored in a SQLite database and can be accessed via an AI-powered chatbot that answers questions about restaurants, their menus, and local dishes.

Key Features:
Web Scraping: Retrieves restaurant names, menus, ratings, and reviews from platforms like iFood and TripAdvisor.
Data Storage: Saves the collected data into a SQLite database for easy access.
NLP Chatbot: A chatbot that uses natural language processing (NLP) to respond to queries about Macapá restaurants, menus, and popular local dishes.
Sentiment Analysis: Analyze customer reviews to provide insights into the quality of service.
Project Structure
bash
Copy code
|-- data/                  # Folder to store raw and cleaned datasets
|-- db/                    # Folder containing the SQLite database
|-- src/                   # Source code
|   |-- scraper.py         # Script to scrape restaurant data from web
|   |-- database.py        # Script to handle SQLite operations
|   |-- chatbot.py         # NLP-based chatbot for answering queries
|-- requirements.txt       # List of required Python packages
|-- README.txt             # Project description and instructions
|-- LICENSE                # License file
Installation

Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/macapa-restaurant-chatbot.git
cd macapa-restaurant-chatbot
Step 2: Install Dependencies
Use the provided requirements.txt to install the necessary packages:

bash
Copy code
pip install -r requirements.txt
Dependencies include:

BeautifulSoup (for scraping HTML)
Selenium (for dynamic website scraping)
SQLite3 (for database management)
Flask/Django (for building the chatbot web interface)
spaCy/NLTK (for NLP processing)
OpenAI API (optional, for chatbot responses)
Running the Project
Step 1: Scraping Data
To scrape restaurant information from the web, run the following script:

bash
Copy code
python src/scraper.py
This will gather restaurant data and store it in a SQLite database under the db/ directory.

Step 2: Running the AI Chatbot
Once the data is scraped and stored, launch the AI chatbot to start querying the database:

bash
Copy code
python src/chatbot.py
This will start a local web server where users can ask questions like:

“What are the best restaurants for Amazonian cuisine in Macapá?”
“What is the most common dish served in local restaurants?”
Contributing
We welcome contributions! Here’s how you can help:

Fork the Repository: Make your own copy of the project.
Create a Branch:
bash
Copy code
git checkout -b feature-branch
Commit Changes: Commit your code to the new branch.
bash
Copy code
git commit -m "Add a feature"
Push Changes: Push your changes to GitHub.
bash
Copy code
git push origin feature-branch
Submit a Pull Request: Submit your changes for review.
Future Enhancements
Automated Data Updates: Implement a cron job or background process to periodically scrape data and update the database.
Expanded NLP Capabilities: Improve the chatbot’s ability to understand complex queries and respond with more nuanced answers.
Mobile App Integration: Consider building a mobile app interface for easier access to restaurant recommendations on the go.
License
This project is licensed under the MIT License - see the LICENSE file for details.










