import csv
import psycopg2


def load_csv():
    try:
        conn = psycopg2.connect("host=localhost dbname=DB user=postgres password=12345")
        cur = conn.cursor()
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                cur.execute(
                    "INSERT INTO charts_vulnerabilities VALUES (%s, %s, %s, %s)",
                    row)
        conn.commit()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    load_csv()