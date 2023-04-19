def split_list(lst):
    result = []
    if len(lst) <= 130:
        result.append(lst)
    elif len(lst) > 130 and len(lst) <= 260:
        result.append(lst[:130])
        result.append(lst[130:])
    elif len(lst) > 260:
        result.append(lst[:130])
        result.append(lst[130:260])
        result.append(lst[260:])
    return result