def get_val(collection: dict, key: str, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default.
    :param collection: исходный словарь
    :param key: ключ
    :param default:
    :return:
    """
    clean_key = key.strip()
    if collection.get(clean_key) is not None:
        return collection.get(clean_key)
    else:
        return default
