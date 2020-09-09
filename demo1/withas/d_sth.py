def do_sth():
    print('do_sth')
    pass


class sth:
    # def __init__(self):
    #     pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def say(self):
        print('hey')

    def __call_duty(self):
        pass


pass
