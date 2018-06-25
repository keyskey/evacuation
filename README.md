#User guide

計算と可視化に必要なファイルは

1. Agent.py
  => 歩行者の持つパラメータ、移動確率を計算する関数などが書かれています

2. Field.py
  => メイン実行プログラム

3. field.csv 
  => 人間が移動する空間を描いたエクセルシートをcsvに変換したもの

4. animation.py
  => outputファイルをpng画像に変換してgifアニメにするスクリプト

の4つです。
計算実行時はターミナルで
$ python Field.py

と打ってください。output*.csvというファイルが大量に吐き出されます。

次にアニメーションを作成します。
$ python animation.py

と打つと収束までにかかったタイムステップ数を聞かれるので、Field.pyのログの最後に出力されている〜timestep
の〜に当たる数字を入力してください。animation.gifという名前でgifアニメが作られているのが確認できます。
