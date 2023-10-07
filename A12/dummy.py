users = dict(A='p@ss', B='pass')

def suppress_exception(exception, result):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception:
                return result
        return inner
    return decorator

@suppress_exception(exception=KeyError, result=False)
def authenticate(user, password):
    print(f'authenticating {user}')
    return users[user] == password

print(authenticate('A','pass'))
print(authenticate('A','p@ss'))
print(authenticate('B','pass'))
print(authenticate('B','p@ss'))