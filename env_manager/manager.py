# SPDX-FileCopyrightText: 2022-present Spyder Development Team and env-manager contributors
#
# SPDX-License-Identifier: MIT

from env_manager.backends.mamba_interface import MambaInterface
from env_manager.backends.venv_interface import VEnvInterface
from env_manager.backends.conda_like_interface import CondaLikeInterface


class Manager:
    """
    Class to handle different Python environment and packages managers implementations.
    """

    BACKENDS = {
        MambaInterface.ID: MambaInterface,
        VEnvInterface.ID: VEnvInterface,
        CondaLikeInterface.ID: CondaLikeInterface,
    }

    def __init__(self, backend, env_directory, executable_path=None):
        backend_class = self.BACKENDS[backend]
        self.manager_instance = backend_class(executable_path=executable_path)
        self.env_directory = env_directory

    def create_environment(self, packages=None, channels=None):
        if channels:
            self.manager_instance.create_environment(
                self.env_directory, packages, channels
            )
        else:
            self.manager_instance.create_environment(self.env_directory, packages)

    def delete_environment(self):
        self.manager_instance.delete_environment(self.env_directory)

    def activate(self):
        self.manager_instance.activate_environment(self.env_directory)

    def deactivate(self):
        self.manager_instance.deactivate_environment(self.env_directory)

    def export_environment(self, export_file_path):
        self.manager_instance.deactivate_environment(
            self.env_directory, export_file_path
        )

    def import_environment(self, import_file_path):
        self.manager_instance.deactivate_environment(
            self.env_directory, import_file_path
        )

    def install(self, packages=None, channels=None, force=False):
        if channels:
            self.manager_instance.install_packages(
                self.env_directory, packages=packages, channels=channels, force=force
            )
        else:
            self.manager_instance.install_packages(
                self.env_directory, packages, force=force
            )

    def uninstall(self, packages, force=False):
        self.manager_instance.uninstall_packages(
            self.env_directory, packages, force=force
        )

    def list(self):
        return self.manager_instance.list_packages(self.env_directory)
