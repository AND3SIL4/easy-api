from sqlmodel import Field, SQLModel, create_engine


# Create model
class Hero(SQLModel, table=True):
    # Id will be increment in db
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


# Connect to database
sqlite_file_name = "db_tutorial.db"
sqlite_url = "sqlite:///db/{}".format(sqlite_file_name)

# Create engine
engine = create_engine(sqlite_url, echo=True)


def create_db_and_models():
    # Create all
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_models()
