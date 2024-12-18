from src.config.db import create_db_and_tables
from src.models.user import User


def main():
    create_db_and_tables()


if __name__ == "__main__":
    main()
