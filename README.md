# Book Summarizer

This is a Streamlit app that summarizes a PDF book using the OpenAI API. It extracts text from the PDF, splits it into smaller portions, and generates summaries using the OpenAI text-davinci-002 model.

## Prerequisites

- Python 3.7 or higher
- PyPDF2 library
- Streamlit library
- OpenAI library

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/elchristog/book-summarizer.git

2. Install the required dependencies:
3.    ```pip install -r requirements.txt

## Usage
- Set up your OpenAI API key. You can obtain an API key from the OpenAI website.

- Place your PDF file in the project directory.

- Run the Streamlit app:

```streamlit run streamlit_app.py
- Access the app through the provided URL in the terminal or your web browser.

- Enter your OpenAI API key in the text input field.

- Choose the PDF file using the file uploader.

- The app will extract text from the PDF, summarize each chapter, and display the summaries along with the corresponding page numbers.

## Contributing
Contributions are welcome! If you find any issues or want to enhance the functionality, feel free to submit a pull request.

## License
This project is licensed under the MIT License.
