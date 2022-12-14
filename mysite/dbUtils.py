# install : pip install psycopg2-binary
import psycopg2
import psycopg2.extras

def get_conn():
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="postgres", port=5432)
    return conn

def get_data():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    query = '''
    
    '''
    cur.execute(query)

    results = cur.fetchall()

    return results

if __name__ == '__main__':
    pass
