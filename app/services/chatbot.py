def get_response(text: str):
    text = text.lower()

    if "stipendiya" in text:
        return "Stipendiya haqida ma'lumot..."

    elif "hemis" in text:
        return "HEMIS: https://hemis.uz"

    elif "salom" in text:
        return "Salom! Sizga qanday yordam bera olaman?"

    return "Savolingizni tushunmadim 🤔"