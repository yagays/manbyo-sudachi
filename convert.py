"""
万病辞書をsudachiのユーザ辞書形式に変換する
"""

import pandas as pd

from util.SudachiCharNormalizer import SudachiCharNormalizer


def extract_yomigana(s):
    yomi = s.split(";")[0]
    if yomi != "nan":
        return yomi
    else:
        return ""


def convert_dict_format(s, normalizer):
    midashi = normalizer.rewrite(s[0]).replace(",", "、")  # 出現形
    word = s[0]  # 出現形
    yomi = extract_yomigana(s[4])  # 複合文字列ラベル
    return f"{midashi},4786,4786,6000,{midashi},名詞,固有名詞,一般,*,*,*,{yomi},{word},*,*,*,*,*"


normalizer = SudachiCharNormalizer(rewrite_def_path="SudachiPy/sudachipy/resources/rewrite.def")

df = pd.read_excel("data/MANBYO_201907/MANBYO_20190704.xlsx")

target_df = df[df["信頼度LEVEL"].isin(["S", "A", "B", "C"])]
output_df = target_df.apply(lambda x: convert_dict_format(x, normalizer), axis=1)
output_df.to_csv("manbyo20190704_sabc_dic.txt", header=None, index=None, sep="|")


output_df = df.apply(lambda x: convert_dict_format(x, normalizer), axis=1)
output_df.to_csv("manbyo20190704_all_dic.txt", header=None, index=None, sep="|")
