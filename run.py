#! /usr/bin/env python
# -*-encoding:utf-8-*-
# __author:physics

import random

from flask import Flask, render_template, flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import Required, NumberRange
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'very hard to guess string'  # 设置secret key
bootstrap = Bootstrap(app)  # 初始化bootstrap扩展


@app.route('/')
def index():
    session['number'] = random.randint(0, 1000)
    session['times'] = 10
    return render_template('index.html')


class GuessNumberForm(FlaskForm):
    number = IntegerField('请输入数字（0-1000）：', validators=[
        # 传入验证函数和相应的错误提示信息。
        Required('请输入一个有效的数字！'),
        NumberRange(0, 1000, '请输入0-1000以内的数字！')])
    submit = SubmitField('提交')


@app.route('/guess', methods=['POST', 'GET'])
def guess():
    times = session['times']  # 从session变量里面获取次数
    result = session.get('number')  # 从session变量获取index函数生成的随机数
    form = GuessNumberForm()
    if form.validate_on_submit():
        times -= 1
        session['times'] = times
        if times == 0:
            flash('你输啦......o(>...<)o')
            return redirect(url_for('index'))
        answer = form.number.data
        if answer > result:
            flash('太大了，你还有%s次机会' % times)
        elif answer < result:
            flash('太小了，你还有%s次机会' % times)
        else:
            flash('啊哈，你赢啦！VVVvvv')
            return redirect(url_for('index'))
        return redirect(url_for('guess'))
    return render_template('guess.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
