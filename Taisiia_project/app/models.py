from Taisiia_project.database import db
from sqlalchemy.orm import Mapped, mapped_column


class  Product(db.Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    product: Mapped[str]
    brand: Mapped[str | int]
    color: Mapped[str]
    description: Mapped[str | None]

    def __str__(self):
        return f'{self.id} {self.product} brand:{self.brand}, color:{self.color}'