# simple-env
Simple Processing of Environmental Variables

# features
- automatic removal of quotes (`"` and `'`)
- automatic conversion of Booleans (`"true"`, `"True"`, and `"TRUE"` are converted into `True`)
- automatic conversion of Integers
- automatic suggestion of typo corrections

# usage
## get variable
```python
import simple_env as se

email_host = se.get("EMAIL_HOST")
# email_host is "smtp.gmail.com"

email_use_tls = se.get("EMAIL_USE_TLS")
# email_use_tls is True

email_port = se.get("EMAIL_PORT")
# email_port is 8080
```

## suppress warnings
By default, simple env warns when it can't find a variable and offers an alternative suggestion if possible.
```python
email_use_tls = se.get("USE_TLS")
```
prints
```bash
[simple-env] could not find "USE_TLS", did you mean "EMAIL_USE_TLS"?
```

## check if environmental variable is set
```python
import simple_env as se

hasState = se.has("STATE")
# hasState is True if the variable is set to null
```
