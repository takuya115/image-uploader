import os
import shutil
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/picture/")
async def upload_picture(file: UploadFile = File(...)):
    if file:
        # 保存先のファイルパスを設定
        saved_file = os.path.join("./images", file.filename)
        # ファイルの保存
        with open(saved_file, "wb+") as sf:
            shutil.copyfileobj(file.file, sf)
        return {"file_name": file.filename}
    else:
        return {"file_name": None}
