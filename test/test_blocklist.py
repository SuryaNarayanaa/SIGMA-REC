from app.blocklist import BLOCKLIST
def test_blocklist():
    assert BLOCKLIST == set()

def test_blocklist_add():
    BLOCKLIST.add('token')
    assert 'token' in BLOCKLIST

def test_blocklist_remove():
    BLOCKLIST.remove('token')
    assert 'token' not in BLOCKLIST

def test_blocklist_check():
    BLOCKLIST.add('token')
    assert 'token' in BLOCKLIST
    assert 'another_token' not in BLOCKLIST

def test_blocklist_clear():
    BLOCKLIST.clear()
    assert BLOCKLIST == set()

def test_blocklist_len():
    BLOCKLIST.add('token')
    BLOCKLIST.add('another_token')
    assert len(BLOCKLIST) == 2


