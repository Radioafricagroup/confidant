from flask.ext.script import Manager

from confidant import app
from confidant.scripts.utils import ManageGrants
from confidant.scripts.utils import RevokeGrants
from confidant.scripts.utils import CreateDynamoTables
from confidant.scripts.bootstrap import GenerateSecretsBootstrap
from confidant.scripts.bootstrap import DecryptSecretsBootstrap
from confidant.scripts.migrate import (
    MigrateBlindCredentialSetAttribute,
    MigrateServiceSetAttribute,
)
from confidant.scripts.migrate_bool import MigrateBooleanAttribute

manager = Manager(app.app)

# Ensure KMS grants are setup for services
manager.add_command("manage_kms_auth_grants", ManageGrants)

# Revoke all KMS grants
manager.add_command("revoke_all_kms_auth_grants", RevokeGrants)

# Generate encrypted blob from a file
manager.add_command("generate_secrets_bootstrap", GenerateSecretsBootstrap)

# Show the YAML formatted secrets_bootstrap in a decrypted form
manager.add_command("decrypt_secrets_bootstrap", DecryptSecretsBootstrap)

# Create dynamodb tables
manager.add_command("create_dynamodb_tables", CreateDynamoTables)

# Migration scripts
manager.add_command("migrate_blind_cred_set_attribute",
                    MigrateBlindCredentialSetAttribute)
manager.add_command("migrate_service_set_attribute",
                    MigrateServiceSetAttribute)
manager.add_command("migrate_boolean_attribute",
                    MigrateBooleanAttribute)


def main():
    manager.run()
