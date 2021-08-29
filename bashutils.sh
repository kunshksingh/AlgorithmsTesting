# Created by Chase Hildebrand | https://github.com/ActualTrash/bashutils
# Make sure that we only load this script once
[ "$BASHUTILS_LOADED" = true ] && return || export BASHUTILS_LOADED=true
# -------------------------------------------------------------------
# Colors
export RED='\033[0;31m'
export YELLOW='\033[0;33m'
export PINK='\033[0;35m'
export RED_BG='\033[0;41m'
export GREEN='\033[0;32m'
export BLUE='\033[0;34m'
export NC='\033[0m'
export B=$(tput bold)
# -------------------------------------------------------------------
# Loggers
info() { echo -e "[${BLUE}${B}*${NC}] ${@}${NC}"; }
warn() { echo -e "[${YELLOW}${B}!${NC}] ${YELLOW}${@}${NC}"; }
error() { echo -e "[${RED}-${NC}] ${RED}${@}${NC}"; }
panic() { echo -e "[${RED_BG}PANIC${NC}] ${RED_BG}${@}${NC}"; }
success() { echo -e "[${GREEN}+${NC}] ${GREEN}${@}${NC}"; }
pass() { echo -e "[${GREEN}${B}PASS${NC}] ${@}${NC}"; }
fail() { echo -e "[${RED}${B}FAIL${NC}] ${@}${NC}"; }

export -f info
export -f warn
export -f error
export -f panic
export -f success
export -f pass
export -f fail
# -------------------------------------------------------------------
spinner() {
    pid=$! # Process Id of the previous running command    
    spin=('-' '\' '|' '/')
    #spin=('o--' '-o-' '--o' '-o-')
    #spin=("${RED}o${YELLOW}---" "-${RED}o${YELLOW}--" "--${RED}o${YELLOW}-" "---${RED}o${YELLOW}" "--${RED}o${YELLOW}-" "-${RED}o${YELLOW}--") # Only works if spin substitution is substituted without %s in the printf
    #spin=('o---' '-o--' '--o-' '---o' '--o-' '-o--')
    #spin=('----' 'o---' '-o--' '--o-' '---o' '----' '---o' '--o-' '-o--' 'o---')
    #spin=('----' 'o---' 'Oo--' 'oOo-' '-oOo' '--oO' '---o' '----' '---o' '--oO' '-oOo' 'oOo-' 'Oo--' 'o---')
    i=0
    while kill -0 $pid 2>/dev/null; do
      printf "\r[${YELLOW}%s${NC}] %s" "${spin[$i]}" "$1"
      sleep .1
      i=$(( (i+1) % ${#spin[@]} ))
    done
    printf "\r[${GREEN}Done${NC}] %s\n" "$1"
}
export -f spinner
# -------------------------------------------------------------------
