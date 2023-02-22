"""Read .env file"""
import environ  # type: ignore

env = environ.Env(
    DEBUG=(bool, False),
    CI=(bool, False),
)

environ.Env.read_env("/src/.env")  # reading .env file

__all__ = [
    env,
]
