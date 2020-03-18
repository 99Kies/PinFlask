from flask import Flask, render_template_string
from flask import render_template, request, flash, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import base64

app = Flask(__name__)
app.config[ "SECRET_KEY"] =  "s_e_c_r_e_t_k_e_y_h_u_c_t_f "
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    text = StringField( "BASE64加密",validators= [DataRequired()])
    submit = SubmitField( "提交")

class NameForm1(FlaskForm):
    text = StringField("BASE64解密",validators= [DataRequired()])
    submit = SubmitField("提交")

def waf(str):
    black_list = ['flag','os','system','popen','import','eval','chr','request','subprocess','commands','socket','hex','base64']
    for x in black_list :
        if x in str.lower() :
            return 1


@app.route( "/hint",methods=[ "GET"])
def hint():
    txt = '失败奈成功她妈'
    return render_template('hint.html',txt = txt)


@app.route( "/",methods=[ "POST", "GET"])
def encode():
    if request.values.get( "text"):
        text = request.values.get('text')
        text_decode = base64.b64encode(text.encode())
        tmp = '结果 :{0}'.format(str(text_decode.decode()))
        res =  render_template_string(tmp)
        flash(tmp)
        return redirect(url_for( "encode"))

    else:
        text = ''
        form = NameForm(text)
        return render_template('encode.html',form = form ,method = 'GET')

@app.route( "/decode",methods=[ "POST", "GET"])
def decode():
    if request.values.get( "text") :
        text = request.values.get('text')
        text_decode = base64.b64decode(text.encode())
        tmp = '结果 {0}'.format(text_decode.decode())
        if waf(tmp) :
            flash('no no no !!')
            return redirect(url_for( "decode"))
        res =  render_template_string(tmp)
        flash( res )
        return redirect(url_for( "decode"))

    else :
        text = ''
        form = NameForm1(text)
        return render_template('decode.html',form = form)



@app.errorhandler(400)
def bad_request(e):
    return render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ ==  "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
