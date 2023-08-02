from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = ')532j8(0+oqe0frsht1_69%ke4pnw4(@33f*uuj9d3le$p#9%c'

DEBUG = True

DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": 'defaultdb_bail',
            "USER": 'postgres',
            "PASSWORD": 'AVNS_XsoM-MTsvINDikW',
            "HOST": '127.0.0.1',
            "PORT": 5432,
        }
    }
DATABASES["default"]["OPTIONS"] = {
"sslmode": "prefer"
}