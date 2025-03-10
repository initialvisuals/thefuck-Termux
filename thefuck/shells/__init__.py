"""Package with shell specific actions, each shell class should
implement `from_shell`, `to_shell`, `app_alias`, `put_to_history` and
`get_aliases` methods.
"""
import os
from .bash import Bash
from .fish import Fish
from .generic import Generic
from .tcsh import Tcsh
from .zsh import Zsh
from .powershell import Powershell

shells = {'bash': Bash,
          'fish': Fish,
          'zsh': Zsh,
          'csh': Tcsh,
          'tcsh': Tcsh,
          'powershell': Powershell,
          'pwsh': Powershell}

def _get_shell_from_env():
    name = os.environ.get('TF_SHELL')
    if name in shells:
        return shells[name]()

def _get_shell_from_proc():
    # Use $SHELL env var or default to bash, avoiding psutil
    shell_path = os.environ.get('SHELL', '/data/data/com.termux/files/usr/bin/bash')
    shell_name = os.path.basename(shell_path)  # Extracts 'bash', 'fish', etc.
    return shells.get(shell_name, Generic)()

shell = _get_shell_from_env() or _get_shell_from_proc()
