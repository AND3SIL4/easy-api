import models
from sqlmodel import create_engine, SQLModel

# Dummy assign for import
_ = models

# Database location
sqlite_file_name = "db_tutorial.db"
sqlite_url = "sqlite:///app/db/{}".format(sqlite_file_name)

# Create engine
engine = create_engine(sqlite_url, echo=True)


def create_db_and_models():
    # Create all
    SQLModel.metadata.create_all(engine)


# Execute only if this file will be run
if __name__ == "__main__":
    create_db_and_models()
