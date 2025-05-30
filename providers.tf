terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.31.0"
    }
  }
}

provider "azurerm" {
  subscription_id = "ee90b384-dac9-4bcd-b7cc-5b0e0ce49994"
  features {}
}