import pytest

from utilities.custom_logger import Log_Maker


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class BaseTest:
    logger= Log_Maker.log_gen()