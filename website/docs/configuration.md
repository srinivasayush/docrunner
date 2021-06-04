# Configuration

All docrunner configuration is stored in `docrunner.toml`. Toml allows us to easily
store configuration options with a single file using key-value pairs.

Learn more about the `toml` markup language [here](https://toml.io/en/)

:::important
Use of any and all docrunner configuration is **optional**
:::

## Example
```toml
[docrunner]
language = 'python'
markdown_paths = ['README.md']
multi_file = false
```

Store all docrunner options under:
```toml
[docrunner]
```

### language
- The language you want to run. string, **Optional**

### markdown_paths
- An array to the to the markdown '.md' files you want to run code from.
You can also list directories. array, **Optional**

Example:
```toml
[docrunner]
markdown_paths = [
    'README.md',
    './documentation'
]
```
- We are pointing `docrunner` to both `README.md` and a folder called `documentation`
where our markdown files are stored. Check [recursive](#recursive) for more details
on listing directories in `markdown_paths`

### directory_path
- The path to the directory where your code should be stored and run. You can
install and store dependencies in this directory. string, **Optional**

### multi_file
- Whether or not you want each code snippet, delimited by backticks(\```)
to be stored and run in another file. boolean, **Optional**

### startup_command
- The command you would like to run in order to run  your code. Put the command in
between quotes like "node main.js". string, **Optional**

### recursive
- Whether you want docrunner to search through specified directories recursively
(look through sub-directories). boolean, **Optional**

### dotenv
- The path to your dotenv file(if one exists), which stores your environment variables
and secrets. string, **Optional**
