# collect data from crawler and label them positive or not
# Uppdate: add some keywords to do second clean
import os
import csv
import numpy as np
# Here is the folder path
filepath=".\clean_data"
namelist = os.listdir(filepath)

tag = """"""
mid_content = """"""
counter = 1
for username in namelist:
    username_path = filepath + "\\" + username
    with open(username_path, "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        print(rows)
        # Ignore the file when content amount less 4 rows
        if len(rows)<4:
            continue
        print("NoW is :" + username)
        res = []
        for row_content in rows[4:]:
            res.append(row_content)
        mid_content = """"""
        for row_content in res:
            if "covid".upper() in row_content[3].upper() or "Corona".upper() in row_content[3].upper() or "sars".upper() in row_content[3].upper():
                highlight_content = row_content[3].replace("test", """"<span style="color: yellow;">test</span>""")
                highlight_content = highlight_content.replace("TEST",""""<span style="color: yellow;">TEST</span>""")
                highlight_content = highlight_content.replace("positive", """"<span style="color: yellow;">positive</span>""")
                highlight_content = highlight_content.replace("POSITIVE", """"<span style="color: yellow;">POSITIVE</span>""")
                highlight_content = highlight_content.replace("covid", """"<span style="color: red;">covid</span>""")
                highlight_content = highlight_content.replace("COVID", """"<span style="color: red;">COVID</span>""")
                highlight_content = highlight_content.replace("Covid", """"<span style="color: red;">Covid</span>""")
                highlight_content = highlight_content.replace("Corona", """"<span style="color: red;">Corona</span>""")
                highlight_content = highlight_content.replace("corona", """"<span style="color: red;">corona</span>""")
                highlight_content = highlight_content.replace("CORNOA", """"<span style="color: red;">CORNOA</span>""")
                highlight_content = highlight_content.replace("sars", """"<span style="color: #D35400;">sars</span>""")
                highlight_content = highlight_content.replace("SARS", """"<span style="color: #D35400;">SARS</span>""")
                highlight_content = highlight_content.replace("Sars", """"<span style="color: #D35400;">Sars</span>""")
                tweet_content = """<tr class="tbContext">
                <td>{number}</td>
                <td>{tweet_time}</td>
                <td class ="content_left">{tweet_information}</td>
                <td>{retweet_count}</td>
                <td>{favorite_count}</td>
                <td><a href="{twitter_url}">原文</a></td>
                <td><input type="checkbox" name = "{user_name}" style="width:35px; height:35px"></td>
                <td><textarea name="remark" style="width:100%;height:100%;font-size:30px;"></textarea></td>
            </tr>""".format(number = row_content[0], tweet_time = row_content[8], tweet_information = highlight_content, retweet_count = row_content[5], favorite_count = row_content[6], twitter_url = row_content[4], user_name=row_content[1])
                # counter += 1
                mid_content += tweet_content
        # Here is html format frame
        content = """<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>"""+username+"""</title>
</head>
<style>
    body {
        background: #000;
    }
    #Main {
        width: 2500px;
        text-align: center;
        margin: 0 auto;
    }
    table {
        width: 2500px;
        border-collapse: collapse;
        text-align: left;
        margin: 10px 5px 5px 10px;
        cursor: default;
        border: 1px solid #ccc;
        margin-top:20px;
        box-shadow: 0px 0px 10px rgba(0,255,255,0.75);
        border: 1px solid rgba(127,255,255,0.75);
        -webkit-box-shadow: 0px 0px 8px rgba(0,255,255,0.75);
        -moz-box-shadow: 0px 0px 8px rgba(0,255,255,0.75);
        box-shadow: 0px 0px 8px rgba(0,255,255,0.75);
    }
    .tbTitle>th {
        font-weight: 300;
        text-align: center;
        padding: 10px 0 10px 0;
        font: 15px "微软雅黑", Arial, Helvetica, sans-serif;
        background-color: rgba(0,93,93,0.8);
        color: rgba(127,255,255,0.75);
        text-shadow: 0px 0px 20px rgba(127,255,255,1);
    }
    th, td {
        border: 3px solid rgba(127,255,255,0.55);
        text-align: center;
        color: rgba(127,255,255,0.75);
        text-shadow: 0px 0px 20px rgba(127,255,255,1);

    }
    .tbContext:hover {
        background-color: rgba(0,99,99,0.9) !important;
    }
    td,td>a {
        font: 30px "微软雅黑", Arial, Helvetica, sans-serif;
        text-align: center;
        padding-top: 10px;
        padding-right: 10px;
        padding-left: 10px;
        padding-bottom: 10px;
        color: rgba(127,255,255,0.75);
        text-shadow: 0px 0px 20px rgba(0,255,255,0.75);
    }
    .tbContext:nth-child(2n 1) {
        background-color: rgba(0,127,127,0.1);
    }
    .content_left{
        text-align: left;
    }
</style>
<body>
<script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
<script>
    function validateForm() {
       res = {};
        res_namelist = [];
        var str = ["username, No., created_at, full_text, retweet, favorite, url, remarks, \\n"];
        var Tabobj = $("#data");
        var Check = $("table input[type=checkbox]:checked");//在table中找input下类型为checkbox属性为选中状态的数据
        Check.each(function () {//遍历
            var row = $(this).parent("td").parent("tr");//获取选中行
            var temp = []
            
            temp.push(row.get(0).getElementsByTagName("td")[6].getElementsByTagName("input")[0].name)
            temp.push(row.get(0).getElementsByTagName("td")[0].innerText);
            temp.push(row.get(0).getElementsByTagName("td")[1].innerText);
            console.log(row.get(0).getElementsByTagName("td")[2].innerText)
            modified_content = row.get(0).getElementsByTagName("td")[2].innerText.replace(/\\"/g, "\\\"\\\"")
            console.log(modified_content)
            modified_content = "\\"" + modified_content + "\\""
            console.log(modified_content)
            temp.push(modified_content);
            temp.push(row.get(0).getElementsByTagName("td")[3].innerText);
            temp.push(row.get(0).getElementsByTagName("td")[4].innerText);
            temp.push(row.get(0).getElementsByTagName("td")[5].getElementsByTagName("a")[0].href);
            temp.push(row.get(0).getElementsByTagName("td")[7].getElementsByTagName("textarea")[0].value);
            str.push(temp.join(",")+"\\n");
        })

        var uri = 'data:text/csv;charset=utf-8,' + '\\uFEFF' + encodeURIComponent(str.join(""));
        var downloadLink = document.createElement("a");
        downloadLink.href = uri;
         downloadLink.download = \"""" + username + """.csv\";
        document.body.appendChild(downloadLink);
        downloadLink.click();
        document.body.removeChild(downloadLink);
    }
</script>

<br>
<H1 style="text-align: left;"><span style="color: white; ">"""+username+""""</span></H1></body>
<br>
<div id="Demo" style="height: 67px; max-height: 989px;">
    <div id="Main">
        <form name="myForm" onsubmit="validateForm()" method="post">
            <table style="table-layout:fixed;word-break:normal;>
			<tbody>
			<tr class="tbTitle">
            <th width= "1">NO.</th>
            <th width= "15">created_at</th>
            <th width= "70">full_text</th>
            <th width= "1">retweet</th>
            <th width= "1">favorite</th>
            <th width= "3">twitter_url</th>
            <th width="1">reslut</th>
            <th width="7">remark</th>
            </tr>
            </tbody>""" + mid_content + """            
            </table>
            <br>
            <br>
            <input type="button" onclick="validateForm()" value="完成提交" style="text-align: center; width: 200px; height: 100px;font-size: 30px;background-color: lightgreen">
        </form>
    </div>
</div>
</body>
</html>"""
    # print(content)
    with open(".\html\{filename_username}.html".format(filename_username=username[:-4]+"_second_clean"), "w", encoding="UTF-8") as f:
        f.write(content)
