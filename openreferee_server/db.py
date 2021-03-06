from flask_sqlalchemy import SQLAlchemy

from .app import app


db = SQLAlchemy(app)
db.Model.metadata.naming_convention = {
    "fk": "fk_%(table_name)s_%(column_names)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
    "ix": "ix_%(unique_index)s%(table_name)s_%(column_names)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "uq": "uq_%(table_name)s_%(column_names)s",
    "column_names": lambda constraint, table: "_".join(
        (c if isinstance(c, str) else c.name) for c in constraint.columns
    ),
    "unique_index": lambda constraint, table: "uq_" if constraint.unique else "",
}
