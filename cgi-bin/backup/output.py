#!/usr/bin/python3

import SQLlib
import cgi

form = cgi.FieldStorage()
value1 = form.getfirst("value1")
value2 = form.getfirst("value2")

conn = SQLlib.connect_personalDB()
cursor = conn.cursor()
info_name = []
#user_code='testuser'
provider_code = value1
#rows = SQLlib.get_user_info(cursor, user_code)
rows = SQLlib.get_provider_name(cursor, provider_code)
rowsHTML = ""
for r in rows:
    info_name.append(r['info_name'])
    rowHTML = f"""
                <tr>
                  <td>{provider_code}</td>
                  <td>{r['info_name']}</td>
                  <td>{r['info']}</td>
                  <td>{r['register_date']}</td>
                  <td>{r['user_code']}</td>
                  <td>{r['URL']}</td>
                  <td>{r['provide_date']}</td>
                </tr>"""
    rowsHTML = rowsHTML + rowHTML
SQLlib.close_DB(conn)
#

html = """
<html>
<head>
<title>Nodegraph</title>
<title>Home</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="../../html/viewformation/css/home.css" />
<link rel="stylesheet" href="../../html/viewformation/css/style.css" > <!--多分ない-->

<script>
window.onload = function() {
    var cv = document.getElementById('cv1');    // 要素を得る
    if (!cv) { return; }

    var ct = cv.getContext('2d');               // 2D(平面)コンテキストを得る
    if (!ct) { return; }

    //cv.setAttribute("width", ct.width.toString());
    //cv.setAttribute("height", ct.height.toString());

    let width = cv.width;
    let height= cv.height;
    let r = 40;
    let dist = 200;

    let nowang = 0;
"""
leng = len(rows)
m = f"""let num_circles = {leng};
let aroundText = {info_name};
"""
#let aroundText = ["姓名", "Eメール", "住所", "生年月日", "性別"];
html2 = f"""
    let angle = Math.PI*2/num_circles;

    let centerx = 0;
    let centery = 0;
"""
m2 = 'let centerText = "%s"' % (provider_code);

html3 = """
    ct.beginPath();
    ct.fillStyle = '#97973F';
    ct.arc(width/2, height/2, r, 0, Math.PI * 2, false);  // 円を描画する
    ct.fill();

    centerx = width/2;
    centery = height/2;

    for(let i = 0; i < num_circles; i++){
	    let x =  centerx+(dist*Math.cos(nowang));
	    let y =  centery+(dist*Math.sin(nowang));

	    ct.beginPath();
	    ct.fillStyle = '#97973f';
	    ct.arc(x, y, r, 0, Math.PI * 2, false);  // 円を描画する
    	    ct.fill();

       	    makeEdge(ct,centerx, centery, x, y);

	    ct.fillStyle = '#000000';
	    ct.font = 'normal 18pt "メイリオ"';
	    ct.fillText(aroundText[i], x-30, y+10);

            nowang += angle;
    }
    ct.fillStyle = '#000000';
    ct.font = 'normal 18pt "メイリオ"';
    ct.fillText(centerText, centerx-30, centery+10);

}
function makeEdge(ct, cetx, cety,x, y){
    ct.beginPath();
    ct.strokeStyle = '#97973f';
    ct.moveTo(x, y);
    ct.lineTo(cetx, cety);                        // 線を描画する
    ct.closePath();
    ct.stroke();
}
"""
html4 = f"""
</script>
</head>
<body>
	<header>
		<div class="container">
			<div class="icon">
				<img src="../../html/viewformation/images/icon1.png" width="150" alt="toro's picture">
			</div>
			<div class="info">
				<h1>your information</h1><br>
				<p>あなたの大切な個人情報を管理します</p>
			</div>
		</div>
	</header>
        <main>
		<div class="textbody">
 			<canvas id="cv1" width="600" height="600"></canvas>
		</div>
	</main>
</body>
</html>
"""
print("Content-type:text/html")
print("")
print(html+m+html2+m2+html3+html4)
