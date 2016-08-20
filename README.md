## README

Some Python tools.

### Context manager for file I/O

A "context manager" imposes a beginning and end on some process that can cause problems if interrupted midway through. In the case of file I/O, if a file is opened for reading or writing and then not closed properly, it can be left in a locked state. A context manager (initiated by the `with` keyword) ensure that the file is closed in any case. Example

```python
with open('questions_and_answers.json', 'r') as f:
    content = f.read()
```

The content of the file is in variable `content` after the file is closed by the context manager.

### JSON format

JSON is a human-readable data-storage format, originated for use with JavaScript. There is a Python library `json` that can be used for working with JSON. Imagine that you have a variable `content` containing JSON data as a strong; the following will "load" the string for decoding, and assign the converted data to a Python dict:

```python
import json
content_dict = json.loads(content)
```

Variable `content_dict` can now be accessed as a regular Python dict.

[end]