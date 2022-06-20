SECRET_KEY = 'django-insecure-^knhue$cf05lzd6@ge9@8#85(^5=twi$)z0-hza!efq69m7q=6'
PGPASS = '127.0.0.1:5432:shop:ilya:asdwow'


def read_pgpass():
    words = PGPASS.split(':')

    return {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST' : words[0],
            'PORT' : words[1],
            'NAME': words[2],
            'USER': words[3],
            'PASSWORD': words[4],
            }