from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    gemini_api_key: str
    embedding_model: str = "intfloat/multilingual-e5-base"
    qdrant_path: str = "./storage/qdrant"
    qdrant_collection: str = "thai_company_docs"
    top_k: int = 5

    class Config:
        env_file = ".env"

settings = Settings()