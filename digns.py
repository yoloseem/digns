# encoding: utf-8
import dns.resolver
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def dig():
    domain = request.args.get('domain', '').strip()
    if domain:
        try:
            answers = dns.resolver.query(domain, 'NS')
            nameservers = sorted([ans.to_text() for ans in answers])
        except Exception as e:
            error = True
        else:
            error = False
    return render_template('dig.html', **locals())
