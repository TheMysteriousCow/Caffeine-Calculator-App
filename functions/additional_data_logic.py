import re
from difflib import SequenceMatcher

from functions.additional_data_rules import (
    CONDITION_RULES,
    ALLERGY_RULES,
    MEDICATION_RULES,
    NO_CAFFEINE_WARNING_MEDICATIONS
)


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
    input_text_norm = normalize_text(input_text)
    input_items = split_user_input(input_text)

    for keyword in keywords:
        keyword_norm = normalize_text(keyword)

        if keyword_norm in input_text_norm:
            return True, keyword

        for item in input_items:
            if len(item) >= 5 and len(keyword_norm) >= 5:
                if similarity(item, keyword_norm) >= threshold:
                    return True, keyword

            if len(keyword_norm) >= 6 and len(item) >= 6:
                if keyword_norm in item or item in keyword_norm:
                    return True, keyword

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
        matched, matched_keyword = fuzzy_match(
            medication_text,
            med["keywords"]
        )

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