import pulumi
from pulumi_azure import core, storage

# Create an Azure Resource Group
resource_group = core.ResourceGroup('resource_group')


account = storage.Account('storage',
                          resource_group_name=resource_group.name,
                          account_tier='Standard',
                          account_replication_type='LRS')


pulumi.export('account_name', account.name)
