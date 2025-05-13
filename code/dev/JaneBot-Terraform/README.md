
![img](https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Terraform_Logo.svg/2560px-Terraform_Logo.svg.png)

## Terraform setup for JaneBot

### Initial Setup

Make sure you have [Terraform](https://developer.hashicorp.com/terraform/install) installed.

After that, clone the repository then run

```
terraform init
```

*Note:* You wont be able to make use of this repository if you don't have the `secrets.tfvars`.

If you __do__ have it...

```
terraform plan --var-file=secrets.tfvars  ## Check the changes to be made
terraform apply --var-file=secrets.tfvars ## Apply the changes
```

#### Author

[@RJ Paraiso](https://github.com/thisis-rjp/)