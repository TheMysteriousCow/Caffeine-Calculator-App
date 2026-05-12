import streamlit as st
import base64
import os
import re
from difflib import SequenceMatcher
from functions.logo import set_logo

# Logo Function

image_path = os.path.join(os.getcwd(), "images", "logo.png")

set_logo(
    image_path,
    top=-30,
    right=-20,
    width=140
)

# Styling
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Georgia', 'Times New Roman', serif;
    color: #5C4033;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: #5C4033 !important;
    }

.main-title {
    text-align: center;
    font-size: 3.4rem;
    font-family: 'Georgia', 'Times New Roman', serif;
    font-weight: 600;
    color: #5C4033;
    margin-bottom: 0.3rem;
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    font-size: 1.05rem;
    color: #5C4033;
    margin-bottom: 2rem;
}

.info-box, .warning-box, .good-box, .avoid-box, .neutral-box {
    padding: 1rem 1.2rem;
    border-radius: 14px;
    margin-top: 1rem;
    margin-bottom: 1rem;
    color: #5C4033;
    line-height: 1.55;
}

.info-box {
    background-color: #F8F1EB;
    border-left: 6px solid #B98B73;
}

.warning-box {
    background-color: #FFF3E8;
    border-left: 6px solid #D08A45;
}

.avoid-box {
    background-color: #FBEAEA;
    border-left: 6px solid #B95C5C;
}

.good-box {
    background-color: #EEF7EE;
    border-left: 6px solid #7FA87F;
}

.neutral-box {
    background-color: #F4F1EF;
    border-left: 6px solid #A89B93;
}

.small-note {
    font-size: 0.9rem;
    color: #6B4E3D;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>Additional Data</div>", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Add relevant health information so the app can give more personalised caffeine guidance.
</div>
""", unsafe_allow_html=True)

# Text Helpers
def normalize_text(text):
    text = str(text).lower()
    text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    text = text.replace("ß", "ss")
    text = re.sub(r"[^a-z0-9\s\-]", " ", text)
    text = text.replace("-", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_user_input(text):
    text = normalize_text(text)
    items = re.split(r"[\n,;/]+", text)
    return [item.strip() for item in items if item.strip()]


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def fuzzy_match(input_text, keywords, threshold=0.82):
    """
    Recognises exact matches, brand names, generic names and small spelling mistakes.
    Example: 'cirpofloxacin' will still match 'ciprofloxacin'.
    """
    input_text_norm = normalize_text(input_text)
    input_items = split_user_input(input_text)

    for keyword in keywords:
        keyword_norm = normalize_text(keyword)

        # Exact phrase match
        if keyword_norm in input_text_norm:
            return True, keyword

        # Fuzzy phrase match per line/item
        for item in input_items:
            if len(item) >= 5 and len(keyword_norm) >= 5:
                if similarity(item, keyword_norm) >= threshold:
                    return True, keyword

            # Partial match for longer medication names
            if len(keyword_norm) >= 6 and len(item) >= 6:
                if keyword_norm in item or item in keyword_norm:
                    return True, keyword

        # Word-level fuzzy matching
        words = input_text_norm.split()
        keyword_words = keyword_norm.split()

        for word in words:
            for key_word in keyword_words:
                if len(word) >= 5 and len(key_word) >= 5:
                    if similarity(word, key_word) >= threshold:
                        return True, keyword

    return False, None


def remove_duplicates(recommendations):
    seen = set()
    unique = []

    for rec in recommendations:
        key = rec["title"]
        if key not in seen:
            seen.add(key)
            unique.append(rec)

    return unique

# Medical Knowledge Base
CONDITION_RULES = [
    {
        "keywords": [
            "tachycardia", "fast heartbeat", "racing heart", "palpitations",
            "arrhythmia", "svt", "atrial fibrillation", "afib", "heart rhythm disorder",
            "heart rhythm problem", "irregular heartbeat"
        ],
        "title": "Fast heartbeat or heart rhythm symptoms",
        "level": "avoid",
        "message": (
            "Caffeine is a stimulant and may increase heart rate or make palpitations feel stronger in some people. "
            "This does not mean caffeine is always forbidden, but high-caffeine drinks and energy drinks are not ideal if these symptoms occur."
        ),
        "advice": "Recommendation: choose low-caffeine or caffeine-free options and avoid strong energy drinks."
    },
    {
        "keywords": [
            "hypertension", "high blood pressure", "blood pressure", "arterial hypertension"
        ],
        "title": "High blood pressure",
        "level": "warning",
        "message": (
            "Caffeine can temporarily raise blood pressure in some people. If blood pressure is already elevated, "
            "a moderate and consistent caffeine intake is usually the safer approach."
        ),
        "advice": "Recommendation: reduced caffeine intake recommended. Avoid very strong coffee and energy drinks."
    },
    {
        "keywords": [
            "anxiety", "panic", "panic attack", "panic disorder", "nervousness",
            "restlessness", "stress disorder"
        ],
        "title": "Anxiety or panic symptoms",
        "level": "warning",
        "message": (
            "Caffeine can increase alertness, but it can also increase shakiness, nervousness, restlessness "
            "and a racing-heart feeling."
        ),
        "advice": "Recommendation: try smaller portions, decaf coffee, herbal tea, or other caffeine-free alternatives."
    },
    {
        "keywords": [
            "insomnia", "sleep disorder", "sleep problems", "trouble sleeping",
            "poor sleep", "difficulty sleeping"
        ],
        "title": "Sleep difficulties",
        "level": "warning",
        "message": (
            "Caffeine can stay active in the body for several hours and may reduce sleep quality, especially if consumed later in the day."
        ),
        "advice": "Recommendation: avoid caffeine in the afternoon and evening."
    },
    {
        "keywords": [
            "reflux", "gerd", "acid reflux", "heartburn", "gastritis", "stomach ulcer",
            "ulcer", "sensitive stomach"
        ],
        "title": "Reflux or sensitive stomach",
        "level": "warning",
        "message": (
            "Coffee, caffeine and acidic drinks may worsen heartburn, reflux or stomach discomfort in some people."
        ),
        "advice": "Recommendation: monitor symptoms and consider gentler options such as caffeine-free herbal tea."
    },
    {
        "keywords": [
            "pregnant", "pregnancy", "breastfeeding", "lactation"
        ],
        "title": "Pregnancy or breastfeeding",
        "level": "warning",
        "message": (
            "During pregnancy or breastfeeding, caffeine intake should usually be limited because caffeine passes through the body differently."
        ),
        "advice": "Recommendation: keep caffeine low and follow professional medical advice."
    },
    {
        "keywords": [
            "epilepsy", "seizure", "seizures"
        ],
        "title": "Epilepsy or seizure history",
        "level": "warning",
        "message": (
            "High caffeine intake may affect sleep and nervous system stimulation, which can matter for some people with seizure disorders."
        ),
        "advice": "Recommendation: avoid high-caffeine products and ask a healthcare professional about a safe personal limit."
    }
]


ALLERGY_RULES = [
    {
        "keywords": [
            "caffeine allergy", "caffeine intolerance", "caffeine sensitivity",
            "sensitive to caffeine", "caffeine sensitive"
        ],
        "title": "Caffeine sensitivity or intolerance",
        "level": "avoid",
        "message": (
            "If you already know that you react strongly to caffeine, even small amounts may cause symptoms such as jitteriness, "
            "anxiety, headache, stomach discomfort or sleep problems."
        ),
        "advice": "Recommendation: choose caffeine-free alternatives instead of coffee, guarana, green tea or black tea."
    },
    {
        "keywords": [
            "guarana allergy", "allergy to guarana", "guarana intolerance", "guarana sensitivity",
            "guarana sensitive"
        ],
        "title": "Guarana allergy or sensitivity",
        "level": "avoid",
        "message": (
            "Guarana naturally contains caffeine and is often used in energy products. If you have a guarana allergy or sensitivity, "
            "guarana-based alternatives are not suitable."
        ),
        "advice": "Recommendation: avoid guarana-based products."
    },
    {
        "keywords": [
            "cocoa allergy", "cacao allergy", "chocolate allergy", "cocoa intolerance",
            "cacao intolerance", "chocolate intolerance", "cocoa sensitivity", "cacao sensitivity"
        ],
        "title": "Cocoa or chocolate allergy",
        "level": "avoid",
        "message": (
            "Cocoa and chocolate can contain small amounts of caffeine and theobromine. If you have an allergy or intolerance, "
            "cocoa-based alternatives are not suitable."
        ),
        "advice": "Recommendation: avoid cocoa-based alternatives."
    },
    {
        "keywords": [
            "green tea allergy", "black tea allergy", "tea allergy",
            "camellia sinensis allergy", "green tea intolerance", "black tea intolerance"
        ],
        "title": "Tea allergy or sensitivity",
        "level": "avoid",
        "message": (
            "Green tea and black tea both come from the tea plant and naturally contain caffeine. If you react to tea, "
            "these alternatives may not be appropriate."
        ),
        "advice": "Recommendation: avoid green tea and black tea if they trigger symptoms."
    },
    {
        "keywords": [
            "mate allergy", "yerba mate allergy", "mate intolerance", "yerba mate intolerance",
            "mate sensitivity", "yerba mate sensitivity"
        ],
        "title": "Mate allergy or sensitivity",
        "level": "avoid",
        "message": (
            "Yerba mate naturally contains caffeine. If you have a mate allergy or sensitivity, mate-based drinks are not suitable."
        ),
        "advice": "Recommendation: avoid yerba mate-based products."
    }
]


MEDICATION_RULES = [
    {
        "keywords": [
            "theophylline", "aminophylline", "euphyllin", "theo dur", "unifyl"
        ],
        "title": "Theophylline or aminophylline",
        "level": "avoid",
        "message": (
            "These medicines are chemically related to caffeine-like stimulants. Combining them with caffeine may increase side effects "
            "such as trembling, restlessness, insomnia, nausea or irregular heartbeat."
        ),
        "advice": "Recommendation: avoid high caffeine intake and ask a doctor or pharmacist about a safe limit."
    },
    {
        "keywords": [
            "ciprofloxacin", "ciproxin", "cipro", "norfloxacin", "enoxacin",
            "fluvoxamine", "floxifral"
        ],
        "title": "Medication that can slow caffeine breakdown",
        "level": "warning",
        "message": (
            "Some medicines can slow down how quickly caffeine is broken down. This can make caffeine effects feel stronger "
            "or last longer than usual."
        ),
        "advice": "Recommendation: reduce caffeine while taking this medication, especially if you feel jittery, restless or unwell."
    },
    {
        "keywords": [
            "clozapine", "leponex", "clozaril", "olanzapine", "zyprexa"
        ],
        "title": "Certain psychiatric medicines",
        "level": "warning",
        "message": (
            "Caffeine can affect how some psychiatric medicines are processed. Sudden large changes in caffeine intake may matter."
        ),
        "advice": "Recommendation: keep caffeine intake consistent and ask your doctor or pharmacist before making big changes."
    },
    {
        "keywords": [
            "methylphenidate", "ritalin", "concerta", "medikinet", "equasym",
            "amphetamine", "adderall", "lisdexamfetamine", "elvanse", "vyvanse"
        ],
        "title": "ADHD stimulant medication",
        "level": "warning",
        "message": (
            "Stimulant medication and caffeine can both increase alertness. Together, they may increase side effects such as "
            "restlessness, appetite changes, faster heartbeat or sleep problems."
        ),
        "advice": "Recommendation: avoid high-caffeine drinks and monitor how your body reacts."
    },
    {
        "keywords": [
            "pseudoephedrine", "ephedrine", "phenylephrine", "triofan", "otrivin complex",
            "sudafed"
        ],
        "title": "Decongestant or stimulant cold medication",
        "level": "warning",
        "message": (
            "Some cold medicines can stimulate the body. Together with caffeine, this may increase nervousness, heart rate or blood pressure."
        ),
        "advice": "Recommendation: keep caffeine low while using these medicines."
    },
    {
        "keywords": [
            "propranolol", "inderal", "bisoprolol", "concor", "metoprolol", "beloc",
            "atenolol", "tenormin", "carvedilol", "dilatrend", "nebivolol", "nebilet"
        ],
        "title": "Beta blocker medication",
        "level": "warning",
        "message": (
            "Beta blockers are often used for heart rate or blood pressure control. Caffeine may still trigger symptoms such as "
            "nervousness or palpitations in some people."
        ),
        "advice": "Recommendation: keep caffeine moderate and consistent."
    },
    {
        "keywords": [
            "amlodipine", "norvasc", "lisinopril", "zestril", "ramipril", "triatec",
            "enalapril", "reniten", "valsartan", "diovan", "losartan", "cosaar",
            "candesartan", "atacand", "irbesartan", "aprovel", "hydrochlorothiazide",
            "hct", "esidrex", "torasemide", "toresamid", "furosemide", "lasix"
        ],
        "title": "Blood pressure medication",
        "level": "warning",
        "message": (
            "Because this medication is related to blood pressure control, it is helpful to avoid very high caffeine intake "
            "and keep your daily amount consistent."
        ),
        "advice": "Recommendation: reduced caffeine intake may be helpful."
    },
    {
        "keywords": [
            "levothyroxine", "eltroxin", "euthyrox", "tirosint", "thyroxine"
        ],
        "title": "Thyroid medication",
        "level": "info",
        "message": (
            "Coffee can reduce the absorption of thyroid medication if taken too close together."
        ),
        "advice": "Recommendation: take thyroid medication as prescribed and avoid coffee directly around the dose unless your doctor advised otherwise."
    },
    {
        "keywords": [
            "warfarin", "marcoumar", "phenprocoumon", "acenocoumarol", "sintrom"
        ],
        "title": "Blood-thinning medication",
        "level": "info",
        "message": (
            "Caffeine itself is not usually the main issue here, but sudden diet changes and some teas or supplements may matter "
            "for people taking blood-thinning medication."
        ),
        "advice": "Recommendation: avoid sudden major changes in tea or supplement intake and ask a healthcare professional if unsure."
    },
    {
        "keywords": [
            "lithium", "lithiofor", "quilonum"
        ],
        "title": "Lithium medication",
        "level": "warning",
        "message": (
            "Large changes in caffeine intake may influence fluid balance and can matter for people taking lithium."
        ),
        "advice": "Recommendation: keep caffeine intake consistent and discuss changes with your doctor or pharmacist."
    }
]


NO_CAFFEINE_WARNING_MEDICATIONS = [
    {
        "keywords": [
            "aspirin", "aspirin cardio", "acetylsalicylic acid", "ass", "asa", "cardio aspirin",
            "thrombo ass"
        ],
        "title": "Aspirin / low-dose aspirin",
        "message": (
            "This medication was recognised. In typical daily use, there is no specific caffeine warning based on this medication alone."
        )
    },
    {
        "keywords": [
            "augmentin", "co amoxicillin", "co amoxi", "co amoxiclav",
            "amoxicillin clavulanic acid", "amoxicillin clavulanate",
            "amoxiclav", "amoxicillin", "clavulanic acid"
        ],
        "title": "Amoxicillin / clavulanic acid antibiotics",
        "message": (
            "This antibiotic was recognised. It is not one of the antibiotics typically known for strongly slowing caffeine breakdown."
        )
    },
    {
        "keywords": [
            "paracetamol", "dafalgan", "panadol", "acetaminophen"
        ],
        "title": "Paracetamol",
        "message": (
            "This medication was recognised. There is no specific caffeine warning based on this medication alone."
        )
    },
    {
        "keywords": [
            "ibuprofen", "algifor", "brufen", "nurofen", "diclofenac", "voltaren", "naproxen", "aleve"
        ],
        "title": "Common pain-relief medication",
        "message": (
            "This medication was recognised. There is no specific caffeine warning based on this medication alone. "
            "However, coffee or caffeine may worsen stomach discomfort in sensitive people."
        )
    },
    {
        "keywords": [
            "allopurinol", "zyloric"
        ],
        "title": "Allopurinol",
        "message": (
            "This medication was recognised. There is no specific caffeine warning based on this medication alone."
        )
    }
]

# Recommendation Logic
def check_rules(input_text, rules):
    matches = []

    for rule in rules:
        matched, matched_keyword = fuzzy_match(input_text, rule["keywords"])
        if matched:
            rule_copy = rule.copy()
            matches.append(rule_copy)

    return matches


def check_no_warning_medications(medication_text):
    matches = []

    for med in NO_CAFFEINE_WARNING_MEDICATIONS:
        matched, matched_keyword = fuzzy_match(medication_text, med["keywords"])
        if matched:
            med_copy = med.copy()
            med_copy["matched_keyword"] = matched_keyword
            matches.append(med_copy)

    return matches


def check_user_data(illness_text, allergy_text, medication_text):
    recommendations = []

    recommendations.extend(check_rules(illness_text, CONDITION_RULES))
    recommendations.extend(check_rules(allergy_text, ALLERGY_RULES))
    recommendations.extend(check_rules(medication_text, MEDICATION_RULES))

    return remove_duplicates(recommendations)


def box_class(level):
    if level == "avoid":
        return "avoid-box"
    if level == "warning":
        return "warning-box"
    if level == "info":
        return "info-box"
    return "good-box"

# Input Fields
st.markdown("<h3>Previous illness</h3>", unsafe_allow_html=True)
illness_list = st.text_area(
    "Enter previous illnesses or health conditions, one per line",
    placeholder="Example: high blood pressure, tachycardia, anxiety, reflux, insomnia..."
)

st.markdown("<h3>Allergies or sensitivities</h3>", unsafe_allow_html=True)
allergy_list = st.text_area(
    "Enter allergies or sensitivities, one per line",
    placeholder="Example: caffeine sensitivity, guarana allergy, cocoa allergy, green tea allergy..."
)

st.markdown("<h3>Medication</h3>", unsafe_allow_html=True)
medication_list = st.text_area(
    "Enter medications, one per line",
    placeholder="Example: bisoprolol, methylphenidate, ciprofloxacin, theophylline, Augmentin..."
)

# Disclaimer
st.markdown("""
<div class='info-box'>
<b>Important note:</b><br>
This app gives general caffeine-related information only. It does not diagnose, treat, prescribe or replace medical advice.
If you have symptoms, a medical condition, take regular medication, are pregnant, or feel unsure, please speak with a doctor,
pharmacist or another qualified healthcare professional.
</div>
""", unsafe_allow_html=True)

# Button + Output
if st.button("Check caffeine recommendations"):

    recommendations = check_user_data(illness_list, allergy_list, medication_list)
    no_warning_meds = check_no_warning_medications(medication_list)

    st.markdown("<h3>Your caffeine guidance</h3>", unsafe_allow_html=True)

    if recommendations:
        for rec in recommendations:
            st.markdown(f"""
            <div class='{box_class(rec["level"])}'>
            <b>{rec["title"]}</b><br><br>
            {rec["message"]}<br><br>
            <b>{rec["advice"]}</b>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class='info-box'>
        <b>Gentle next step:</b><br>
        You do not necessarily have to stop caffeine completely. A realistic first step can be choosing smaller servings,
        avoiding caffeine later in the day, switching to decaf, or checking the Alternatives page.
        </div>
        """, unsafe_allow_html=True)

    if no_warning_meds:
        for med in no_warning_meds:
            st.markdown(f"""
            <div class='neutral-box'>
            <b>{med["title"]}</b><br><br>
            {med["message"]}
            </div>
            """, unsafe_allow_html=True)

    if not recommendations and not no_warning_meds:
        st.markdown("""
        <div class='good-box'>
        <b>No specific caffeine-related warning found.</b><br><br>
        Based on the information entered, the app did not detect a clear caffeine-related condition, allergy or medication note.
        This does not mean caffeine is risk-free for everyone. It simply means that no specific rule in this app was triggered.
        </div>
        """, unsafe_allow_html=True)