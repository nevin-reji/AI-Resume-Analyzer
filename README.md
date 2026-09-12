# AI Resume Analyzer

### AI-powered resume analysis and job matching platform

[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge)](https://ai-resume-analyzer-avup.onrender.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Render](https://img.shields.io/badge/Deployed-Render-purple?style=for-the-badge)](https://render.com/)

> Analyze your resume against a job description, identify matching and missing skills, and understand how closely your profile aligns with a target role.

**Live Application:** [AI Resume Analyzer](https://ai-resume-analyzer-avup.onrender.com/)

---

## Overview

**AI Resume Analyzer** is a web application that evaluates the compatibility between a candidate's resume and a target job description.

The system extracts text from uploaded PDF resumes, identifies relevant skills, compares them with job requirements, and calculates an overall compatibility score using **skill matching** and **NLP-based text similarity**.

The goal is to help students, graduates, and job seekers identify skill gaps and improve their resumes before applying for positions.

---

## Key Features

- 📄 **PDF Resume Analysis**  
  Extracts and processes text from uploaded resumes.

- 🧠 **Automated Skill Extraction**  
  Detects technical and professional skills from resumes and job descriptions.

- 🎯 **Job Compatibility Scoring**  
  Calculates an overall match score between a resume and a target role.

- 🔍 **Skill Gap Detection**  
  Identifies skills required by the job description but missing from the resume.

- 📊 **NLP Similarity Analysis**  
  Uses TF-IDF and cosine similarity to measure textual alignment.

- 📈 **Interactive Results Dashboard**  
  Presents match scores, extracted skills, matching skills, and missing skills.

- 🔐 **Temporary File Processing**  
  Uploaded resumes are processed temporarily and removed after analysis.

- 🌐 **Public Web Application**  
  Deployed as a live Flask application using Render and Gunicorn.

---

## How It Works

```text
             ┌──────────────────────┐
             │     Upload Resume    │
             │        (PDF)         │
             └──────────┬───────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │   PDF Text Extraction│
             │       PyMuPDF        │
             └──────────┬───────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │    Text Cleaning     │
             │   & Normalization    │
             └──────────┬───────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │    Skill Extraction  │
             │      skills.json     │
             └──────────┬───────────┘
                        │
                ┌───────┴────────┐
                │                │
                ▼                ▼
      ┌──────────────────┐ ┌──────────────────┐
      │  Skill Matching  │ │  NLP Similarity  │
      │                  │ │                  │
      │ Resume vs Job    │ │ TF-IDF +         │
      │ Requirements     │ │ Cosine Similarity│
      └────────┬─────────┘ └────────┬─────────┘
               │                    │
               └──────────┬─────────┘
                          ▼
               ┌─────────────────────┐
               │   Final Match Score │
               └──────────┬──────────┘
                          │
                          ▼
               ┌─────────────────────┐
               │ Analysis Dashboard  │
               │                     │
               │ • Match Score       │
               │ • Matching Skills   │
               │ • Missing Skills    │
               │ • NLP Similarity    │
               └─────────────────────┘
```

---

## Scoring Methodology

The current scoring system combines two signals.

### Skill Match — 70%

Measures how many skills required by the job description are detected in the candidate's resume.

```text
Skill Match =
(Matching Required Skills / Total Required Skills) × 100
```

### NLP Similarity — 30%

Uses **TF-IDF vectorization** and **cosine similarity** to measure the textual similarity between the resume and job description.

### Final Score

```text
Final Score =
(Skill Match × 0.70) +
(NLP Similarity × 0.30)
```

---

## Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Flask |
| NLP / ML | Scikit-learn, TF-IDF, Cosine Similarity |
| PDF Processing | PyMuPDF |
| Data | JSON |
| Production Server | Gunicorn |
| Version Control | Git, GitHub |
| Deployment | Render |

---

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── skills.json
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── tests/
│   ├── __init__.py
│   └── test_parser.py
│
├── utils/
│   ├── __init__.py
│   ├── pdf_parser.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   └── job_matcher.py
│
└── uploads/
```

---

## Getting Started

### Prerequisites

- Python 3.x
- Git

### Clone the Repository

```bash
git clone https://github.com/nevin-reji/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### Create a Virtual Environment

#### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Example Workflow

### 1. Upload Resume

Upload a resume in PDF format.

### 2. Add Job Description

Paste the description of the position you're applying for.

### 3. Analyze

The application processes both inputs and performs skill matching and NLP similarity analysis.

### 4. Review Results

The results page provides:

- Overall match score
- Skill match score
- NLP similarity score
- Detected resume skills
- Matching skills
- Missing skills

---

## Example Job Description

```text
We are looking for an AI/ML Engineer with experience in Python,
Machine Learning, Deep Learning, NumPy, Pandas, Scikit-learn,
TensorFlow, SQL, Flask and REST APIs.

The candidate should have strong problem-solving skills,
data analysis experience, and knowledge of developing
machine learning applications.
```

---

## Security & Privacy

Resume files can contain sensitive personal information, so the application follows a temporary-processing approach.

Current protections include:

- PDF file type restriction
- Maximum upload size
- Secure filename handling
- Randomized temporary filenames
- Automatic deletion after processing
- Resume files excluded from version control

> **Privacy Note:** This project is currently an educational/portfolio deployment. Additional production security measures such as rate limiting, stronger file validation, monitoring, and a formal privacy policy should be implemented before handling large-scale public traffic.

---

## Deployment

The application is deployed on **Render** using Gunicorn.

Production start command:

```bash
gunicorn app:app
```

### Live Demo

🌐 [AI Resume Analyzer](https://ai-resume-analyzer-avup.onrender.com/)

> The free Render instance may spin down after inactivity, so the first request after a period of inactivity can take longer.

---

## Screenshots

### Homepage

_Add a screenshot of the homepage here._

```text
docs/screenshots/home.png
```

### Analysis Results

_Add a screenshot of the analysis results here._

```text
docs/screenshots/result.png
```

---

## Roadmap

### Completed

- [x] PDF resume upload
- [x] Resume text extraction
- [x] Skill extraction
- [x] Job skill matching
- [x] TF-IDF similarity analysis
- [x] Match score calculation
- [x] Results dashboard
- [x] GitHub repository
- [x] Public deployment
- [x] Google Search Console verification

### Planned

- [ ] Context-aware skill extraction
- [ ] ATS compatibility score
- [ ] Resume section analysis
- [ ] Resume keyword optimization
- [ ] AI-powered improvement recommendations
- [ ] Job recommendation engine
- [ ] Resume quality scoring
- [ ] Skill-gap recommendations
- [ ] Interactive analytics
- [ ] Rate limiting
- [ ] Enhanced PDF validation
- [ ] Custom domain
- [ ] SEO optimization
- [ ] Automated testing
- [ ] CI/CD pipeline

---

## Future Vision

The long-term goal is to evolve the project into a complete **AI-powered career optimization platform**.

```text
Resume
   ↓
ATS Analysis
   ↓
Job Matching
   ↓
Skill Gap Detection
   ↓
Personalized Recommendations
   ↓
Resume Optimization
   ↓
Job Recommendations
   ↓
Career Insights
```

---

## What I Learned

This project provided practical experience in:

- Flask web application development
- PDF text extraction
- Natural Language Processing
- TF-IDF vectorization
- Cosine similarity
- Feature-based matching
- File upload handling
- Frontend/backend integration
- Git and GitHub
- Cloud deployment
- Production serving with Gunicorn
- Basic web security and privacy

---

## Author

### Nevin Reji

**B.Tech Computer Science Engineering — Artificial Intelligence & Machine Learning**

Interested in:

`Artificial Intelligence` · `Machine Learning` · `Data Science` · `Full Stack Development`

---

## Links

🌐 **Live Demo:**  
https://ai-resume-analyzer-avup.onrender.com/

💻 **Repository:**  
https://github.com/nevin-reji/AI-Resume-Analyzer

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐.