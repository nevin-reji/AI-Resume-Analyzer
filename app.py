from flask import (
    Flask,
    render_template,
    request
)

import os
import uuid

from werkzeug.utils import secure_filename

from utils.pdf_parser import (
    extract_text_from_pdf
)

from utils.resume_parser import (
    clean_text
)

from utils.skill_extractor import (
    extract_skills
)

from utils.job_matcher import (
    calculate_skill_match,
    calculate_text_similarity,
    calculate_final_score
)


app = Flask(__name__)


# ==============================
# CONFIGURATION
# ==============================

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = (
    UPLOAD_FOLDER
)

# Maximum upload size = 5 MB
app.config["MAX_CONTENT_LENGTH"] = (
    5 * 1024 * 1024
)


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


# ==============================
# HOME PAGE
# ==============================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )

# ==============================
# ROBOTS.TXT
# ==============================

@app.route("/robots.txt")
def robots():

    return """User-agent: *
Allow: /

Sitemap: https://ai-resume-analyzer-avup.onrender.com/sitemap.xml
""", 200, {
        "Content-Type": "text/plain"
    }

# ==============================
# SITEMAP.XML
# ==============================

@app.route("/sitemap.xml")
def sitemap():

    return """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

    <url>
        <loc>https://ai-resume-analyzer-avup.onrender.com/</loc>
    </url>

</urlset>
""", 200, {
        "Content-Type": "application/xml"
    }

# ==============================
# ANALYZE RESUME
# ==============================

@app.route(
    "/analyze",
    methods=["POST"]
)
def analyze():

    # Get resume
    resume = request.files.get(
        "resume"
    )

    # Get job description
    job_description = request.form.get(
        "job_description",
        ""
    )


    # --------------------------
    # VALIDATION
    # --------------------------

    if not resume:

        return "Please upload a resume."


    if resume.filename == "":

        return "Please select a resume."


    if not resume.filename.lower().endswith(
        ".pdf"
    ):

        return (
            "Only PDF files are allowed."
        )


    if not job_description.strip():

        return (
            "Please enter a job description."
        )


    # --------------------------
    # SAVE TEMPORARY FILE
    # --------------------------

    original_filename = (
        secure_filename(
            resume.filename
        )
    )


    filename = (

        str(uuid.uuid4())

        + "_"

        + original_filename

    )


    file_path = os.path.join(

        app.config[
            "UPLOAD_FOLDER"
        ],

        filename

    )


    resume.save(file_path)


    try:

        # ==========================
        # 1. EXTRACT PDF TEXT
        # ==========================

        resume_text = (
            extract_text_from_pdf(
                file_path
            )
        )


        # Check empty PDF

        if not resume_text.strip():

            return (
                "Could not extract text "
                "from this PDF."
            )


        # ==========================
        # 2. CLEAN RESUME
        # ==========================

        cleaned_resume = (
            clean_text(
                resume_text
            )
        )


        # ==========================
        # 3. EXTRACT RESUME SKILLS
        # ==========================

        resume_skills = (
            extract_skills(
                cleaned_resume
            )
        )


        # ==========================
        # 4. EXTRACT JOB SKILLS
        # ==========================

        job_skills = (
            extract_skills(
                job_description
            )
        )


        # ==========================
        # 5. SKILL MATCH
        # ==========================

        skill_result = (
            calculate_skill_match(
                resume_skills,
                job_skills
            )
        )


        # ==========================
        # 6. NLP SIMILARITY
        # ==========================

        similarity = (
            calculate_text_similarity(
                cleaned_resume,
                job_description
            )
        )


        # ==========================
        # 7. FINAL SCORE
        # ==========================

        final_score = (
            calculate_final_score(
                skill_result["score"],
                similarity
            )
        )


        # ==========================
        # 8. SHOW RESULTS
        # ==========================

        return render_template(

            "result.html",

            final_score=final_score,

            skill_score=
                skill_result["score"],

            similarity=similarity,

            resume_skills=
                resume_skills,

            matched_skills=
                skill_result[
                    "matched_skills"
                ],

            missing_skills=
                skill_result[
                    "missing_skills"
                ]

        )


    finally:

        # ==========================
        # DELETE TEMPORARY PDF
        # ==========================

        if os.path.exists(
            file_path
        ):

            os.remove(
                file_path
            )


# ==============================
# RUN APPLICATION
# ==============================

if __name__ == "__main__":

    app.run(
        debug=True
    )