import csv
import os

import typer
from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.models.charts import Chart, Entry
from app.models.users import User
from app.security import get_password_hash

app = typer.Typer()

ASSETS_FOLDER = os.path.join('app/assets')
CHARTS_FILENAME = 'charts.csv'
ENTRIES_FILENAME = 'entries.csv'


def get_db():
    local_db_url = settings.DB_URL.replace('@db:', '@localhost:')
    engine = create_engine(local_db_url, echo=False)
    Session = sessionmaker(engine, expire_on_commit=False)

    with Session() as session:
        try:
            yield session
        finally:
            session.close()


@app.command()
def hello():
    """Test command"""
    print('Hello World!')


@app.command()
def create_user(email: str, name: str, password: str):
    """Create a user account"""

    # inicializar database
    db = next(get_db())

    db_user = (
        db.query(User)
        .where(
            and_(User.email == email, User.is_deleted == False)  # NoQA
        )
        .first()
    )

    if db_user:
        print('User email already exists')
        return

    user = User(email, name, get_password_hash(password))

    try:
        print('Creating user:', f"'{user.email}'.")

        db.add(user)
        db.commit()
        db.refresh(user)

        print('User created successfully!', f"'{user.email}'.")
    except Exception as e:
        raise e


@app.command()
def populate_charts():
    """Read information from 'app/assets/charts.csv'
    and push them into database"""
    charts_filepath = os.path.join(ASSETS_FOLDER, CHARTS_FILENAME)

    # inicializar database
    db = next(get_db())

    try:
        with open(charts_filepath, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            # pular header
            next(reader)

            for chart_row in reader:
                chart_name = chart_row[0]
                chart_code = chart_row[1]
                chart_dice = chart_row[2]

                db_chart = (
                    db.query(Chart).where(Chart.code == chart_code).first()
                )

                if db_chart:
                    print(f"Chart '{chart_code}' already exists in database")
                else:
                    chart = Chart(
                        name=chart_name, code=chart_code, dice=chart_dice
                    )
                    print('Creating Chart:', f"'{chart.name}'...")

                    db.add(chart)
                    db.commit()
                    db.refresh(chart)

                    print(
                        'Chart created successfully!',
                        f"Name: '{chart.name}',",
                        f'Code: {chart.code},',
                        f'Dice: {chart.dice}',
                        '\n',
                    )
    except Exception as e:
        raise e('Some error occurred when operating database')


@app.command()
def populate_entries():
    """Read information from 'app/assets/entries.csv'
    and push them into database"""
    entries_filepath = os.path.join(ASSETS_FOLDER, ENTRIES_FILENAME)

    # inicializar db
    db = next(get_db())

    try:
        with open(entries_filepath, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            # pular header
            next(reader)

            for entry_row in reader:
                entry_chart = entry_row[0]
                entry_result = entry_row[1]
                entry_text = entry_row[2]

                db_chart = (
                    db.query(Chart).filter(Chart.code == entry_chart).first()
                )

                if not db_chart:
                    raise Exception(
                        f"'{entry_chart}' does not exist in database"
                    )

                db_entry = (
                    db.query(Entry, Chart)
                    .join(Chart)
                    .filter(
                        Entry.result == entry_result, Chart.code == entry_chart
                    )
                    .first()
                )

                if db_entry:
                    entry = db_entry._tuple()[0].text
                    print(
                        f"'{entry}' in chart '{entry_chart}' already exists in database"
                    )
                else:
                    entry = Entry(
                        text=entry_text,
                        result=entry_result,
                        chart_uuid=db_chart.uuid,
                    )
                    print('Creating Entry:', f"'{entry.text}'...")

                    db.add(entry)
                    db.commit()
                    db.refresh(entry)

                    print(
                        'Entry created successfully!',
                        f'Chart: {db_chart.code},',
                        f'Result: {entry.result},',
                        f"Text: '{entry.text}'",
                        '\n',
                    )
    except Exception as e:
        raise e


if __name__ == '__main__':
    app()
