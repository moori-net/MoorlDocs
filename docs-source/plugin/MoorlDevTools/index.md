# Developer tools

## Most common commands

```ruby
# Create migration files based on EntityDefinitions - Please do not forget to download the Migration directory from deployment server!
bin/console mdt:migration:create MoorlPlugin -m dry|live|file|cleanup -a

# Install single Plugin or all with dependencies
bin/console mdt:plugin:install MoorlPlugin|all

# Uninstall single Plugin or all with dependencies
bin/console mdt:plugin:uninstall MoorlPlugin|all

# Update single Plugin or all with dependencies
bin/console mdt:plugin:update MoorlPlugin|all

# Demo install single Plugin or all with dependencies
bin/console mdt:demo:install MoorlPlugin|all -r
```
