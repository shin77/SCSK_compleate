#!/usr/bin/python3

import cgi
# パラメータを取得するための関数
# get、post区分なしでデータを持ち込む。
#form = cgi.FieldStorage()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Title</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="../html/uikit2.css" />
        <link rel="stylesheet" href="../html/style.css" > <!--多分ない-->
        <script src="../html/uikit.min.js"></script>
        <script src="../html/uikit-icons.min.js"></script>
    </head>
    <body>
        
        <ul>
          <form method="POST" action="server.py">
            <p><span class="m1">サイト名</span>：<input type="text" name="website"></p>
            <p><span class="m2">URL</span>：<input type="text" name="url"></p>
            <p><span class="m3">ユーザー名</span>：<input type="text" name="user_id" size="20"></p>
            <p><span class="m4">パスワード</span>：<input type="text" name="password"></p>
            <p><span class="m5">氏名</span>：<input type="text" name="name"></p>
            <p><span class="m6">生年月日</span>：
                <!--year-->
                <select name="year">
                    <option value="1980">1980年</option>
                    <option value="1981">1981年</option>
                    <option value="1982">1982年</option>
                    <option value="1983">1983年</option>
                    <option value="1984">1984年</option>
                    <option value="1985">1985年</option>
                    <option value="1986">1986年</option>
                    <option value="1987">1987年</option>
                    <option value="1988">1988年</option>
                    <option value="1989">1989年</option>
                    <option value="1990">1990年</option>
                    <option value="1991">1991年</option>
                    <option value="1992">1992年</option>
                    <option value="1993">1993年</option>
                    <option value="1994">1994年</option>
                    <option value="1995">1995年</option>
                    <option value="1996">1996年</option>
                    <option value="1997">1997年</option>
                    <option value="1998">1998年</option>
                    <option value="1999">1999年</option>
                    <option value="2000">2000年</option>
                    <option value="2001">2001年</option>
                    <option value="2002">2002年</option>
                    <option value="2003">2003年</option>
                    <option value="2004">2004年</option>
                    <option value="2005">2005年</option>
                    <option value="2006">2006年</option>
                    <option value="2007">2007年</option>
                    <option value="2008">2008年</option>
                    <option value="2009">2009年</option>
                    <option value="2010">2010年</option>
                    <option value="2011">2011年</option>
                    <option value="2012">2012年</option>
                    <option value="2013">2013年</option>
                    <option value="2014">2014年</option>
                    <option value="2015">2015年</option>
                    <option value="2016">2016年</option>
                    <option value="2017">2017年</option>
                    <option value="2018">2018年</option>
                    <option value="2019">2019年</option>
                    <option value="2020">2020年</option>
                    <option value="2021">2021年</option>
                    
                    </select>
                <!--month-->
                <select name="month">
                <option value="01">1月</option>
                <option value="02">2月</option>
                <option value="03">3月</option>
                <option value="04">4月</option>
                <option value="05">5月</option>
                <option value="06">6月</option>
                <option value="07">7月</option>
                <option value="08">8月</option>
                <option value="09">9月</option>
                <option value="10">10月</option>
                <option value="11">11月</option>
                <option value="12">12月</option>
                </select>
                <select name="day">
                    <option value="01">1日</option>
                    <option value="02">2日</option>
                    <option value="03">3日</option>
                    <option value="04">4日</option>
                    <option value="05">5日</option>
                    <option value="06">6日</option>
                    <option value="07">7日</option>
                    <option value="08">8日</option>
                    <option value="09">9日</option>
                    <option value="10">10日</option>
                    <option value="11">11日</option>
                    <option value="12">12日</option>
                    <option value="13">13日</option>
                    <option value="14">14日</option>
                    <option value="15">15日</option>
                    <option value="16">16日</option>
                    <option value="17">17日</option>
                    <option value="18">18日</option>
                    <option value="19">19日</option>
                    <option value="20">20日</option>
                    <option value="21">21日</option>
                    <option value="22">22日</option>
                    <option value="23">23日</option>
                    <option value="24">24日</option>
                    <option value="25">25日</option>
                    <option value="26">26日</option>
                    <option value="27">27日</option>
                    <option value="28">28日</option>
                    <option value="29">29日</option>
                    <option value="30">30日</option>
                    <option value="31">31日</option>
                    </select></p>
            
            <p><span class="m7">性別</span>:<input type="radio" name="gender" value="男" />男性
                <input type="radio" name="gender" value="女" checked/>女性
                <input type="radio" name="gender" value="LGBT" checked/>その他</p>
            <p><span class="m8">電話番号</span>：<input type="text" name="phone1-1">
                   - <input type="text" name="phone1-2">
                   - <input type="text" name="phone1-3"></p>
            <p><span class="m9">携帯番号</span>：<input type="text" name="phone2-1">
                   - <input type="text" name="phone2-2">
                   - <input type="text" name="phone2-3"></p>
            <p><span class="m10">メールアドレス</span>：<input type="text" name="email"></p>
            <p><span class="m11">住所</span>：<select name="pref_id">
                <option value="" selected>都道府県</option>
                <option value="北海道">北海道</option>
                <option value="青森県">青森県</option>
                <option value="岩手県">岩手県</option>
                <option value="宮城県">宮城県</option>
                <option value="秋田県">秋田県</option>
                <option value="山形県">山形県</option>
                <option value="福島県">福島県</option>
                <option value="茨城県">茨城県</option>
                <option value="栃木県">栃木県</option>
                <option value="群馬県">群馬県</option>
                <option value="埼玉県">埼玉県</option>
                <option value="千葉県">千葉県</option>
                <option value="東京都">東京都</option>
                <option value="神奈川県">神奈川県</option>
                <option value="新潟県">新潟県</option>
                <option value="富山県">富山県</option>
                <option value="石川県">石川県</option>
                <option value="福井県">福井県</option>
                <option value="山梨県">山梨県</option>
                <option value="長野県">長野県</option>
                <option value="岐阜県">岐阜県</option>
                <option value="静岡県">静岡県</option>
                <option value="愛知県">愛知県</option>
                <option value="三重県">三重県</option>
                <option value="滋賀県">滋賀県</option>
                <option value="京都府">京都府</option>
                <option value="大阪府">大阪府</option>
                <option value="兵庫県">兵庫県</option>
                <option value="奈良県">奈良県</option>
                <option value="和歌山県">和歌山県</option>
                <option value="鳥取県">鳥取県</option>
                <option value="島根県">島根県</option>
                <option value="岡山県">岡山県</option>
                <option value="広島県">広島県</option>
                <option value="山口県">山口県</option>
                <option value="徳島県">徳島県</option>
                <option value="香川県">香川県</option>
                <option value="愛媛県">愛媛県</option>
                <option value="高知県">高知県</option>
                <option value="福岡県">福岡県</option>
                <option value="佐賀県">佐賀県</option>
                <option value="長崎県">長崎県</option>
                <option value="熊本県">熊本県</option>
                <option value="大分県">大分県</option>
                <option value="宮崎県">宮崎県</option>
                <option value="鹿児島県">鹿児島県</option>
                <option value="沖縄県">沖縄県</option>
                </select><br>
                <span class="m12"></span><input type="text" name="town" placeholder="市区町村"></p><br>
            <p><input type="submit" value="保存" id="save"></p>
          </form>
    </body>
</html>
""";

print("Content-type:text/html")
print("")
print(html)
