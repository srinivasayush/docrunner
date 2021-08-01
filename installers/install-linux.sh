set -e

latest=$(curl -Ls -o /dev/null -w %{url_effective} https://github.com/DudeBro249/docrunner/releases/latest | cut -d'/' -f8)
docrunner_url="https://github.com/DudeBro249/docrunner/releases/download/$latest/docrunner-linux"
docrunner_directory="/usr/local/bin"
bin_location="$docrunner_directory/docrunner"

# Makes the web request to install the exe from GitHub
sudo curl --fail --location --progress-bar --output "$bin_location" "$docrunner_url"
sudo chmod +x $bin_location

echo "Docrunner was installed successfully to $bin_location"
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
