letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''

a = letter.replace("<|Name|>", "Aarish").replace("<|Date|>", "24 Spet, 2024")
print(a)