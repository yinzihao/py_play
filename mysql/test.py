import DMysql
db = DMysql.DMysql()
res = db.findArr('select * from t_keywords limit 2')
print res