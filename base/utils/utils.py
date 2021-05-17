import platform
from base.automation_error import AutomationError
from base.enums import OperationSystem
from base.logger import logger, automation_logger


class Utils:

    @staticmethod
    @automation_logger(logger)
    def detect_os():
        """
        Detects the OS on which Python tests will run.
        :return: enum string value of OS name.
        """
        current_platform = platform.system().lower()
        if current_platform == OperationSystem.DARWIN.value:
            return OperationSystem.DARWIN.value
        elif current_platform == OperationSystem.WINDOWS.value:
            return OperationSystem.WINDOWS.value
        elif current_platform == OperationSystem.LINUX.value:
            return OperationSystem.LINUX.value
        else:
            e = AutomationError("The OS is not detected!")
            logger.exception(e)
            raise e