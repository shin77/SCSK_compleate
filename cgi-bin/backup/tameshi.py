#! /usr/bin/python3
import cgi
# cgiはcgiプログラムに使うモジュールだ。
import cgitb
# cgitbはcgiプログラムデバッグに関するモジュールだ。(エラーが発生すればphpみたいにエラーを画面に表示する。)
cgitb.enable()
# パラメータを取得するための関数
# get、post区分なしでデータを持ち込む。
form = cgi.FieldStorage()
# パラメータdataを取得する。
# パラメータのtestを取得する。
# 画面い応答するhtmlドキュメント
html = f"""
<!DOCTYPE html>
<html>
<h5>サイト名入力</h5>
  <body>
    <form action="output.py" method='post'>
      <input type='text' name='value1'>
      <input type='submit' name='submit' value="送信">
    </form>
  </body>
</html>
""";
# ヘッダータイプ設定
print("Content-type:text/html")
# httpプロトコールでheaderとbodyの区分は改行なので必ず入れる。なければエラーに発生する。(bodyがないhttpファイルなので)
print('')
print(html)
