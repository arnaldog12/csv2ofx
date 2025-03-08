import itertools as it
from operator import itemgetter

from meza.io import IterStringIO, read_csv, write

from csv2ofx.ofx import OFX
from csv2ofx.utils import gen_data

mapping = dict(
    bank="InfinitePay",
    bank_id="542",
    delimiter=",",
    account="CHECKING",
    account_id="14099972-6",
    currency="BRL",
    parse_fmt="%d/%m/%Y",
    date=itemgetter("Data"),
    amount=itemgetter("Valor"),
    payee=itemgetter("Detalhe"),
    balance="0,00",
    ms_money=True,
)

ofx = OFX(mapping)

records = read_csv("InfinitePay 01-02-2025 a 28-02-2025.csv", has_header=True)

groups = ofx.gen_groups(records)
trxns = ofx.gen_trxns(groups)
cleaned_trxns = ofx.clean_trxns(trxns)
data = gen_data(cleaned_trxns)
content = it.chain([ofx.header(language="POR"), ofx.gen_body(data), ofx.footer()])

# for line in IterStringIO(content):
#     print(line)

write("output.ofx", IterStringIO(content), overwrite=True, encoding="utf-8")
