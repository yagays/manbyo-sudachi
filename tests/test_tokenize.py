from sudachipy import tokenizer
from sudachipy import dictionary

import pytest


@pytest.fixture(scope="module")
def tokenizer_all():
    return dictionary.Dictionary(config_path="config/sudachi_all.json").create()


@pytest.fixture(scope="module")
def tokenizer_sabc():
    return dictionary.Dictionary(config_path="config/sudachi_sabc.json").create()


def test_tokenize_disease_name_normal(tokenizer_all, tokenizer_sabc):
    text = "疼痛"
    assert tokenizer_all.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == text
    assert tokenizer_sabc.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == text


def test_tokenize_disease_name_alphabet_number_zen(tokenizer_all, tokenizer_sabc):
    text = "Ｅ２Ａ−ＰＢＸ１陽性Ｂリンパ芽球性白血病"
    assert tokenizer_all.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == text
    assert tokenizer_sabc.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == text


def test_tokenize_disease_name_alphabet_number_han(tokenizer_all, tokenizer_sabc):
    text = "e2a−pbx1陽性bリンパ芽球性白血病"
    assert tokenizer_all.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == text
    assert tokenizer_sabc.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == text


def test_tokenize_disease_name_phrase(tokenizer_all, tokenizer_sabc):
    text = "lsd使用による急性精神・行動障害"
    assert tokenizer_all.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == text
    assert tokenizer_sabc.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == text


def test_tokenize_disease_name_punctuation(tokenizer_all, tokenizer_sabc):
    text = "中咽頭癌、病期不明"
    assert tokenizer_all.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == text
    assert tokenizer_sabc.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == text


def test_tokenize_disease_name_punctuation_comma(tokenizer_all, tokenizer_sabc):
    text = "熱帯熱マラリア、赤痢"
    assert tokenizer_all.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == text
    assert tokenizer_sabc.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == text


def test_tokenize_disease_name_punctuation_comma_before_fix(tokenizer_all, tokenizer_sabc):
    text = "熱帯熱マラリア，赤痢"
    assert tokenizer_all.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == "熱帯熱マラリア"
    assert tokenizer_sabc.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == "熱帯熱マラリア"


def test_tokenize_disease_name_confidence_D(tokenizer_all, tokenizer_sabc):
    text = "脊椎腫瘤"
    assert tokenizer_all.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == "脊椎腫瘤"
    assert tokenizer_sabc.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == "脊椎"  # 脊椎 腫瘤


def test_tokenize_disease_name_confidence_F(tokenizer_all, tokenizer_sabc):
    text = "不感蒸散分"
    assert tokenizer_all.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == "不感蒸散分"
    assert tokenizer_sabc.tokenize(text, tokenizer.Tokenizer.SplitMode.B)[0].surface() == "不感"  # 不感 蒸散 分


def test_tokenize_normal_text(tokenizer_all, tokenizer_sabc):
    text = "吾輩は猫である"
    assert [t.surface() for t in tokenizer_all.tokenize(text, tokenizer.Tokenizer.SplitMode.B)] == [
        "吾輩",
        "は",
        "猫",
        "で",
        "ある",
    ]
    assert [t.surface() for t in tokenizer_sabc.tokenize(text, tokenizer.Tokenizer.SplitMode.B)] == [
        "吾輩",
        "は",
        "猫",
        "で",
        "ある",
    ]
