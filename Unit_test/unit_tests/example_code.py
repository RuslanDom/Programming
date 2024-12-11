def get_social_status(age):
    if not isinstance(age, (float, int)):
        raise ValueError('Please provide a number!')

    if age < 0:
        raise ValueError('Check age')
    elif 0 <= age < 13:
        return 'Child'
    elif 13 <= age < 18:
        return 'Teenager'
    elif 18 <= age < 58:
        return 'Adult'
    elif 58 <= age < 65:
        return 'Elderly'
    else:
        return 'Pensioner'