# localhome 

configs, tools, bash stuff, random. 

[diceware thing](#diceware-string-fixer-thing)

[shrug alias](#shrug-alias)

[ppypath: pretty bash PYTHONPATH](#ppypath)

[... more](#more-whenver-i-get-around-to-it-lol)


## diceware string fixer thing 

having a CLI diceware on hand is stupidly useful for a variety of things. tbh, I end up using it multiple times a week. 

Ive used it to generate big random word lists for Lorem Ipsum type stuff, coming up with random cool name for a service, assorted generative text / ML, and ofc coming up with passwords and secrets. 

Using diceware from a CPU isn't recommended for high-security usecases, but IMO its fine to do for like, making new accounts on sites where it doesnt matter so much.

shouout to @yuvallanger OG author of the diceware rust crate. 

### why?

The rust crate i use for CLI diceware prints words with spaces between, but i want a `between_char` like_these_are_some_words in whatever casing you like.

Coulda forked and updated the diceware crate itself, still might. Wanted to make sure the script had no non-standard-lib deps, so only using stuff included with python3. 

maybe will make it a proper bash script to handle args better.  for now just quick and dirty

### howto: 

- get cli diceware from [diceware](https://crates.io/crates/diceware)
  - [shoutout to rustlang diceware author @yuvallanger](https://github.com/yuvallanger/rusty-diceware)
- make bash alias that pipes diceware into `python3 diceware_string_fixer.py`
- can include a `between_char` as first param to change whats between the words.
- source `.bashrc`
- enjoy `$ diceware_` ;)

### alias 


``` bash
alias diceware_="diceware | python3 /path/to/wherever/you/put/localhome/diceware_string_fixer.py '_'"
```


### examples:

``` bash
$ diceware | python3 diceware_string_fixer.py 
no sys.argv[1] for between_char so using default _
_ 1 2
---
input: caddie patination refracted superstition laconic stooge padlocks licensees 
 
between_char: _ 
---
caddie_patination_refracted_superstition_laconic_stooge_padlocks_licensees
--- :) ---
```

``` bash
$ diceware | python3 diceware_string_fixer.py "_"
got sys.argv[1] = _
_ 1 2
---
input: diffidently disturbed textual bracket dynamics hugeness unknowns works 
 
between_char: _ 
---
diffidently_disturbed_textual_bracket_dynamics_hugeness_unknowns_works
--- ;) ---

```

wacky mode 
``` bash
$ shrug
¯\_(ツ)_/¯

$ diceware | python3 diceware_string_fixer.py "¯\_(ツ)_/¯"
got sys.argv[1] = ¯\_(ツ)_/¯
¯\_(ツ)_/¯ 9 10
---
input: deflation iteratively backups dustmen centrifuged gullibility answered percentage 
 
between_char: ¯\_(ツ)_/¯ 
---
deflation¯\_(ツ)_/¯iteratively¯\_(ツ)_/¯backups¯\_(ツ)_/¯dustmen¯\_(ツ)_/¯centrifuged¯\_(ツ)_/¯gullibility¯\_(ツ)_/¯answered¯\_(ツ)_/¯percentage
--- ;) ---
```

## shrug alias

hate it when you need to search for the shrug emoticon string? no more!

``` bash
$ shrug
¯\_(ツ)_/¯
```

put this in `.bashrc` or wherever, then `$ source .bashrc` 

``` bash
alias shrug="echo '¯\_(ツ)_/¯' "
```


## ppypath

pretty bash PYTHONPATH 


```
alias ppypath="python3 -c 'import sys; from pprint import pprint as pp; pp(sys.path)'"
```


## more whenver i get around to it lol
