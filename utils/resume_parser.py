import re


def clean_text(text):
    """
    Clean extracted resume text.
    """

    # Convert to lowercase
    text = text.lower()

    # Replace multiple spaces/newlines
    # with a single space
    text = re.sub(r"\s+", " ", text)

    # Keep useful characters
    text = re.sub(
        r"[^a-zA-Z0-9\s+#.\-/]",
        " ",
        text
    )

    # Remove extra spaces again
    text = re.sub(r"\s+", " ", text)

    return text.strip()