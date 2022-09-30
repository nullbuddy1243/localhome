echo ".bashrc"

alias rebashrc="source /Users/human/.bashrc"

# exa ls replacement, very pretty

alias ll="exa -lah"

# exa tree depth 2 long out as lll
alias lll="exa --tree --level=2 --long"

alias shrug="echo '¯\_(ツ)_/¯' " 

# icat prints img in terminal
alias icat="kitty +kitten icat"

# diceware alias  
alias diceware_="diceware | python3 /Users/human/GRIND/LAB/localhome/diceware_string_fixer.py '_'"


# python stuff

alias python="python3"

alias ppypath="python3 -c 'import sys; from pprint import pprint as pp; pp(sys.path)'"


# node stuff

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
echo ""

# check nest for upgrades 

alias nestupgrade='npx npm-check-updates "/nestjs*/" -u'


# to remove, ls colors stuff

# export LS_COLORS='*.env=31:*.git=31:*.gitignore=91:*.js=94:*.ts=36:*.py=92:*.png=96:*.jpg=96:*.jpeg=96:*.gif=96:*.json=33:*.yaml=33:*.wav=95:*.mp3=95:*.avi=95:*.mp4=95:*.md=33:*.txt=33:';



# ---- end localhome
# ---- ---- remove / update below... reorganize it...

alias marketback1SSH="ssh -i ~/.ssh/id_ed25519 root@143.198.49.202"

export OS_API="1379b4994aa64cd09752e705f3f263c0"

alias urbit=/Users/human/urbit/urbit

export PATH="$PATH:/Users/human/.foundry/bin"

alias ipfs=/Users/human/ipfs/go-ipfs/ipfs

export PATH=/opt/local:$PATH

export PATH=/Users/human/.rustup:$PATH
. "$HOME/.cargo/env"

export PKG_CONFIG_PATH=/opt/local/lib/pkgconfig:/usr/local/lib:/opt/homebrew/Cellar/pango/1.50.9/lib:/opt/homebrew/Cellar/pango/1.50.9/lib/pkgconfig/:/opt/homebrew/Cellar/harfbuzz/5.1.0/lib/pkgconfig/

export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/opt/homebrew/Cellar/graphite2/1.3.14/lib/pkgconfig/

export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/opt/homebrew/Cellar/fribidi/1.0.12/lib/pkgconfig/

# -- end 
fortune
# sinprint
python3 /Users/human/GRIND/LAB/localhome/sinprint.py
