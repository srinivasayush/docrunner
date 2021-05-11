---
sidebar_position: 4
---
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
markdown_path = 'README.md'
multi_file = false
```

Store all docrunner options under:
```toml
[docrunner]
```

### language
- The language you want to run. **Optional**

### markdown_path
- The path to the to the markdown '.md' file you want to run code from. **Optional**

### directory_path
- The path to the directory where your code should be stored and run. You can
install and store dependencies in this directory. **Optional**

### multi_file
- Whether or not you want each code snippet, delimited by backticks "`"
to be stored and run in another file. **Optional**

### startup_command
- The command you would like to run in order to run  your code. Put the command in 
between quotes like "node main.js". **Optional**
