from pathlib import Path
import random
import numpy as np
from faker import Faker

fake = Faker("en_GB")
random.seed()
np.random.seed()

ROOT_DIR = Path(__file__).resolve().parents[1]

RAW_DIRS = {
    "hris": ROOT_DIR / "01_raw" / "hris",
    "ats": ROOT_DIR / "01_raw" / "ats",
    "lms": ROOT_DIR / "01_raw" / "lms",
    "engagement": ROOT_DIR / "01_raw" / "engagement",
    "timekeeping": ROOT_DIR / "01_raw" / "timekeeping",
}

for path in RAW_DIRS.values():
    path.mkdir(parents=True, exist_ok=True)

COUNTRIES = ["UK", "Germany", "France", "Netherlands", "Ireland"]

COUNTRY_WEIGHTS = {
    "UK": 0.55,
    "Germany": 0.20,
    "France": 0.12,
    "Netherlands": 0.08,
    "Ireland": 0.05,
}

SITES_BY_COUNTRY = {
    "UK": ["London", "Manchester", "Birmingham", "Leeds", "Glasgow"],
    "Germany": ["Berlin", "Munich", "Hamburg"],
    "France": ["Paris", "Lyon"],
    "Netherlands": ["Amsterdam", "Rotterdam"],
    "Ireland": ["Dublin", "Cork"],
}

DEPARTMENTS = [
    "Operations",
    "Supply Chain",
    "Customer Support",
    "Sales",
    "Technology",
    "Finance",
    "Commercial",
    "People",
]

DEPARTMENT_WEIGHTS = {
    "Operations": 0.32,
    "Supply Chain": 0.20,
    "Customer Support": 0.12,
    "Sales": 0.10,
    "Technology": 0.08,
    "Finance": 0.06,
    "Commercial": 0.07,
    "People": 0.05,
}

JOB_FAMILIES = {
    "Operations": [
        ("Site Engineer", 0.25),
        ("Project Manager", 0.20),
        ("Construction Supervisor", 0.30),
        ("Health & Safety Officer", 0.15),
        ("Operations Analyst", 0.10),
    ],
    "Supply Chain": [
        ("Procurement Specialist", 0.35),
        ("Logistics Coordinator", 0.40),
        ("Warehouse Manager", 0.25),
    ],
    "Customer Support": [
        ("Customer Support Rep", 0.70),
        ("Customer Success Manager", 0.30),
    ],
    "Sales": [
        ("Sales Executive", 0.65),
        ("Account Manager", 0.35),
    ],
    "Technology": [
        ("Data Analyst", 0.40),
        ("Data Engineer", 0.25),
        ("Software Engineer", 0.35),
    ],
    "Finance": [
        ("Financial Analyst", 0.60),
        ("Accountant", 0.40),
    ],
    "Commercial": [
        ("Commercial Analyst", 0.50),
        ("Pricing Manager", 0.50),
    ],
    "People": [
        ("HR Advisor", 0.70),
        ("HR Business Partner", 0.30),
    ],
}

JOB_LEVEL_MAP = {
    "Site Engineer": "Mid",
    "Project Manager": "Manager",
    "Construction Supervisor": "Manager",
    "Health & Safety Officer": "Mid",
    "Operations Analyst": "Mid",
    "Procurement Specialist": "Mid",
    "Logistics Coordinator": "Junior",
    "Warehouse Manager": "Manager",
    "Customer Support Rep": "Junior",
    "Customer Success Manager": "Manager",
    "Sales Executive": "Junior",
    "Account Manager": "Manager",
    "Data Analyst": "Mid",
    "Data Engineer": "Senior",
    "Software Engineer": "Senior",
    "Financial Analyst": "Mid",
    "Accountant": "Mid",
    "Commercial Analyst": "Mid",
    "Pricing Manager": "Manager",
    "HR Advisor": "Mid",
    "HR Business Partner": "Senior",
}

GENDERS = ["Male", "Female"]
GENDER_WEIGHTS = [0.89, 0.11]

ETHNICITIES = [
    "White",
    "Black",
    "Asian",
    "Mixed",
    "Other",
]

ETHNICITY_WEIGHTS = [0.72, 0.08, 0.10, 0.06, 0.04]

AGE_BANDS = ["18-24", "25-34", "35-44", "45-54", "55+"]
AGE_BAND_WEIGHTS = [0.18, 0.34, 0.24, 0.16, 0.08]

SURVEY_THEMES = [
    "Workload",
    "Manager Support",
    "Career Growth",
    "Recognition",
    "Inclusion",
    "Wellbeing",
]

COURSES = [
    {"course_id": "C001", "course_name": "Code of Conduct", "mandatory": 1},
    {"course_id": "C002", "course_name": "Health and Safety", "mandatory": 1},
    {"course_id": "C003", "course_name": "Data Protection", "mandatory": 1},
    {"course_id": "C004", "course_name": "Leadership Essentials", "mandatory": 0},
    {"course_id": "C005", "course_name": "Stakeholder Management", "mandatory": 0},
    {"course_id": "C006", "course_name": "Advanced Analytics", "mandatory": 0},
]

ATTRITION_RISK_BY_COUNTRY = {
    "UK": 0.10,
    "Germany": 0.18,
    "France": 0.14,
    "Netherlands": 0.08,
    "Ireland": 0.15,
}

TRAINING_COMPLETION_BY_DEPARTMENT = {
    "Operations": 0.56,
    "Supply Chain": 0.60,
    "Customer Support": 0.64,
    "Sales": 0.68,
    "Technology": 0.78,
    "Finance": 0.80,
    "Commercial": 0.70,
    "People": 0.82,
}

ENGAGEMENT_BASE_BY_COUNTRY = {
    "UK": 69,
    "Germany": 60,
    "France": 65,
    "Netherlands": 78,
    "Ireland": 63,
}

OVERTIME_RISK_BY_DEPARTMENT = {
    "Operations": 0.38,
    "Supply Chain": 0.31,
    "Customer Support": 0.22,
    "Sales": 0.16,
    "Technology": 0.10,
    "Finance": 0.09,
    "Commercial": 0.14,
    "People": 0.07,
}

ABSENCE_RISK_BY_COUNTRY = {
    "UK": 0.05,
    "Germany": 0.08,
    "France": 0.06,
    "Netherlands": 0.04,
    "Ireland": 0.07,
}


def weighted_choice(options, weights):
    return random.choices(options, weights=weights, k=1)[0]


def choose_country():
    return weighted_choice(
        COUNTRIES,
        [COUNTRY_WEIGHTS[c] for c in COUNTRIES],
    )


def choose_site(country):
    return random.choice(SITES_BY_COUNTRY[country])


def choose_department():
    return weighted_choice(
        DEPARTMENTS,
        [DEPARTMENT_WEIGHTS[d] for d in DEPARTMENTS],
    )


def choose_job_role(department):
    role_list = JOB_FAMILIES[department]
    names = [r[0] for r in role_list]
    weights = [r[1] for r in role_list]
    return weighted_choice(names, weights)


def choose_gender():
    return weighted_choice(GENDERS, GENDER_WEIGHTS)


def choose_ethnicity():
    return weighted_choice(ETHNICITIES, ETHNICITY_WEIGHTS)


def choose_age_band():
    return weighted_choice(AGE_BANDS, AGE_BAND_WEIGHTS)