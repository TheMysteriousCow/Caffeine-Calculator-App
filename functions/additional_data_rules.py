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