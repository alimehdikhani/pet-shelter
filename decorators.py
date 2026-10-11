def log_operation(function):

    def wrapper(*args, **kwargs):

        result = function(*args, **kwargs)

        print(f"Operation completed: {function.__name__}")

        return result

    return wrapper