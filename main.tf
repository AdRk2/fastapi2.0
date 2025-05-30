//container app environnment

resource "azurerm_log_analytics_workspace" "log_environnment" {
  name                = var.workspace_group_name
  location            = var.resource_group_location
  resource_group_name = var.resource_group_name
  sku                 = var.sku
  retention_in_days   = var.retention_in_days
}

resource "azurerm_container_app_environment" "container_app_environnment" {
  name                       = var.container_environnment_app_name
  location                   = var.resource_group_location
  resource_group_name        = var.resource_group_name
  logs_destination           = "log-analytics"
  log_analytics_workspace_id = azurerm_log_analytics_workspace.log_environnment.id
}

resource "azurerm_user_assigned_identity" "iac" {
  resource_group_name = var.resource_group_name
  location            = var.resource_group_location

  name = "registry-adbz-iac"
}

resource "azurerm_virtual_network" "vnet_terraform" {
  name                = var.vnet_name
  location            = var.resource_group_location
  resource_group_name = var.resource_group_name
  address_space       = var.vnet_address_space
  dns_servers         = var.vnet_dns_space
}

resource "azurerm_subnet" "app" {
  name                 = "service-subnet-registry"
  resource_group_name  = var.resource_group_name
  virtual_network_name = azurerm_virtual_network.vnet_terraform.name
  address_prefixes     = var.subnet_address_prefix
}
resource "azurerm_subnet" "iac" {

  name                 = "service-subnet-registry"
  resource_group_name  = var.resource_group_name
  virtual_network_name = azurerm_virtual_network.vnet_terraform.name
  address_prefixes     = ["10.0.2.0/24"]

  delegation {
    name = "subnetjoins"
    service_delegation {
      name = "Microsoft.DBforPostgreSQL/flexibleServers"
      actions = [
        "Microsoft.Network/virtualNetworks/subnets/join/action",
      ]
    }
  }

}

resource "azurerm_role_assignment" "acr_pull" {
  scope                = azurerm_container_app.api.id
  role_definition_name = "AcrPull"
  principal_id         = azurerm_user_assigned_identity.iac.id
}



resource "azurerm_container_registry" "registryiac" {
  name                = var.azurerm_container_registry
  resource_group_name = var.resource_group_name
  location            = var.resource_group_location
  sku                 = "Premium"
  admin_enabled       = true

  identity {
    type = "UserAssigned"
    identity_ids = [
      azurerm_user_assigned_identity.iac.id
    ]
  }

}

//container app

resource "azurerm_container_app" "view" {
  name                         = "fastapi-pgadmin"
  container_app_environment_id = azurerm_container_app_environment.container_app_environnment.id
  resource_group_name          = var.resource_group_name
  revision_mode                = "Single"

  ingress {
    traffic_weight {
      latest_revision = true
      percentage      = 100
      revision_suffix = "v1"
    }

    external_enabled = true
    ip_security_restriction {
      action           = "Allow"
      ip_address_range = "133.237.7.64/27"
      name             = "Rakuten"
    }

    ip_security_restriction {
      action           = "Allow"
      ip_address_range = "133.237.7.127/32"
      name             = "Rakuten"
    }

    ip_security_restriction {
      action           = "Allow"
      ip_address_range = "133.237.92.64/27"
      name             = "Rakuten"
    }

    ip_security_restriction {
      action           = "Allow"
      ip_address_range = "133.237.92.10"
      name             = "Rakuten"
    }

    ip_security_restriction {
      action           = "Allow"
      ip_address_range = "162.10.0.0/17"
      name             = "Netskope"
    }

    ip_security_restriction {
      action           = "Allow"
      ip_address_range = "163.116.128.0/17"
      name             = "Netskope"
    }

    target_port = 5000
  }

  template {
    container {
      name   = "fastapi-pgadmin"
      image  = "docker.io/dpage/pgadmin4:latest"
      cpu    = 0.5
      memory = "1Gi"
    }
  }
}


resource "azurerm_container_app" "api" {
  name                         = "restendpointfastapi-python"
  container_app_environment_id = azurerm_container_app_environment.container_app_environnment.id
  resource_group_name          = var.resource_group_name
  revision_mode                = "Single"

  registry {
    server   = "registryiac.azurecr.io"
    identity = azurerm_user_assigned_identity.iac.id
  }

  ingress {
    traffic_weight {
      latest_revision = true
      percentage      = 100
      revision_suffix = "v1"
    }

    external_enabled = true
    ip_security_restriction {
      action           = "Allow"
      ip_address_range = "133.237.7.64/27"
      name             = "Rakuten"
    }

    ip_security_restriction {
      action           = "Allow"
      ip_address_range = "133.237.7.127/32"
      name             = "Rakuten"
    }

    ip_security_restriction {
      action           = "Allow"
      ip_address_range = "133.237.92.64/27"
      name             = "Rakuten"
    }

    ip_security_restriction {
      action           = "Allow"
      ip_address_range = "133.237.92.10"
      name             = "Rakuten"
    }

    ip_security_restriction {
      action           = "Allow"
      ip_address_range = "162.10.0.0/17"
      name             = "Netskope"
    }

    ip_security_restriction {
      action           = "Allow"
      ip_address_range = "163.116.128.0/17"
      name             = "Netskope"
    }

    target_port = 8000
  }

  template {
    container {
      name   = "restendpointfastapi-python"
      image  = "registryiac.azurecr.io"
      cpu    = 0.5
      memory = "1Gi"
    }
  }
}


resource "azurerm_private_dns_zone" "registry" {
  name                = "privatelink.azurecr.io"
  resource_group_name = var.resource_group_name
}

resource "azurerm_private_dns_zone_virtual_network_link" "registry" {
  name                  = "private-link-iac001"
  resource_group_name   = var.resource_group_name
  private_dns_zone_name = azurerm_private_dns_zone.registry.name
  virtual_network_id    = azurerm_virtual_network.vnet_terraform.id
}

//Postgres service
resource "azurerm_private_dns_zone" "iac" {
  name                = "privatelink.postgres.database.azure.com"
  resource_group_name = var.resource_group_name
}

resource "azurerm_private_dns_zone_virtual_network_link" "iac" {
  name                  = "postgresVnetZone.com"
  private_dns_zone_name = azurerm_private_dns_zone.iac.name
  virtual_network_id    = azurerm_virtual_network.vnet_terraform.id
  resource_group_name   = var.resource_group_name
}

resource "azurerm_postgresql_flexible_server" "example" {
  name                          = "psqlflexibleserveriacadbz"
  resource_group_name           = var.resource_group_name
  location                      = var.resource_group_location
  version                       = "12"
  delegated_subnet_id           = azurerm_subnet.iac.id
  private_dns_zone_id           = azurerm_private_dns_zone.iac.id
  public_network_access_enabled = false
  administrator_login           = "devadmin"
  administrator_password        = "ijustwanttolog2@"
  zone                          = "1"

  storage_mb   = 32768
  storage_tier = "P4"
  sku_name     = "B_Standard_B1ms"
  depends_on   = [azurerm_private_dns_zone_virtual_network_link.iac]

}
