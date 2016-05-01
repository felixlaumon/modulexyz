ignore_test_paths = [
    # Files to ignore
]


def pytest_ignore_collect(path, config):
    return any(path.fnmatch(ignore) for ignore in ignore_test_paths)
