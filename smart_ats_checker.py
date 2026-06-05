import re
from pypdf import PdfReader

print("===== SMART ATS RESUME CHECKER =====")


# Read TXT or PDF file
def read_file(file_name):
    try:

        # PDF Support
        if file_name.endswith(".pdf"):

            text = ""
            reader = PdfReader(file_name)

            for page in reader.pages:
                extracted_text = page.extract_text()

                if extracted_text:
                    text += extracted_text

            return text.lower()

        # TXT Support
        elif file_name.endswith(".txt"):

            with open(
                file_name,
                "r",
                encoding="utf-8"
            ) as file:

                return file.read().lower()

        else:
            print(
                "Only .txt and .pdf files supported."
            )
            return None

    except FileNotFoundError:
        print("File not found!")
        return None

    except Exception as e:
        print("Error:", e)
        return None


# Exact skill matching
def skill_exists(skill, text):

    pattern = (
        r'\b'
        + re.escape(skill)
        + r'\b'
    )

    return (
        re.search(
            pattern,
            text,
            re.IGNORECASE
        )
        is not None
    )


# ===============================
# JOB DESCRIPTION INPUT
# ===============================

print("\nJOB DESCRIPTION INPUT")
print("1. Paste Job Description")
print("2. Upload Job Description File")

jd_choice = input(
    "Enter Choice: "
).strip()

if jd_choice == "1":

    job_description = input(
        "\nPaste Job Description:\n"
    ).lower()

elif jd_choice == "2":

    jd_file = input(
        "Enter Job Description File Name: "
    ).strip()

    job_description = read_file(
        jd_file
    )

    if job_description is None:
        exit()

else:
    print("Invalid Choice")
    exit()


# ===============================
# RESUME INPUT
# ===============================

print("\nRESUME INPUT")
print("1. Paste Resume")
print("2. Upload Resume File")

resume_choice = input(
    "Enter Choice: "
).strip()

if resume_choice == "1":

    resume = input(
        "\nPaste Resume Text:\n"
    ).lower()

elif resume_choice == "2":

    resume_file = input(
        "Enter Resume File Name: "
    ).strip()

    resume = read_file(
        resume_file
    )

    if resume is None:
        exit()

else:
    print("Invalid Choice")
    exit()


# Fix merged words issue
resume = re.sub(
    r'([a-z])([A-Z])',
    r'\1 \2',
    resume
)


# ===============================
# SKILLS DATABASE
# ===============================

skills_database = [

    # Programming
    "python", "java",
    "javascript",
    "typescript",
    "c++", "c#",
    "php", "ruby",
    "go", "swift",
    "kotlin",

    # Frontend
    "html", "css",
    "react",
    "angular",
    "vue",

    # Backend
    "node.js",
    "express",
    "django",
    "flask",
    "spring boot",
    "api",
    "rest api",

    # Database
    "sql",
    "mysql",
    "mongodb",
    "postgresql",
    "sqlite",

    # DevOps / Cloud
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "linux",
    "terraform",

    # Data / AI
    "machine learning",
    "deep learning",
    "data science",
    "data analysis",
    "pandas",
    "numpy",
    "tensorflow",
    "pytorch",
    "excel",
    "power bi",

    # Tools
    "git",
    "github",
    "jira",
    "postman",

    # Soft Skills
    "communication",
    "problem solving",
    "leadership",
    "teamwork",
    "critical thinking"
]


matched_skills = []
missing_skills = []


# ===============================
# SKILL MATCHING
# ===============================

for skill in skills_database:

    skill_in_jd = skill_exists(
        skill,
        job_description
    )

    skill_in_resume = skill_exists(
        skill,
        resume
    )

    if skill_in_jd:

        if skill_in_resume:
            matched_skills.append(
                skill
            )
        else:
            missing_skills.append(
                skill
            )


# ===============================
# REALISTIC ATS SCORE
# ===============================

total_required_skills = (
    len(matched_skills)
    + len(missing_skills)
)

# Skills = 70%
if total_required_skills > 0:

    skill_match_ratio = (
        len(matched_skills)
        / total_required_skills
    )

    skill_score = (
        skill_match_ratio
        * 70
    )

else:
    skill_score = 0


# Resume Quality = 30%
section_score = 0

if "education" in resume:
    section_score += 5

if "project" in resume:
    section_score += 7

if "experience" in resume:
    section_score += 7

if "internship" in resume:
    section_score += 4

if "github" in resume:
    section_score += 4

if "certification" in resume:
    section_score += 3


ats_score = round(
    skill_score
    + section_score
)

# Safety limit
ats_score = min(
    ats_score,
    100
)


# ===============================
# ATS RESULT
# ===============================

print("\n===== ATS RESULT =====")

print(
    f"ATS Match Score: "
    f"{ats_score}/100"
)


print("\nMatched Skills:")

if matched_skills:

    for skill in matched_skills:
        print(
            "✔",
            skill.title()
        )

else:
    print(
        "No matching skills found"
    )


print("\nMissing Skills:")

if missing_skills:

    for skill in missing_skills:
        print(
            "✘",
            skill.title()
        )

else:
    print(
        "No missing skills"
    )


# ===============================
# RESUME SECTIONS
# ===============================

print(
    "\n===== RESUME SECTIONS ====="
)

sections = [
    "education",
    "skills",
    "project",
    "experience",
    "internship",
    "github",
    "certification"
]

for section in sections:

    if section in resume:
        print(
            "✔",
            section.title()
        )
    else:
        print(
            "✘",
            section.title()
        )


# ===============================
# RESUME ANALYSIS
# ===============================

print(
    "\n===== RESUME ANALYSIS ====="
)

if ats_score >= 80:
    strength = (
        "Strong Resume"
    )

elif ats_score >= 60:
    strength = (
        "Moderate Resume"
    )

else:
    strength = (
        "Weak Resume"
    )

print(
    f"Resume Strength: "
    f"{strength}"
)

print(
    f"ATS Compatibility: "
    f"{ats_score}%"
)


# ===============================
# SUGGESTIONS
# ===============================

print(
    "\n===== IMPROVEMENT "
    "SUGGESTIONS ====="
)

if "github" not in resume:
    print(
        "- Add GitHub profile"
    )

if "project" not in resume:
    print(
        "- Add Projects section"
    )

if "experience" not in resume:
    print(
        "- Add Work Experience"
    )

if "internship" not in resume:
    print(
        "- Add Internship experience"
    )

if "certification" not in resume:
    print(
        "- Add Certifications"
    )


print("\nTop Missing Skills:")

if missing_skills:

    for i, skill in enumerate(
        missing_skills[:5],
        start=1
    ):
        print(
            f"{i}. "
            f"{skill.title()}"
        )

else:
    print(
        "No critical skills missing"
    )