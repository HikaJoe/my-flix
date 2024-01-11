#provider
provider "aws" {
  region = "us-east-1"
}

#allow ssh connection
resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"
  vpc_id      = "vpc-08769d590e43c099d"

  ingress {
    description = "SSH from VPC"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "ec2_instance" {
  count = 3

  ami           = "ami-0c94855ba95c71c99"
  instance_type = "t2.micro"
  tags = {
    Name = "${element(["jenkins", "login", "videos"], count.index)}"
  }

  root_block_device {
    volume_size = 20
  }
}
