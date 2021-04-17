import bangla
import sqlite3

con = sqlite3.connect("gk_capital")


print("enter number")
num = input()

print("enter question category")
qc = input()

print("enter question")
q = input()

print("enter answer")
ans = input()

print("enter relations")
re = input()
# insert into cap_info(number, question_category, question, answer, relations) values()
query = "insert into cap_info(number,question_category, question, answer,relations) values("+num+",'"+qc+"','"+q+"','"+ans+"','"+re+"')"
con.execute(query)
con.commit()

con.close()

print("data saved...")