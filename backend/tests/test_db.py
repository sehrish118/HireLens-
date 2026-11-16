from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from app.core.config import get_settings

settings = get_settings()


async def test_test_database_has_pgvector():
    engine = create_async_engine(settings.test_database_url)
    async with engine.connect() as conn:
        result = await conn.execute(
            text("SELECT extname FROM pg_extension where extname = 'vector'")
        )
        assert result.scalar() == "vector"
    await engine.dispose()
