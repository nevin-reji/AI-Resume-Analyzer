from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity


def calculate_skill_match(
    resume_skills,
    job_skills
):

    resume_set = set(
        skill.lower()
        for skill in resume_skills
    )

    job_set = set(
        skill.lower()
        for skill in job_skills
    )

    matched_skills = (
        resume_set.intersection(job_set)
    )

    missing_skills = (
        job_set - resume_set
    )

    if len(job_set) == 0:

        score = 0

    else:

        score = (
            len(matched_skills)
            /
            len(job_set)
        ) * 100

    return {

        "score": round(score, 2),

        "matched_skills":
            sorted(matched_skills),

        "missing_skills":
            sorted(missing_skills)

    }


def calculate_text_similarity(
    resume_text,
    job_description
):

    documents = [

        resume_text,

        job_description

    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(
        documents
    )

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return round(
        similarity * 100,
        2
    )


def calculate_final_score(
    skill_score,
    text_similarity
):

    final_score = (

        skill_score * 0.70

        +

        text_similarity * 0.30

    )

    return round(
        final_score,
        2
    )