from sqlmodel import Field, SQLModel


# Create model
class Hero(SQLModel, table=True):
    # Id will be increment in db
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
