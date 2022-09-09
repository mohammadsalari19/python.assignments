
text = input('matn ra vared konid : ')

text_split = input('matn  ba ch reshte joda shvad : ')

text_join = input('matn ba ch rashte vasl shavad : ')

matn = text.split(text_split)
matn = text_join.join(matn)

print(matn)