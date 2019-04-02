def migratoryBirds(arr):
    max_count, max_type = 0, None

    for type_id in sorted(set(arr)):
        count = arr.count(type_id)
        if count > max_count:
            max_count, max_type = count, type_id

    return max_type
