def input_errors(func):
    """Decorator to handle input errors"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone, please."
        except IndexError:
            return "You must enter a valid command."
    return wrapper
