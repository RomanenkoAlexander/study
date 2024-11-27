def introspection_info(obj):
    obj_type = type(obj).__name__

    # Получение атрибутов объекта
    attributes = [at for at in dir(obj) if not callable(getattr(obj, at))]

    # Получение методов объекта
    methods = [m for m in dir(obj) if callable(getattr(obj, m))]

    # Получение информации о модуле
    module = obj.__class__.__module__

    dict_int = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,

    }

    return dict_int



number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("пример")
print(string_info)