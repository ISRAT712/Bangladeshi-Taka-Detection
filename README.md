# Bangladeshi Taka Note Detection API

## Project Overview

This project detects Bangladeshi banknotes using a trained YOLOv11 model.

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run API

```bash
uvicorn app:app --reload
```

Open

http://127.0.0.1:8000/docs

---

## API Endpoint

POST

```
/predict
```

Upload a JPG or PNG image.

Example Response

```json
{
    "filename":"test.jpg",
    "predictions":[
        {
            "class":"500 Taka",
            "confidence":0.98,
            "bbox":[45,66,301,242]
        }
    ]
}
```

---

## Docker

Build

```bash
docker build -t taka-detector .
```

Run

```bash
docker run -p 8000:8000 taka-detector
```

Open

```
http://localhost:8000/docs
```