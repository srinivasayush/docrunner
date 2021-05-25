# Comments

Comments allow you to annotate code snippets within your markdown files with important
metadata and options. Docrunner parses these comments to know how to run your code.

These comments provide docrunner with important information, however
are not shown when rendering markdown files because they are comments.

:::important
Use of any and all docrunner comments is **optional**
:::

## Example

    <!--docrunner.ignore-->  
    ```python
    print('Ignored code snippet')
    ```

- In this example, docrunner will not run the python code snippet due to the
`<!--docrunner.ignore-->` markdown comment above it.

:::info
You can stack multiple docrunner comments on the same code snippet
:::

## List of Parsed Comments
- `<!--docrunner.ignore-->` - Causes docrunner to ignore the code snippet this is attached to
- `<!--docrunner.file_name = "file.py"-->` - If the `multi_file` field is set to `True` when running docrunner,
docrunner will put this code snippet in a file named `file.py`
Check [here](/docs/configuration#multi_file) for more information about `multi_file`
