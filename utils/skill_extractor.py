import json


def load_skills():

    with open(
        "data/skills.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def extract_skills(text):

    skills_data = load_skills()

    found_skills = []

    text = text.lower()

    for category, skills in skills_data.items():

        for skill in skills:

            if skill.lower() in text:

                found_skills.append(skill)

    return sorted(
        list(set(found_skills))
    )