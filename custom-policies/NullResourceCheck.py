from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class NullResourceCheck(BaseResourceCheck):
    def __init__(self) -> None:
        name = 'Null resource is forbidden'
        id = "CUSTOM_NO_NULL_RESOURCE"
        supported_data = ["null_resource"]
        categories = [CheckCategories.APPLICATION_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_data)

    def scan_resource_conf(self, conf) -> CheckResult:
        """ 
            validates iam policy document 
            https://learn.hashicorp.com/terraform/aws/iam-policy 
        :param conf: aws_kms_key configuration 
        :return: <CheckResult> 
        """
        if self.entity_type == "null_resource":
            return CheckResult.FAILED

        return CheckResult.PASSED


check = NullResourceCheck()
