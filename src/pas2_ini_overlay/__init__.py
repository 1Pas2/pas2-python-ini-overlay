from configparser import ConfigParser


def overlay(*documents: str) -> dict[str, dict[str, str]]:
    result = {}
    for document in documents:
        parser = ConfigParser(interpolation=None, strict=True)
        parser.optionxform = str
        parser.read_string(document)
        for section in parser.sections():
            result.setdefault(section, {}).update(dict(parser[section]))
    return result
