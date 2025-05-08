🧠 AI Resume Analyzer
AI Resume Analyzer is a Streamlit-based web application designed to assist job seekers and recruiters by analyzing resumes using Natural Language Processing (NLP) techniques. The tool extracts key information, evaluates resume quality, and provides actionable feedback to enhance the effectiveness of resumes.

🚀 Features
Resume Parsing: Extracts essential details such as contact information, education, work experience, and skills from uploaded resumes.

Keyword Analysis: Identifies and highlights relevant keywords to ensure alignment with job descriptions.

Scoring Mechanism: Evaluates resumes based on predefined criteria to provide a comprehensive score.

Feedback & Recommendations: Offers suggestions to improve resume content and structure.

User-Friendly Interface: Interactive and intuitive UI built with Streamlit for seamless user experience.



🛠️ Technologies Used
Python 3.11+

Streamlit: For building the web interface.

pytesseract: For Optical Character Recognition (OCR) to extract text from images or PDFs.

spaCy: For advanced NLP tasks.

uv: For managing Python dependencies and virtual environments.

📦 Installation
Prerequisites
Ensure Tesseract OCR is installed on your system.

For Windows users, download the installer from here and add the installation path to your system's environment variables.

Steps
Clone the Repository

bash
Copy
Edit
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
Set Up Virtual Environment

bash
Copy
Edit
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install Dependencies

bash
Copy
Edit
uv pip install -r requirements.txt
Run the Application

bash
Copy
Edit
streamlit run main.py
📁 Project Structure
bash
Copy
Edit
ai-resume-analyzer/
├── .venv/                  # Virtual environment
├── main.py                 # Main application script
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation

🤝 Contributing
Contributions are welcome! If you'd like to enhance the project, please fork the repository and submit a pull request.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

📬 Contact
For any inquiries or feedback, please reach out to me adeelmaheen602@gmail.com.
