from parser import Parser
from downloader import Downloader
import pytest

def test_get_dict():
    result = Parser("test.vtt").get_dict()
    assert len(result) == 3
    assert result[0]["text"] == "Hello, this is a test."
def test_last_row():
    result = Parser("test.vtt").get_dict()
    assert result[2]["text"] == "The last sentense."
def test_url_setter():
    with pytest.raises(ValueError):
        Downloader("https://google.com.tw")