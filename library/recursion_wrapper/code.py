from types import GeneratorType
def bootstrap(cache=False):
    def _helper(f, stack=[], memo={}, args_list=[]):
        def wrappedfunc(*args):
            if cache:
                if not stack and args in memo:
                    return memo[args]
                args_list.append(args)
            if stack:
                return f(*args)
            to = f(*args)
            while True:
                if isinstance(to, GeneratorType):
                    if cache and args_list[-1] in memo:
                        to = stack[-1].send(memo[args_list.pop()])
                    else:
                        stack.append(to)
                        to = next(to)
                else:
                    if cache:
                        memo[args_list.pop()] = to
                    stack.pop()
                    if not stack:
                        return to
                    to = stack[-1].send(to)
        return wrappedfunc
    return _helper

if __name__ == "__main__":
    @bootstrap(True)
    def fibonacci(n):
        if n <= 2:
            yield 1
        yield (yield fibonacci(n - 1)) + (yield fibonacci(n - 2))
    
    print(fibonacci(50))