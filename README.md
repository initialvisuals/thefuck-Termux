# thefuck-Termux

This is a fork of [TheFuck](https://github.com/nvbn/thefuck), tweaked to run smoothly on Termux with Python 3.12+. Check the original repo at [nvbn/thefuck](https://github.com/nvbn/thefuck) for full details on what `thefuck` can do.

## What’s Changed
- Swapped out `imp` for `importlib` to work with Python 3.12.
- Ditched `psutil` in shell detection to dodge Android’s `/proc` permission issues.
- works well with Fish shell

## How to Install
```bash
pkg update && pkg install python git -y
python -m pip uninstall thefuck -y  # Clear any old version
git clone https://github.com/initialvisuals/thefuck-Termux.git
cd thefuck-Termux
python -m pip install --user .
```

## Shell Setup

Bash
```bash
echo "eval \$(thefuck --alias)" >> ~/.bashrc
source ~/.bashrc
```

Fish Shell
```bash
# Set PATH
echo "set -gx PATH ~/.local/bin \$PATH" > ~/.config/fish/config.fish
nano ~/.config/fish/functions/fuck.fish
# Paste this:
function fuck -d "Correct your previous console command"
    set -l fucked_up_command "$history[1]"
    if test -n "$fucked_up_command"
        set -l unfucked_command (env TF_ALIAS=fuck PYTHONIOENCODING=utf-8 thefuck "$fucked_up_command")
        if test -n "$unfucked_command"
            eval "$unfucked_command"
            builtin history delete --exact --case-sensitive -- "$fucked_up_command"
            builtin history merge >/dev/null 2>&1
        else
            echo "No correction found."
        end
    else
        echo "No previous command to correct."
    end
end
# Save (Ctrl+O, Enter, Ctrl+X), then:
source ~/.config/fish/config.fish
```

## How to use
```bash
fush    # Typo
fuck    # Fixes to `fish`
```
## Troubleshooting

command not found?

```bash
set -gx PATH ~/.local/bin $PATH
cd ~/thefuck-Termux && python -m pip install --user .
```

fish config errors?
```bash
grep -r "thefuck" ~/.config/fish  # Find old aliases
echo "set -gx PATH ~/.local/bin \$PATH" > ~/.config/fish/config.fish
rm -rf ~/.config/fish/functions/*  # Backup custom stuff first!
# Redo the Fish setup above
```

More Info
See nvbn/thefuck for the full scoop on thefuck’s features and rules.




