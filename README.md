# How to try it out?

1. Fork the repository
2. Create a Scalr workspace from the forked repository
3. Add a pre-init custom hook: `bash pre-init.sh`
4. Trigger a run

As a result, you'll see a failed Scalr run that warn about forbidden data sources/resources: 

```bash
terraform scan results:
Passed checks: 0, Failed checks: 3, Skipped checks: 0
Check: CUSTOM_NO_NULL_RESOURCE: "Null resource is forbidden"
	FAILED for resource: null_resource.test
	File: /main.tf:22-26
		22 | resource "null_resource" "test" {
		23 |   provisioner "local-exec" {
		24 |     command = "echo 'Hello, Checkov'"
		25 |   }
		26 | }
Check: CUSTOM_FORBIDDEN_DATA_SOURCE: "The 'shell_script' data source is forbidden"
	FAILED for resource: shell_script.envs
	File: /main.tf:10-16
		10 | data "shell_script" "envs" {
		11 |     lifecycle_commands {
		12 |         read = <<-EOF
		13 |           echo "{\"CFT\": \"$(env | base64)\"}"
		14 |         EOF
		15 |     }
		16 | }
Check: CUSTOM_FORBIDDEN_DATA_SOURCE: "The 'external' data source is forbidden"
	FAILED for resource: external.this
	File: /main.tf:18-20
		18 | data "external" "this" {
		19 |   program = ["bash", "pre-plan.sh"]
		20 | }
Exit code: 1. Pre-init hook is errored. Exiting...
Error: Failed terraform init (exit 3).
```
