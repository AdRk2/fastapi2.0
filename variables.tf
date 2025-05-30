//--------------Ressource group  ----------//
variable "resource_group_location" {
  type        = string
  default     = "Japan East"
  description = "Location of the resource group."
}


variable "resource_group_name" {
  type    = string
  default = "adam-iac-experiments"
}

//--------------Workspace  ----------//

variable "workspace_group_name" {
  type    = string
  default = "log-workspace-app-environnment"
}

variable "sku" {
  type    = string
  default = "PerGB2018"
}

variable "retention_in_days" {
  type    = number
  default = "30"
}

variable "destination" {
  type    = string
  default = "log-analytics-container-environnment-app"
}

//---------Container Environnment App ----//
variable "container_environnment_app_name" {
  type    = string
  default = "terraform-environnment"
}


//------------Vnet-----------------------//
variable "vnet_name" {
  default = "vnet-terraform"
  type    = string
}
variable "vnet_address_space" {
  type    = list(string)
  default = ["10.0.0.0/16"]
}

variable "vnet_dns_space" {
  type    = list(string)
  default = ["10.0.0.4", "10.0.0.5"]
}


//-----------Subnet----------//

variable "subnet_name" {
  type    = string
  default = "subnet-app-envrionnment"
}

variable "subnet_address_prefix" {
  type    = list(string)
  default = ["10.0.1.0/24"]
}

//--Container Registry--------//

variable "azurerm_container_registry" {
  type    = string
  default = "registryiac"
}
