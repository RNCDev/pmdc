import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy import create_engine

from alembic import context

# Add the project root directory to the Python path
# This allows alembic to find the app modules
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import settings and Base from your application
from app.core.config import settings
from app.db.models.base import Base # Adjust if your Base is elsewhere
# Import all models here so Base knows about them for autogenerate
from app.db.models.publisher import Publisher
from app.db.models.subscriber import Subscriber
from app.db.models.subscription import Subscription
from app.db.models.data_record import DataRecord
# from app.db.models.audit_log import AuditLog # If you have this

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Use the DATABASE_URI from your application settings
# Ensure the DATABASE_URI is set in your environment or .env file
if settings.DATABASE_URI:
    config.set_main_option("sqlalchemy.url", settings.DATABASE_URI.render_as_string(hide_password=False))
else:
    raise ValueError("DATABASE_URI not configured in settings.")

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        # include_schemas=True # Add if using multiple schemas
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # Use create_engine directly with the DATABASE_URI from settings
    # engine_from_config might not pick up the URI correctly if set programmatically
    connectable = create_engine(settings.DATABASE_URI.render_as_string(hide_password=False))

    # Original approach using engine_from_config (might work if .ini has the correct URI)
    # connectable = engine_from_config(
    #     config.get_section(config.config_ini_section, {}),
    #     prefix="sqlalchemy.",
    #     poolclass=pool.NullPool,
    # )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            # include_schemas=True # Add if using multiple schemas
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
