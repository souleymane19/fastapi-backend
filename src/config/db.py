from sqlmodel import Field, Session, SQLModel, create_engine
# Définir le nom du fichier SQLite, par exemple 'database.db'
sqlite_file_name = "test.db"

# Créer l'URL de connexion à la base de données SQLite
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Créer l'engine de connexion à la base de données
engine = create_engine(sqlite_url, echo=True)


# Fonction pour créer la base de données et les tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Fonction pour obtenir une session de base de données
def get_db():
    with Session(engine) as session:
        yield session
