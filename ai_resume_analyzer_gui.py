import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from PyPDF2 import PdfReader

skills = [
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Python",
    "Java",
    "SQL",
    "Git",
    "REST API"
]

selected_resume = ""

def load_pdf():

    global selected_resume

    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_path:

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, text)

        selected_resume = file_path

def analyze_resume():

    resume = text_area.get("1.0", tk.END)

    found = []
    missing = []

    for skill in skills:

        if skill.lower() in resume.lower():
            found.append(skill)
        else:
            missing.append(skill)

    score = int((len(found) / len(skills)) * 100)

    result = f"CV Score: {score}/100\n\n"

    result += "Detected Skills:\n"

    for item in found:
        result += f"✓ {item}\n"

    result += "\nMissing Skills:\n"

    for item in missing:
        result += f"✗ {item}\n"

    

    result += "\nRecommendations:\n"

    if "SQL" in missing:
        result += "• Learn SQL for database management\n"

    if "Git" in missing:
        result += "• Learn Git for version control\n"

    if "REST API" in missing:
        result += "• Learn REST API for backend development\n"

    result += "\nResume Evaluation:\n"

    if score >= 80:
        result += "✅ Ready for Internship / Junior Roles"
    elif score >= 60:
        result += "⚠️ Good Foundation - Improve Missing Skills"
    else:
        result += "❌ Needs More Development"

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result)


root = tk.Tk()
root.title("AI Resume Analyzer")
root.geometry("700x600")

title = tk.Label(
    root,
    text="AI Resume Analyzer",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

text_area = scrolledtext.ScrolledText(
    root,
    width=80,
    height=12
)
text_area.pack(pady=10)

load_button = tk.Button(
    root,
    text="Select Resume PDF",
    command=load_pdf,
    font=("Arial", 12)
)

load_button.pack(pady=5)

analyze_button = tk.Button(
    root,
    text="Analyze Resume",
    command=analyze_resume,
    font=("Arial", 12)
)
analyze_button.pack(pady=10)

result_box = scrolledtext.ScrolledText(
    root,
    width=80,
    height=15
)
result_box.pack(pady=10)

root.mainloop()