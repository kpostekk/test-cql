from fastapi import FastAPI
from sqlite3 import connect

app = FastAPI()
db = connect('database.db')

@app.post('/exec')
def exec_any(code: str):
    return {'result': eval(code)}

@app.post('/create-cat')
def create_cat(name: str):
    cursor = db.cursor()
    cursor.execute('INSERT INTO cats (name) VALUES (?)', (name,))
    db.commit()
    return {'result': 'ok'}


@app.get('/get-cats')
def get_cats(name: str = None):
    cursor = db.cursor()
    cursor.execute('SELECT * FROM cats WHERE name LIKE ?', (name,))
    return {'result': cursor.fetchall()}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
