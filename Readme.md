# Sentiment Analysis API using GROQ API

## Overview

This application allows users to upload CSV or Excel file through a web interface by a Python Flask backend. The backend converts the uploaded file into a Pandas DataFrame and iterates through each row of it and performs sentiment analysis on each row and the result for each row is mapped to each row by storing it into a dictionary. The resulting dictionary is then converted into JSON and dicplayed into the website.

### Features

- Upload CSV or Excel (.csv, .xlsx, .xls) files.
- Convert the uploaded file into a Pandas DataFrame.
- Perform sentiment analysis on DataFrame
- Return and display the Sentiment as formatted JSON on the webpage.
- Handles file upload errors and unsupported file formats

## Installation

1. Prerequisites:

   - Python 3.8 and above
   - Pandas 2.2.x
   - Flask 3.0.x
   - strictjson 5.1.x
   - groq 0.11.x

2. Installation Steps:

   1. Clone the repository or download the code.
   2. Install the Prerequisites

## Usage

1. Replace the GROQ API key with your API key in FileToDataFrame class **init**() method.

2. Run the app.py file in terminal.

   ```bash
   python app.py
   ```

   This will start the development server.

3. Access the Web Interface
   - Open your browser and navigate to http://127.0.0.1:5000/home
   - You will see a simple form where you can upload a file (CSV or Excel).
   - After selecting a file, click the "Upload" and "Analyse" buttons.
   - The Sentiment Analysis data will appear in JSON format.

## Application Structure

1. Flask Backend (app.py):

   - Routes:

     - GET /: Renders the HTML form from templates/index.html.
     - POST /home: Handles file uploads and converts the file to a DataFrame. Returns the JSON representation of the DataFrame.

   - File Handling:

     - The uploaded file is saved in the uploads/ folder.
     - Based on the file extension, the app uses Pandas' read_csv() or read_excel() to load the file into a DataFrame.

   - Error Handling:

     - If the file is not found, not selected, or in an unsupported format, appropriate error messages are returned.

2. Utilities (utils.py): Contains the utility classes required by the API.

   - FileToDataFrame(file_path):
     - Initializes a FileToDataFrame object with the specified file path.
     - Loads the data from the file path into a pandas DataFrame if the format is CSV or Excel.
     - Raises a ValueError if the file format is not supported.
   - llm(system_prompt, user_prompt)

     - Interacts with the LLM using Groq to analyze the user prompt based on the system prompt.
     - Requires LLM imports within the function (not shown in provided code).
     - Returns the LLM's response as the sentiment analysis result.

   - analyze(self, text: str) -> dict:

     - Uses the internal llm function to analyze the provided text.
     - Constructs a dictionary containing system and user prompts, output format (Positive, Negative, Neutral with descriptive names), and the llm function as the analysis method.
     - Returns the constructed dictionary with sentiment scores.

   - output(self) -> dict:

     - Iterates through the loaded DataFrame (if available).
     - For each row, extracts the text from the 'Review' column (assuming the column name).
     - Analyzes the text using the analyze function.
     - Stores the analyzed text and its sentiment scores in a dictionary.
     - Returns the constructed dictionary containing all analyzed texts and scores.

## Error Handling

The application includes basic error handling for various scenarios:

- No file selected: If no file is uploaded, a message will be displayed.
- Unsupported file format: Only CSV and Excel files are supported.
- General exceptions: Other errors are caught and displayed on the frontend.

## Conclusion

This application provides a simple solution to upload .csv or .xlsx file containing reviews and performing sentiment analysis on them and returning JSON output.
