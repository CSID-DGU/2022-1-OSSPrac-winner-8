from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')  # default URLpyt
def student():
   return render_template('input_info.html')

  

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')
      result['Univ'] = request.form.get('Univ')
      result['Student Number'] = request.form.get('Student Number')
      result['Gender'] = request.form.get('Gender')
      result['Major'] = request.form.get('Major')

      txt = ', '.join( i for i in request.form.getlist('Programming Languages'))
      result['Programming Languages'] = txt
      
      return render_template("result.html",result = result)

if __name__ == '__main__':
   #app.run()
   app.run(host='127.0.0.1', port=80)
