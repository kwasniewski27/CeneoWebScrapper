def extract(ancestor, selector = None, attribute = None, many = False):
    if selector:
        if many:
            if attribute:
                return [item[attribute].strip() for item in ancestor.select(selector)]
            return [item.text.strip() for item in ancestor.select(selector)]
        if attribute:
            try:
                return ancestor.select_one(selector)[attribute].strip()
            except TypeError:
                return None
        try:
            return ancestor.select_one(selector).text.strip()
        except AttributeError:
            return None     
    if attribute:
        try:
            return ancestor[attribute]
        except TypeError:
            return None
    return ancestor.text.strip()
        