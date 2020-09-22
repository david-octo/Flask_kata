def transform_row_age(row):
    if row['Age'] <= 18:
        return 'Children'
    elif row['Age'] <= 35:
        return 'Mid age'
    else:
        return 'Old'


def transform_age(data):
    new_cat = data.apply(transform_row_age, axis=1)
    data['Age_cat'] = new_cat
    return data
