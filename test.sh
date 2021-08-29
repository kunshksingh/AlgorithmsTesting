#!/bin/bash
source bashutils.sh

# Command line arguments
USAGE="Usage: $0 <path to binary> <module name> [-n <number>]"
HELP="$USAGE
        -n, test_number         Test number to run (optional)
	-h, --help              Display this menu
"

if [ "$#" = "0" ]; then
    error "Invalid arguments. Use $YELLOW$0 -h$RED for help"
    exit 1
fi

# Default values
test_num=-1
positional=()

# Set non-positional args and pull out positional args
while (("$#")); do
    case $1 in
	-n)
                if [ "$2" = "" ]; then
                    error "Number required with -n"
                    exit 1
                fi
		test_num=$2
		shift 2
	;;
	-h | --help | --usage) # Display the help menu
		echo "$HELP"
		exit 0
	;;
	-* | --*=) # Unsupported flags
		error "Unknown argument: $1"
            	error "Use $0 -h for the help menu"
            	exit 1
	;;
        *)
            positional+=("$1")
            shift 1
        ;;
    esac
done

if [ ${#positional[@]} != 2 ]; then
    error 'Invalid number of positional arguments'
    error "Use $0 -h for the help menu"
    exit 1
fi

mod_name="${positional[0]}"
bin_path="${positional[1]}"

info "module_name: $mod_name"
info "binary_path: $bin_path"
info "test_num: $test_num"



