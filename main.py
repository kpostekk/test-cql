from fastapi import FastAPI

app = FastAPI()

@app.post('/exec')
def exec_any(code: str):
    return {'result': eval(code)}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
