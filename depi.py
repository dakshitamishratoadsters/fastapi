from typing import Annotated
from fastapi import Cookie, Depends ,FastAPI

app =FastAPI(
    title="dependency injection "
)

async def common_parameters(q:str|None =None,skip:int=0,limit:int=100):
    print("common parameter calles ")
    return{"q":q,"skip":skip,"limit":limit}

@app.get("/items/")
async def read_items(commons:Annotated[dict ,Depends(common_parameters)]):
    print("read items called")
    return commons

@app.get("/users/")
async def read_users(commons: Annotated[dict ,Depends(common_parameters)]):
    print("read_users_called")
    return commons


def query_extractor(q:str|None =None):
    print("query extractor called")
    return q



def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[str | None, Cookie()] = None,
):
    if not q:
        return last_query
    return q


@app.get("/itemss/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],):
    print("read_query called")
    return {"q_or_cookie": query_or_default}


