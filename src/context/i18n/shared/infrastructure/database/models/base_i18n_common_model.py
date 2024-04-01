from sqlalchemy import Column, VARCHAR, ARRAY

from context.i18n.shared.infrastructure.database.models.base_i18n_model import BaseI18nModel


class BaseI18nCommonModel(BaseI18nModel):
    __abstract__ = True

    description = Column(ARRAY(VARCHAR(1)), nullable=False)
