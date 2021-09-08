from exceptions import(InheritanceException,
                       InvalidNameException,
                       NotCallableException,
                       NotCompatibleOperationException,
                       TypeNotValidException,
                       NotValidValueException,
                       NoneException)
from xml.etree.ElementTree import Element, SubElement
from functools import wraps


def is_sub_type(value, sub_type):

    if not issubclass(value.__class__, sub_type):
        message = f'value must be {sub_type.__name__} type.'
        raise TypeNotValidException(message)


def is_not_none(value):
    return True if value is not None else False


def set_value(param, default, **kwargs) -> object:
    if param in kwargs:
        return kwargs[param]
    return default


def convert_to_string(value):
    if type(value) is bool:
        return str(value).lower()
    return str(value)


def force_type(method):
    """
    Forces a valid value type for a method.

    All parameters must be annotated.

    The value type None is accepted.

    Ex.:  

        @force_type
        def method(self, value: str,  value2: int):
            pass
    """

    @wraps(method)
    def get_value(*args, **kwargs):

        args_values = args[1:]
        kwargs_values = kwargs

        params_types = tuple(method.__annotations__.items())

        params_types_values = tuple(zip(params_types, args_values))

        for (param_, type_), value_ in params_types_values:
            if value_ is not None and type(value_) is not type_:
                raise NotValidValueException(f'The param {param_} must be of type {type_}.')

        params_types_values = tuple((((param_, type_), value_) for (param_, type_) in params_types
                                     for param_kwarg, value_ in kwargs_values.items() if param_ == param_kwarg))

        for (param_, type_), value_ in params_types_values:
            if value_ is not None and type(value_) is not type_:
                raise NotValidValueException(f'The param {param_} must be of type {type_}.')

        return method(*args, **kwargs)

    return get_value


def is_operation(operation_type):

    def get_method(method):

        @wraps(method)
        def get_value(*args, **kwargs):

            args_values = args[1:]
            kwargs_values = kwargs

            for operation in args_values:
                if operation is None:
                    message = 'None it is not callable.'
                    raise NotCallableException(message)
                if not isinstance(operation, operation_type):
                    message = f'{operation.__class__.__name__} operation not compatible. Operation must be of {operation_type.__name__} type.'
                    raise NotCompatibleOperationException(message)

            for operation in kwargs_values.values():
                if operation is None:
                    message = 'None it is not callable.'
                    raise NotCallableException(message)
                if not isinstance(operation, operation_type):
                    message = f'{operation.__class__.__name__} operation not compatible. Operation must be of {operation_type.__name__} type.'
                    raise NotCompatibleOperationException(message)

            return method(*args, **kwargs)

        return get_value

    return get_method
