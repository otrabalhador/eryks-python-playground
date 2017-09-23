def write_from_file(file, content):
    file.write(content)


def write_from_file_path(file_path, content):
    with open(file_path, 'a') as _file:
        _file.write(content)


def get_content_from_file_path(file_path):
    with open(file_path, 'r') as _file:
        return _file.read()
