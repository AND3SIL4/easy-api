from sqlmodel import Field, Session, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


sql_file_name = "data_script.db"
sqlite_url = f"sqlite:///{sql_file_name}"


engine = create_engine(sqlite_url, echo=True)


def create_database():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    hero_1 = Hero(name="Deadpool", secret_name="Dive Wilson", age=41)
    hero_2 = Hero(name="IronMan", secret_name="Tony Stark")
    hero_3 = Hero(name="Spiderman", secret_name="Peter Parker", age=22)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        # Commit the session
        session.commit()  # The session will be close when with finished


def main():
    create_database()
    create_heroes()


if __name__ == "__main__":
    main()
