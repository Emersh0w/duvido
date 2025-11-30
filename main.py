from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import random

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None



@app.get("/questions")
def read_root():
    return (
    supabase.table("questions")
    .select("question, answer, source, topic")
    .eq("id",random.randint(13,62))
    .limit(1)
    .execute()
    )


@app.post("/questions")
def read_world(question: str, answer: str):
    return (
        supabase.table("questions")
        .insert({"question": question, "answer": answer})
        .execute()
        )


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

