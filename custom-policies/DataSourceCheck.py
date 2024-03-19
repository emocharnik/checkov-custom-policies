from checkov.terraform.checks.data.base_check import BaseDataCheck
from checkov.common.models.enums import CheckResult, CheckCategories
from typing import Dict, Any, List


class DataSourceCheck(BaseDataCheck):
    def __init__(self) -> None:
        name = "The data sources is forbidden"
        id = "CUSTOM_FORBIDDEN_DATA_SOURCE"
        supported_data = ["external", "shell_script"]
        categories = [CheckCategories.APPLICATION_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_data=supported_data)

    def scan_data_conf(self,  conf: Dict[str, List[Any]]) -> CheckResult:
        """ 
        Validates if source code contains forbidden data sources
        :param conf: aws_kms_key configuration
        :return: <CheckResult> 
        """
        if self.entity_type in self.supported_data:
            self.name = f"The '{self.entity_type}' data source is forbidden"
            return CheckResult.FAILED

        return CheckResult.PASSED


check = DataSourceCheck()
