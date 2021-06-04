# Environment Variables

Environment variables allow you to store values that you do not want
exposed to others. Docrunner allows you to load these in through the
`docrunner.toml` configuration file

You can learn more about docrunner configuration [here](/docs/configuration)

```env title=".env"
SECRET_TOKEN=secretvalue
```

```bash {3} title="docrunner.toml"
[docrunner]
markdown_paths = ['README.md']
dotenv = '.env'
```
- In this `docrunner.toml` file we tell docrunner that we want to load the
values in `.env` into our environment, using the <code>[dotenv](/docs/configuration#dotenv)</code>
option

We can now access the environment variables in `.env` in our code snippets:

    ```python
    import os

    # Retrieve the SECRET_VALUE from our environment

    SECRET_VALUE = os.getenv('SECRET_VALUE')
    ```
