# Sudachi向け万病辞書

[万病辞書を形態素解析器Sudachiで利用する \- Out\-of\-the\-box](https://yag-ays.github.io/project/manbyo-sudachi/)

## 配布辞書
万病辞書`MANBYO_201907`から、Sudachiのユーザ辞書形式に変換したファイル

- `manbyo20190704_sabc_dic.txt`: 万病辞書で信頼度LEVELがS,A,B,Cの病名のみ
- `manbyo20190704_all_dic.txt`: 万病辞書のすべての病名

## 使い方
### 1. レポジトリをcloneする

```sh
$ git clone --recursive https://github.com/yagays/manbyo-sudachi
```

### 2. sudachipyをインストールする

```sh
$ pip install sudachipy
```

### 3. バイナリ辞書をビルドする
`BASE_PATH`を自身の環境の`system.dic`が置かれている場所に変更して、下記コマンドを実行。

```sh
BASE_PATH=/path/to/sudachidict/resources/

sudachipy ubuild -s $BASE_PATH/system.dic manbyo20190704_sabc_dic.txt -o user_manbyo_sabc.dic
sudachipy ubuild -s $BASE_PATH/system.dic manbyo20190704_all_dic.txt -o user_manbyo_all.dic
```

