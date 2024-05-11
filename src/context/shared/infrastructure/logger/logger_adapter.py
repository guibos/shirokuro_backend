import logging
from contextvars import ContextVar
from typing import Optional, Dict, Any

from context.shared.infrastructure.logger.logger_context_data import LoggerContextData

from context.shared.domain.value_types.request_metadata.request_id import RequestId


class CustomAdapter(logging.LoggerAdapter):
    """
    This example adapter expects the passed in dict-like object to have a
    'connid' key, whose value in brackets is prepended to the log message.
    """
    def __init__(self, logger: logging.Logger, extra: Optional[Dict[str, Any]] = None):
        super().__init__(logger, extra_dict)
        self._request_id = ContextVar('var', default=RequestId('00000000-0000-0000-0000-000000000000'))

    def process(self, msg, kwargs):
        return '[%s] %s' % (self.extra['connid'], msg), kwargs

    @property
    def request_id(self):
        rfe
