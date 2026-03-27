import json
import os
from contextlib import closing

from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory
from database import add_contact, get_all_contacts, delete_contact, init_database as init_sqlite_db

load_dotenv()

app = Flask(__name__, static_folder=".", static_url_path="")

MEMORY_MESSAGES = []


DEFAULT_PAYLOAD = {
    "about": {
        "paragraphs": [
            "I am Sachin.s, a passionate student at the intersection of data, technology, and finance.",
            "My journey spans Python scripting, data analysis, and curiosity for financial systems.",
            "I enjoy building interfaces and solving analytical problems with practical insights.",
        ]
    },
    "stats": [
        {"value": "7+", "label": "Tech Skills"},
        {"value": "3+", "label": "Projects"},
        {"value": "100%", "label": "Driven"},
        {"value": "INF", "label": "Curiosity"},
    ],
    "skills": [
        {"name": "Python", "percent": 88},
        {"name": "Data Analysis", "percent": 82},
        {"name": "HTML", "percent": 78},
        {"name": "CSS", "percent": 72},
        {"name": "JavaScript", "percent": 68},
        {"name": "Finance", "percent": 80},
        {"name": "Statistics", "percent": 76},
    ],
    "projects": [
        {
            "title": "Market Trend Analyzer",
            "category": "Data Analysis",
            "description": "A Python-powered dashboard to analyze and visualize market trends.",
            "tech_stack": ["Python", "Pandas", "Matplotlib", "Statistics"],
            "demo_url": "#",
            "github_url": "#",
        },
        {
            "title": "Finance Dashboard",
            "category": "Web Development",
            "description": "An interactive personal finance tracker with visual analytics.",
            "tech_stack": ["HTML", "CSS", "JavaScript"],
            "demo_url": "#",
            "github_url": "#",
        },
        {
            "title": "Student Performance Model",
            "category": "Data Science",
            "description": "A regression model predicting student outcomes from academic data.",
            "tech_stack": ["Python", "NumPy", "Scikit-learn", "Statistics"],
            "demo_url": "#",
            "github_url": "#",
        },
    ],
    "education": [
        {
            "years": "2023 - Present",
            "degree": "Bachelor Degree - Computer Science / Data Analytics",
            "school": "University / College Name | Pursuing",
        },
        {
            "years": "2021 - 2023",
            "degree": "Higher Secondary Education (12th Grade)",
            "school": "School Name | Science Stream - Mathematics, Computer Science",
        },
        {
            "years": "2019 - 2021",
            "degree": "Secondary Education (10th Grade)",
            "school": "School Name | Completed with Distinction",
        },
    ],
    "contact": {
        "email": "sachin@email.com",
        "social_links": [
            {"platform": "GitHub", "url": "#", "short": "GH"},
            {"platform": "LinkedIn", "url": "#", "short": "IN"},
            {"platform": "Twitter", "url": "#", "short": "X"},
            {"platform": "Kaggle", "url": "#", "short": "K"},
        ],
    },
}


def get_conn():
    return None  # Not needed for SQLite


def init_db():
    """Initialize SQLite database"""
    try:
        init_sqlite_db()
        print("✅ Database initialized successfully!")
    except Exception as e:
        print(f"⚠️  Database initialization warning: {e}")


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.get("/api/portfolio")
def get_portfolio():
    if not DB_READY:
        return jsonify(DEFAULT_PAYLOAD)

    try:
        with closing(get_conn()) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT payload FROM portfolio_content WHERE section = %s", ("main",))
                row = cur.fetchone()
                return jsonify(row["payload"] if row else DEFAULT_PAYLOAD)
    except Exception:
        return jsonify(DEFAULT_PAYLOAD)


@app.get("/api/widgets")
def get_widgets():
    """Get visitor count and motivational quote"""
    contacts = get_all_contacts()
    visitor_count = len(contacts) + 100
    
    return jsonify({
        "visitors": visitor_count,
        "quote": "Discipline and consistency turn dreams into outcomes."
    })


@app.post("/api/contact")
def save_contact():
    """Save contact message to database"""
    try:
        data = request.get_json(force=True)
    except:
        return jsonify({"error": "Invalid JSON"}), 400
    
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify({"error": "All fields are required"}), 400

    # Save to SQLite database
    if add_contact(name, email, message):
        return jsonify({"status": "ok", "message": "Message saved successfully"}), 201
    else:
        return jsonify({"error": "Failed to save message"}), 500


@app.get("/health")
def health():
    return jsonify({"status": "ok", "message": "Server is running"})


@app.route("/admin")
def admin():
    return send_from_directory(".", "admin.html")


@app.get("/api/admin/contacts")
def admin_get_contacts():
    """Get all contact messages for admin panel"""
    try:
        contacts = get_all_contacts()
        contacts_list = [dict(contact) for contact in contacts]
        return jsonify(contacts_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.delete("/api/admin/contacts/<int:contact_id>")
def admin_delete_contact(contact_id):
    """Delete a contact message"""
    try:
        if delete_contact(contact_id):
            return jsonify({"status": "ok"}), 200
        else:
            return jsonify({"error": "Failed to delete contact"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    init_db()
    print("🚀 Starting Flask server...")
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
else:
    init_db()
