"""
All of the stigs, well not all of them yet
"""

from dataclasses import dataclass
from typing import Callable, Union

# List of all stigs
STIGS = list()

@dataclass
class STIG():
    """
    Represents a stig.

    :param uuid: A unique, standard id for the rule
    :param description: What does this rule do
    :param command: The command to make the file changes
    :param path: The path to seal
    :param function: The or a function to make the file changes
    """
    uuid: str
    description: str
    command: str
    path: str
    function: Union[Callable, None] = None

def register_stig(**kargs) -> STIG:
    """
    A wrapper method to reigister stigs

    :param kargs: args to pass to STIG
    :return: the new stig
    """
    tmp = STIG(**kargs)
    STIGS.append(tmp)
    return tmp

register_stig(uuid="SRG-OS-000480-GPOS-00227",
              description=(
                  "Ubuntu operating systems booted with a BIOS must require authentication upon"
                  " booting into single-user and maintenance modes."
                  ),
              command=(
                  't = "$(grub-mkpasswd-pbkdf2)" &&'
                  'sudo sed -i \'$i set superusers=\"root\"\npassword_pbkdf2 root $t\' /etc/grub.d/40_custom &&'
                  'sudo sed -i -E \'s/^CLASS="[^"]*/&; --unrestricted/\' /etc/grub.d/10_linux &&'
                  'update-grub'
                  ),
              path="/etc/grub.d"
              )
register_stig(uuid="SRG-OS-000080-GPOS-00048",
              description=(
                  "Ubuntu operating systems booted with United Extensible Firmware Interface (UEFI)"
                  " implemented must require authentication upon booting into single-user mode and"
                  " maintenance."
                  ),
              command=(
                  't = "$(grub-mkpasswd-pbkdf2)" &&'
                  'sudo sed -i \'$i set superusers=\"root\"\npassword_pbkdf2 root $t\' /etc/grub.d/40_custom &&'
                  'sudo sed -i -E \'s/^CLASS="[^"]*/&; --unrestricted/\' /etc/grub.d/10_linux &&'
                  'grub-mkconfig -o /boot/efi/EFI/ubuntu/grub.cfg'
                  ),
              path="/etc/grub.d"
              )
register_stig(uuid="SRG-OS-000254-GPOS-00095",
              description=(
                  "The Ubuntu operating system must initiate session audits at system startup."
                  ),
              command=(
                  '# not implemented'
                  ),
              path=""
              )
register_stig(uuid="SRG-OS-000185-GPOS-00079",
              description=(
                  "Ubuntu operating systems handling data requiring data at rest protections must"
                  " employ cryptographic mechanisms to prevent unauthorized disclosure and "
                  " modification of the information at rest."
                  ),
              command=(
                  '# not implemented'
                  ),
              path=""
              )
register_stig(uuid="SRG-OS-000478-GPOS-00223",
              description=(
                  "The Ubuntu operating system must implement NIST FIPS-validated cryptography to"
                  " protect classified information and for the following: to provision digital"
                  " signatures, to generate cryptographic hashes, and to protect unclassified"
                  " information requiring confidentiality and cryptographic protection in accordance"
                  " with applicable federal laws, Executive Orders, directives, policies, regulations,"
                  " and standards."
                  ),
              command=(
                  '# not implemented'
                  ),
              path=""
              )
register_stig(uuid="SRG-OS-000343-GPOS-00134",
              description=(
                  "The Ubuntu operating system must immediately notify the SA and ISSO (at a"
                  " minimum) when allocated audit record storage volume reaches 75% of the repository"
                  " maximum audit record storage capacity."
                  ),
              command=(
                  '# not implemented'
                  ),
              path=""
              )
register_stig(uuid="SRG-OS-000479-GPOS-00224",
              description=(
                  "The Ubuntu operating system audit event multiplexor must be configured to"
                  " off-load audit logs onto a different system in real time, if the system is"
                  " interconnected."
                  ),
              command=(
                  'sudo apt-get install audispd-plugins -y &&'
                  'sudo sed -i -E \'s/active\s*=\s*no/active = yes/\' /etc/audisp/plugins.d/au-remote.conf &&'
                  #'sudo sed -i -E \'s/(remote_server\s*=).*/\1 {AS_SERVER};/\''
                  ),
              path="/etc/audisp/plugins.d/au-remote.conf"
              )
register_stig(uuid="SRG-OS-000479-GPOS-00224",
              description=(
                  "The Ubuntu operating system must have a crontab script running weekly to off-load"
                  " audit events of standalone systems."
                  ),
              command=(
                  '# not implemented'
                  ),
              path=""
              )
register_stig(uuid="SRG-OS-000366-GPOS-00153",
              description=(
                  "Advance package Tool (APT) must be configured to prevent the installation of"
                  " patches, service packs, device drivers, or Ubuntu operating system components"
                  " without verification they have been digitally signed using a certificate that is"
                  " recognized and approved by the organization."
                  ),
              command=(
                  '# not implemented'
                  ),
              path=""
              )
register_stig(uuid="SRG-OS-000437-GPOS-00194",
              description=(
                  "The Ubuntu operating system must be configured so that Advance package Tool (APT)"
                  " removes all software components after updated versions have been installed."
                  ),
              command=(
                  'echo "Unattended-Upgrade::Remove-Unused-Dependencies \'true\';" > /etc/apt/apt.conf.d/50unattended-upgrades &&'
                  'echo "Unattended-Upgrade::Remove-Unused-Kernel-Packages \'true\';" > /etc/apt/apt.conf.d/50unattended-upgrades'
                  ),
              path="/etc/apt/apt.conf.d/50unattended-upgrades"
              )
register_stig(uuid="SRG-OS-000095-GPOS-00049",
              description=(
                  "The Ubuntu operating system must not have the Network Information Service (NIS)"
                  " package installed."
                  ),
              command=(
                  'sudo apt-get remove nis'
                  ),
              path="/usr/bin"
              )
register_stig(uuid="SRG-OS-000095-GPOS-00049",
              description=(
                  "The Ubuntu operating system must not have the rsh-server package installed."
                  ),
              command=(
                  'sudo apt-get remove rsh-server'
                  ),
              path="/usr/bin"
              )
register_stig(uuid="SRG-OS-000191-GPOS-00080",
              description=(
                  "The Ubuntu operating system must deploy Endpoint Security for Linux Threat"
                  " Prevention (ENSLTP)."
                  ),
              command=(
                  '# not implemented'
                  ),
              path=""
              )
register_stig(uuid="SRG-OS-000269-GPOS-00103",
              description=(
                  "The Ubuntu operating system must be configured to preserve log records from"
                  " failure events."
                  ),
              command=(
                  'sudo apt-get install rsyslog &&'
                  'sudo systemctl enable rsyslog'
                  ),
              path="/usr/bin"
              )
register_stig(uuid="SRG-OS-000297-GPOS-00115",
              description=(
                  "The Ubuntu operating system must have an application firewall installed in order"
                  " to control remote access methods."
                  ),
              command=(
                  'sudo apt-get install ufw'
                  ),
              path="/usr/bin"
              )
register_stig(uuid="SRG-OS-000342-GPOS-00133",
              description=(
                  "The Ubuntu operating system audit event multiplexor must be configured to"
                  " off-load audit logs onto a different system or storage media from the system being"
                  " audited."
                  ),
              command=(
                  'sudo sed -i -E \'s/active\s*=\s*no/active = yes/\' /etc/audisp/plugins.d/au-remote.conf &&'
                  #'sudo sed -i -E \'s/(remote_server\s*=).*/\1 &lt;remote addr&gt;/\''
                  ),
              path="/etc/audisp/plugins.d/au-remote.conf"
              )
register_stig(uuid="SRG-OS-000383-GPOS-00166",
              description=(
                  "The Ubuntu operating system must be configured such that Pluggable Authentication"
                  " Module (PAM) prohibits the use of cached authentications after one day."
                  ),
              command=(
                  '# not implemented'
                  ),
              path=""
              )
