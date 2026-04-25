import joblib
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

model = joblib.load("model.pkl")

app = FastAPI(title="Simple Linear Regression")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"request": request}
    )


@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request, x: float = Form(...)):

    input_data = [[x]]
    output = model.predict(input_data)

    try:
        prediction = output[0][0]
    except:
        prediction = output[0]

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "request": request,
            "x": x,
            "prediction": prediction
        }
    )