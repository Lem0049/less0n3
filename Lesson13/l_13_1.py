def get_formatted_name(first, last, second=""):
    if second:
        full_name = f"{first.title()} {last.title()} {second.title()}"
    else:
        full_name = f"{first.title()} {last.title()}"
    return full_name
