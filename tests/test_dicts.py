from utils.dicts import get_val

def test_get_val():
    assert get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert get_val({"vcs": "mercurial"}, "vcs", "git") == "mercurial"


def test_empty_dict():
    """Тестируем пустой словарь"""
    assert get_val({}, "vcs", "git") == "git"
    assert get_val({}, "vcs", "bazaar") == "bazaar"

def test_empty_key():
    assert get_val({"vcs": "mercurial"}, " ", "git") == "git"


def test_dirty_key():
    assert get_val({"vcs": "mercurial"}, " vcs   ") == "mercurial"