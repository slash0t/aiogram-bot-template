from sqlmodel import Session, select

from utils.db_api.db import engine


class Commands:
    @staticmethod
    def save(obj):
        with Session(engine) as session:
            session.add(obj)
            session.commit()
            session.refresh(obj)
        return obj

    @staticmethod
    def save_all(objects):
        with Session(engine) as session:
            for obj in objects:
                session.add(obj)

            session.commit()

            for obj in objects:
                session.refresh(obj)

        return objects

    @staticmethod
    def select_by_id(table, pk):
        with Session(engine) as session:
            return session.get(table, pk)

    @staticmethod
    def exec_selection(statement):
        with Session(engine) as session:
            results = session.exec(statement)
            return results

    @staticmethod
    def select_one(statement):
        return Commands.exec_selection(statement).one()

    @staticmethod
    def select_first(statement):
        return Commands.exec_selection(statement).first()

    @staticmethod
    def select_multiple(statement):
        return Commands.exec_selection(statement).all()

    @staticmethod
    def select_all(table):
        statement = select(table)
        return Commands.exec_selection(statement).all()
