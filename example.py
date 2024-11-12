import pandas as pd
import numpy as np

length = 400

data = []
genders = ["male","female"]
second_genders = ["omega","beta"]
hierarchies = ["proletariat","worker"]

tests =[
		[genders[0],second_genders[0],hierarchies[0]],
		[genders[0],second_genders[1],hierarchies[1]],
		[genders[1],second_genders[0],hierarchies[1]],
		[genders[1],second_genders[1],hierarchies[0]],
	]

for t in tests:
	g = t[0]
	s = t[1]
	h = t[2]
	for _ in range(length):
		cash = np.random.random() * 1000
		if s == "omega":
			r = np.random.randint(100,300)
			cash += r
		
		if h == "worker":
			r = np.random.randint(100,600)
			cash -= 500
			while cash < 0:
				cash += np.random.randint(5,30)
		
		cash = int(cash)
		a = {"gender":g,"second_gender":s,"hierarchy":h,"cash":cash}
		data.append(a)
df = pd.DataFrame(data)
df.to_csv('example.csv', index=False, encoding='utf-8-sig')