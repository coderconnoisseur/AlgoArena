import csv
from app.database import SessionLocal
from app.models.problem import Problem

# Path to your CSV file
CSV_FILE = "D:/leetcode_questions.csv"

db = SessionLocal()

with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Check if problem already exists using slug or id
        existing = db.query(Problem).filter(Problem.slug == row['Question Slug']).first()
        if existing:
            continue

        problem = Problem(
            id=int(row['Question ID']),
            title=row['Question Title'],
            slug=row['Question Slug'],
            text=row['Question Text'],
            tags=row['Topic Tagged text'],
            difficulty=row['Difficulty Level'],
            success_rate=float(row['Success Rate']) if row['Success Rate'] else 0.0,
            total_submissions=int(row['total submission']),
            total_accepted=int(row['total accepted']),
            likes=int(row['Likes']),
            dislikes=int(row['Dislikes']),
            hints=row['Hints'],
            similar_question_ids=row['Similar Questions ID'],
            similar_question_texts=row['Similar Questions Text']
        )
        db.add(problem)

db.commit()
db.close()
print("✅ Problems imported successfully!")
