import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import urllib


def load_credentials():
    load_dotenv()

    sql_host = os.getenv("SQL_SERVER_HOST")
    sql_db = os.getenv("SQL_SERVER_DB")
    sql_user = os.getenv("SQL_SERVER_USER")
    sql_password = os.getenv("SQL_SERVER_PASSWORD")

    # PostgreSQL
    pg_host = os.getenv("POSTGRES_HOST")
    pg_port = os.getenv("POSTGRES_PORT")
    pg_db = os.getenv("POSTGRES_DB")
    pg_user = os.getenv("POSTGRES_USER")
    pg_password = os.getenv("POSTGRES_PASSWORD")

    # ODBC Driver
    driver = "{ODBC Driver 17 for SQL Server}"

    return (
        sql_host,
        sql_db,
        sql_user,
        sql_password,
        pg_host,
        pg_port,
        pg_db,
        pg_user,
        pg_password,
        driver,
    )


def connect_to_sql(sql_host, sql_db, sql_user, sql_password, driver):
    try:
        sql_connection_string = urllib.parse.quote_plus(
            f"DRIVER={driver};"
            f"SERVER={sql_host};"
            f"DATABASE={sql_db};"
            f"UID={sql_user};"
            f"PWD={sql_password};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=yes;"
        )
        sql_connection_engine = create_engine(
            f"mssql+pyodbc:///?odbc_connect={sql_connection_string}"
        )
        print("[SUCCESS] → Connection to SQL Server now Live.")
    except SQLAlchemyError as e:
        print(f"SQL Server connection failed: {e}")
        print(""" How to troubleshoot:
                > 1. Check credentials in .env file are correct
                > 2. Verify SQL Server is running
                > 3. Check Windows Authentification is enable or SQL Login on macOS
                > 4. Check that Encryption is Madatory for connection            
            """)

    return sql_connection_engine


def connect_to_sql(pg_host, pg_port, pg_db, pg_user, pg_password):
    try:
        pg_connection_engine = create_engine(
            f"postgresql+psycopg2://{pg_user}:{pg_password}"
            f"@{pg_host}:{pg_port}/{pg_db}",
            connect_args={"host": pg_host, "port": pg_port},
        )
        # Test connection và check version
        with pg_connection_engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()[0]

        print("Connected to PostgreSQL")
        print(f"     Version: {version[:50]}...\n")

    except SQLAlchemyError as e:
        print(f"PostgreSQL connection failed: {e}")
        print(""" How to troubleshoot:
            > 1. Check PostgreSQL is running
            > 2. Verify username and password
            > 3. Check database exists
            """)
    except Exception as e:
        print(f"Unexpected errors: {e}")
        raise
    return pg_connection_engine


def main():
    (
        sql_host,
        sql_db,
        sql_user,
        sql_password,
        pg_host,
        pg_port,
        pg_db,
        pg_user,
        pg_password,
        driver,
    ) = load_credentials()

    sql_engine = connect_to_sql(sql_host, sql_db, sql_user, sql_password, driver)
    pg_engine = connect_to_sql(pg_host, pg_port, pg_db, pg_user, pg_password)


if __name__ == "__main__":
    main()
