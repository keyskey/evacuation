# User guide

計算と可視化に必要なファイルは

1.Agent.py <br>
  => 歩行者の持つパラメータ、移動確率を計算する関数などが書かれています<br>
<br>
2.Field.py <br>
  => メイン実行プログラム <br>
<br>
3.field.csv <br> 
  => 人間が移動する空間を描いたエクセルシートをcsvに変換したもの <br>
<br>
4.animation.py <br>
  => outputファイルをpng画像に変換してgifアニメにするスクリプト <br>
<br>
の4つです。<br>
計算実行時はターミナルで<br>
$ python Field.py <br>

と打ってください。output*.csvというファイルが大量に吐き出されます。<br>

次にアニメーションを作成します。<br>
$ python animation.py <br>

と打つと収束までにかかったタイムステップ数を聞かれるので、Field.pyのログの最後に出力されている〜timestepの〜に当たる数字を入力してください。<br>
animation.gifという名前でgifアニメが作られているのが確認できます。

