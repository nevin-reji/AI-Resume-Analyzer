from utils.pdf_parser import extract_text_from_pdf


pdf_path = "sample_resume.pdf"

text = extract_text_from_pdf(pdf_path)

print("\n==============================")
print("EXTRACTED RESUME TEXT")
print("==============================\n")

print(text)