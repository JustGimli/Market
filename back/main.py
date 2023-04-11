from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from routes.v1 import home

app = FastAPI(
    title='testapi',
    debug=True
)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(home.router)
