def validate_phone(phone):

    if len(phone)==10 and phone.isdigit():
        return True

    return False

def validate_cgpa(cgpa):

    try:

        cgpa=float(cgpa)

        if cgpa>=0 and cgpa<=10:
            return True

        return False

    except ValueError:

        return False