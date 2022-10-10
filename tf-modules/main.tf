provider "aws" {
    region = "us-east-1"
}
resource "aws_instance" "vm" {
    ami           = ""
    subnet_id     = ""
    instance_type = "t3.micro"
    tags = {
        Name = "my-first-tf-node"
    }
}