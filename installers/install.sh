set -e

docrunner_url="https://github.com/DudeBro249/docrunner/releases/download/v1.1.1/docrunner.exe"
docrunner_directory="C:\src\Docrunner"
exe_location="$docrunner_directory\docrunner.exe"

if [ ! -d "$docrunner_directory" ]; then
    echo "Creating installation directory: $docrunner_directory"
	mkdir -p "$docrunner_directory"
fi

# Makes the web request to install the exe from GitHub
curl --fail --location --progress-bar --output "$exe_location" "$docrunner_url"

echo "Docrunner was installed successfully to $exe_location"
if command -v docrunner >/dev/null; then
	echo "Run 'docrunner --help' to get started"
else
	# case $SHELL in
	# /bin/zsh) shell_profile=".zshrc" ;;
	# *) shell_profile=".bash_profile" ;;
	# esac
	# echo "Manually add the directory to your \$HOME/$shell_profile (or similar)"
	# echo "  export DENO_INSTALL=\"$deno_install\""
	# echo "  export PATH=\"\$DENO_INSTALL/bin:\$PATH\""
	# echo "Run '$exe --help' to get started"
    echo "Installation Failed"
fi