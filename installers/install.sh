#!/bin/sh

set -e

# Tells the user that the unzip tool is necessary to use this installation script
if ! command -v unzip >/dev/null; then
	echo "Error: unzip is required to install Docrunner." 1>&2
	exit 1
fi

# Decides docrunner target based on OS
if [ "$OS" = "Windows_NT" ]; then
	target="x86_64-pc-windows-msvc"
else
	case $(uname -sm) in
	"Darwin x86_64") target="x86_64-apple-darwin" ;;
	*) target="x86_64-unknown-linux-gnu" ;;
	esac
fi

# Defines the docrunner download url
if [ $# -eq 0 ]; then
	docrunner_uri="https://github.com/DudeBro249/docrunner/releases/latest/download/docrunner-${target}.zip"
else
	docrunner_uri="https://github.com/DudeBro249/docrunner/releases/download/${1}/docrunner-${target}.zip"
fi

# Defines import installation locations
docrunner_install="${DOCRUNNER_INSTALL:-$HOME/.docrunner}"
bin_dir="$docrunner_install/bin"
exe="$bin_dir/docrunner"

# Makes necessary directories if they don't exist
if [ ! -d "$bin_dir" ]; then
	mkdir -p "$bin_dir"
fi

# Makes web request to install the docrunner zip and unzip it
curl --fail --location --progress-bar --output "$exe.zip" "$docrunner_uri"
unzip -d "$bin_dir" -o "$exe.zip"
chmod +x "$exe"
rm "$exe.zip"

# Outputs success message and adds docrunner to path
echo "Docrunner was installed successfully to $exe"
if command -v docrunner >/dev/null; then
	echo "Run 'docrunner --help' to get started"
else
	case $SHELL in
	/bin/zsh) shell_profile=".zshrc" ;;
	*) shell_profile=".bash_profile" ;;
	esac
	echo "Manually add the directory to your \$HOME/$shell_profile (or similar)"
	echo "  export DOCRUNNER_INSTALL=\"$docrunner_install\""
	echo "  export PATH=\"\$DOCRUNNER_INSTALL/bin:\$PATH\""
	echo "Run '$exe --help' to get started"
fi
