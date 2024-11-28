from airflow.plugins_manager import AirflowPlugin
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.exceptions import AirflowException

class CustomOperator(BaseOperator):
    @apply_defaults
    def __init__(self, custom_message: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_message = custom_message

    def execute(self, context):
        if not self.custom_message:
            raise AirflowException("Custom message is missing!")
        self.log.info(f"Custom Message: {self.custom_message}")
        return self.custom_message

# Plugin class to register custom operator
class CustomAirflowPlugin(AirflowPlugin):
    name = "custom_plugin"
    operators = [CustomOperator]
