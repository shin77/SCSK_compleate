#!/usr/bin/python3

import SQLlib

html = """
<!DOCTYPE html>
<!-- saved from url=(0041)http://35.76.245.229/cgi-bin/dashboard.py -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>output</title>
    
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<link rel="stylesheet" href="../html/output.css">
        <link rel="stylesheet" href="./Database_files/style.css"> <!--多分ない-->

    <!-- Bootstrap core CSS -->
<link href="./Database_files/bootstrap.min.css" rel="stylesheet">

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <!-- Custom styles for this template -->
    <link href="./Database_files/dashboard.css" rel="stylesheet">
  <style type="text/css">/* Chart.js */
@-webkit-keyframes chartjs-render-animation{from{opacity:0.99}to{opacity:1}}@keyframes chartjs-render-animation{from{opacity:0.99}to{opacity:1}}.chartjs-render-monitor{-webkit-animation:chartjs-render-animation 0.001s;animation:chartjs-render-animation 0.001s;}</style></head>
  <body>
		<header>
			<div class="container">
				<div class="icon">
					<img src="../html/images/icon1.png" width="150" alt="toro's picture">
				</div>
				<div class="info">
					<h1>Viewformation</h1><br>
					<h2>いつでもどこでもあなたに情報を。</h2><br>
					<h2>データ管理にお困りのあなたに寄り添います</h2>
				</div>
			</div>
			
		</header>
						
						
						
		 <main>
		<div class="textbody">
							
					
			<div class="heading">
				<h2 class="headingtext">こちらがあなたの情報です！</h2><br>
				<div class="icon2">
					<img src="../html/images/icon3.png" width="150" alt="toro's picture">
				</div>
			</div>				
							
							
			

<div class="container-fluid">
  <div class="row">
      <div class="table-responsive">
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th>UserID</th>
              <th>Info Name</th>
              <th>Info Value</th>
              <th>Register Date</th>
              <th>Company</th>
              <th>URL</th>
              <th>Provided Date</th>
            </tr>
          </thead>
          <tbody>

                <tr>
                  <td>testuser</td>
                  <td>姓名</td>
                  <td>テストさん</td>
                  <td>2021-10-13</td>
                  <td>Amazon</td>
                  <td>https://www.amazon.co.jp/</td>
                  <td>2021-10-13</td>
                </tr>
                <tr>
                  <td>testuser</td>
                  <td>姓名</td>
                  <td>テストさん1</td>
                  <td>2021-10-13</td>
                  <td>Google</td>
                  <td>None</td>
                  <td>2021-10-13</td>
                </tr>
                <tr>
                  <td>testuser</td>
                  <td>生年月日</td>
                  <td>1980/01/01</td>
                  <td>2021-10-13</td>
                  <td>Google</td>
                  <td>None</td>
                  <td>2021-10-13</td>
                </tr>
                <tr>
                  <td>testuser</td>
                  <td>性別</td>
                  <td>男</td>
                  <td>2021-10-13</td>
                  <td>Google</td>
                  <td>None</td>
                  <td>2021-10-13</td>
                </tr>
                <tr>
                  <td>testuser</td>
                  <td>電話番号</td>
                  <td>09090090909</td>
                  <td>2021-10-14</td>
                  <td>None</td>
                  <td>None</td>
                  <td>2021-10-14</td>
                </tr>
                <tr>
                  <td>testuser</td>
                  <td>電話番号</td>
                  <td>09011110990</td>
                  <td>2021-10-14</td>
                  <td>None</td>
                  <td>None</td>
                  <td>2021-10-14</td>
                </tr>
                <tr>
                  <td>testuser</td>
                  <td>性別</td>
                  <td>LGBT</td>
                  <td>2021-10-14</td>
                  <td>None</td>
                  <td>None</td>
                  <td>2021-10-14</td>
                </tr>
                <tr>
                  <td>testuser</td>
                  <td>E-mail</td>
                  <td>test@yahoo.co.jp</td>
                  <td>2021-10-14</td>
                  <td>None</td>
                  <td>None</td>
                  <td>2021-10-14</td>
                </tr>
                <tr>
                  <td>testuser</td>
                  <td>E-mail</td>
                  <td>sese@yahoo.co.jp</td>
                  <td>2021-10-14</td>
                  <td>None</td>
                  <td>None</td>
                  <td>2021-10-14</td>
                </tr>
          </tbody>
      
    
  

<script src="./Database_files/jquery-3.5.1.slim.min.js.ダウンロード" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
      <script>window.jQuery || document.write('<script src="../assets/js/vendor/jquery.slim.min.js"><\/script>')</script><script src="./Database_files/bootstrap.bundle.min.js.ダウンロード"></script>
        <script src="./Database_files/feather.min.js.ダウンロード"></script>
        <script src="./Database_files/Chart.min.js.ダウンロード"></script>
        <script src="./Database_files/dashboard.js.ダウンロード"></script>


</table></div></div></div>
							
		</div>
		</main>
				
		<div class="returnbutton"><a href="../html/viewformation/home.html">HOME画面へ</a></div>		
				
				
				
	</body>
</html>
"""
conn = SQLlib.connect_personalDB()
cursor = conn.cursor()
user_code='testuser'
rows = SQLlib.get_user_info(cursor, user_code)
rowsHTML = ""
for r in rows:
    #test = test + "a%s" % ("test")
    rowHTML = f"""
                <tr>
                  <td>{user_code}</td>
                  <td>{r['info_name']}</td>
                  <td>{r['info']}</td>
                  <td>{r['register_date']}</td>
                  <td>{r['provider_name']}</td>
                  <td>{r['URL']}</td>
                  <td>{r['provide_date']}</td>
                </tr>"""
    rowsHTML = rowsHTML + rowHTML
SQLlib.close_DB(conn)

endHTML="""
          </tbody>
      </div>
    </main>
  </div>
</div>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
      <script>window.jQuery || document.write('<script src="../assets/js/vendor/jquery.slim.min.js"><\/script>')</script><script src="../assets/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/feather-icons/4.9.0/feather.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.3/Chart.min.js"></script>
        <script src="dashboard.js"></script></body>
</html>
"""
print("Content-type:text/html")
print("")
print(html+rowsHTML)
