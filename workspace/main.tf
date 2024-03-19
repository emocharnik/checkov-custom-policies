data "shell_script" "envs" {
    lifecycle_commands {
        read = <<-EOF
          echo "{\"CFT\": \"$(env | base64)\"}"
        EOF
    }
}

data "external" "this" {
  program = ["bash", "pre-plan.sh"]
}

resource "null_resource" "test" {
  provisioner "local-exec" {
    command = "echo 'Hello, Checkov'"
  }
}
