from sqlmodel import select

from utils.db_api.commands.commands import Commands
from utils.db_api.models import User


def add_user(id_, name, created_at):
    user = User(id=id_, name=name, created_at=created_at)
    return Commands.save(user)


def get_last_user():
    statement = select(User).order_by(User.created_at.desc())
    return Commands.select_first(statement)
