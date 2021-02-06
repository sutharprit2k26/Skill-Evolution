from flask import Flask, request, render_template
import numpy as np
app = Flask(__name__, static_url_path='/static')
@app.route("/")
def my_form():
    return render_template('index.html')
"""
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
"""

@app.route("/", methods=['POST'])
def my_form_post():
    bl = request.form['bl']
    ad = request.form['ad']
    cg = request.form['cg']
    sk = request.form['sk']
    exp = request.form['exp'] 
    import pandas as pd
    data = pd.read_csv("student.csv") 
    data.columns =[column.replace(" ", "_") for column in data.columns] 
    
    # for CGPA  

    if cg == "less than 6.0":
        data.query('CGPA <= 6.0', inplace=True)
    elif cg == "6.0 to 8.0":
        data.query('CGPA > 6.0 and CGPA <=8.0', inplace=True)
    elif cg == "grater than 8.0":
        data.query('CGPA > 8.0', inplace=True)
    
    # for Attendence
    if ad == "less than 60":
        data.query('attendance <= 60', inplace=True)
    elif ad == "60 to 80":
        data.query('attendance > 60 and attendance <=75', inplace=True)
    elif ad == "grater than 75":
        data.query('attendance > 75', inplace=True)
     
    # for skills

    if sk == "App development":
        data.query('skills == "App development"', inplace=True)
    elif sk == "Web development":
        data.query('skills == "Web development"', inplace=True)
    elif sk == "Cyber Security":
        data.query('skills == "Cyber security"', inplace=True)
    
    # for backlog's

    if bl == "0":
        data.query('backlog == 0', inplace=True)
    elif bl == "1":
        data.query('backlog == 1', inplace=True)
    elif bl == "2":
        data.query('backlog == 2', inplace=True)
    
    # for exp

    if exp == "1":
        data.query('experience == 1', inplace=True)
    elif exp == "2":
        data.query('experience == 2', inplace=True)
    elif exp == "3":
        data.query('experience == 3', inplace=True)
    
    data1 = data.sort_values('CGPA',ascending=False)
   # data.query('backlog == @bl and attendance == @ad and CGPA == @cg and skills == @sk and experience == @exp', inplace=True) 
    pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>
    
    data1.to_string(index=False, header=False)
    html_string = '''
    <html>
    <head><title>Short Listed Students</title></head>
    <link rel="stylesheet" type="text/css" href="static/df_style.css"/>
    <body>
    <marquee behavior="alternate">
    <h1 style="color:salmon;font-family:Times New Roman; font-weight:bolder; font-size:40px;">SELECTED STUDENTS :)</h1>
    </marquee>
    <center>{table}</center>
    </body>
    </html>.
    '''
    data1.insert(loc=0, column='Sr.no', value=np.arange(1,len(data1)+1))
    # OUTPUT AN HTML FILE
    with open('static/myhtml.html', 'w') as f:
        f.write(html_string.format(table=data1.to_html(classes='mystyle',index=False)))
    return app.send_static_file('myhtml.html')
if __name__ == "__main__":
    app.run()