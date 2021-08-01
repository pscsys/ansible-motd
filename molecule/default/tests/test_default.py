import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file, content', [

  ("/etc/motd", "This system is managed by Ansible"),
  ("/etc/issue", "This system is managed by Ansible"),
  ("/etc/issue.net", "This system is managed by Ansible")

])
def test_files(host, file, content):
    file = host.file(file)

    assert file.exists
    assert file.contains(content)
