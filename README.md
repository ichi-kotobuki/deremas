# THEiDOLM@STER シンデレラガールズ 日本語 IME 用辞書

**THEiDOLM@STER シンデレラガールズ 日本語 IME 用辞書**は、BANDAI NAMCO Entertainment の「アイドルマスター シンデレラガールズ」に関する単語を日本語 IME で快適に入力するための辞書です。

メインターゲットはジャストシステムの ATOK ですが、基本的な変換辞書は MS-IME / Google 日本語変換（Mozc）/ macOS 日本語入力でも利用可能です。

## 特徴

ATOK の単語コメント表示機能、置換候補機能を活用。これで誤入力も怖くない？

※ATOK for Android / ATOK for Android \[Professional\] は対象外です。

## 収録内容

### 登場キャラクター（人名）

「THEiDOLM@STER シンデレラガールズ」（以降、モバマスと表記）および「THEiDOLM@STER シンデレラガールズ スターライトステージ」（以降、デレステと表記）に登場するキャラクターの人名。
辞書にはモバマスとデレステの両方に登場するキャラクターを登録しています。765プロダクション所属のアイドルなどは登録対象外です。

## 辞書登録用テキストの生成方法

辞書登録用テキストは整理済みのデータから [Python](https://www.python.org/) スクリプトを使用して生成します。

### 動作環境

Python 3.6 以上が必要です。追加パッケージのインストールは不要です。

### 実行方法

``makedict.py`` が登録用テキストを生成するスクリプトです。コマンドラインから以下のように実行します。

```
python makedict.py (atok|macos|msime)
```

``(atok|macos|msime)`` の部分は利用している IME を指定してください（Google 日本語入力をお使いの方は ``msime`` を指定）。たとえば、ATOK 用の辞書登録用テキストを出力する場合は、

```
python makedict.py atok
```

とします。

## その他の辞書の情報

アイドルマスターシリーズ全般の単語については、[アイマス DB](https://imas-db.jp/)さんが [IME ユーザー辞書登録用テキスト](https://ime.imas-db.jp/)を作成・管理されています。
