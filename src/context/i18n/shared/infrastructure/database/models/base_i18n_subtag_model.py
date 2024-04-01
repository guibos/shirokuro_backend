from abc import abstractmethod

from sqlalchemy import Text

from context.i18n.shared.infrastructure.database.models.base_i18n_common_model import BaseI18nCommonModel


class BaseI18nSubtagModel(BaseI18nCommonModel):
    __abstract__ = True

    # @property
    # @abstractmethod
    # def subtag(self) -> Text:
    #     raise NotImplementedError
