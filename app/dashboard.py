from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import json
import random
from flask_login import login_required
from .watcher.read import Reader
from .resources.strage import Strag
dashboard_page = Blueprint('dashboard', 'dashboard', template_folder='templates')
# gf=gf_API()
sg=Strag()
rd=Reader()
@dashboard_page.route('/')
@login_required
def get_sample():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


@dashboard_page.route('/account',methods=['POST'])
def get_account():
    # cols=['股票名称','现价','持有','可用','成本','市值','类型']
    cols=[
        { 'field': 'id', 'headerName': 'ID', 'flex': 0.5 },
        { 'field': 'stockclass', 'headerName': '类型', 'flex': 1 },
        { 'field': 'stockname', 'headerName': '股票名称', 'flex': 1 },
        { 'field': 'stockcode', 'headerName': '代码', 'flex': 1 },
        { 'field': 'price', 'headerName': '现价', 'flex': 1 },
        { 'field': 'cost', 'headerName': '成本', 'flex': 1 },
        { 'field': 'has', 'headerName': '持有', 'flex': 1 },
        { 'field': 'canuse', 'headerName': '可用', 'flex': 1},
        { 'field': 'value', 'headerName': '市值', 'flex': 1},
        { 'field': 'profit', 'headerName': '盈亏', 'flex': 1},
        { 'field': 'rate', 'headerName': '盈亏率', 'flex': 1},
        { 'field': 'risk', 'headerName': '建议仓位', 'flex': 1}
    ]
    rows=rd.read_positions()

    data={'cols':cols,'rows':rows}
    return json.dumps(data)

@dashboard_page.route('/stock',methods=['POST'])
def get_stock():
    pass