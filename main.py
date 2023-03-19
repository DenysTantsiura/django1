import logging
# from time import time
from timeit import default_timer

# export PYTHONPATH="${PYTHONPATH}:/1prj/example_beautifulsoup_and_scrapy/"
# https://stackoverflow.com/questions/49493675/django-db-utils-programmingerror-relation-auth-user-does-not-exist-django-v

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')


def duration(fun):
    def inner(*args, **kwargs):
        start = default_timer()
        rez = fun(*args, **kwargs)
        logging.info(f'{default_timer()-start=} sec')

        return rez

    return inner


@duration
def main():
    print(default_timer())


if __name__ == '__main__':
    main()





