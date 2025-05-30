//block of container app environnment
output "azurerm_container_app_environment" {
  value = azurerm_container_app_environment.container_app_environnment.id
}

output "azurerm_container_registry" {
  value = azurerm_container_registry.registryiac.name
}