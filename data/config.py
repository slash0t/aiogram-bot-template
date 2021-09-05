from environs import Env
from os import path

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

PG_USER = env.str("PG_USER")
PG_PASSWORD = env.str("PG_PASSWORD")
DATABASE = env.str("DATABASE")
DB_HOST = env.str("DB_HOST")

POSTGRES_URL = f'postgresql://{PG_USER}:{PG_PASSWORD}@{DB_HOST}/{DATABASE}'

ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
