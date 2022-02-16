import requests
import json
import codecs
from datetime import datetime
api = "https://presidentielle2022.conseil-constitutionnel.fr/telechargement/parrainagestotal.json"


def getListParr(rr):
	res= {}
	for i in rr:
		c = i["Candidat"]
		if c in res:
			res[c] += 1
		else:
			res[c] = 1

	a = sorted(res.items(), key=lambda x: x[1], reverse=True) 
	return a

def getListDept(rr):
	res2={}
	res= {}
	for i in rr:
		c = i["Candidat"]
		if c in res2:
			if i["Departement"] not in res2[c]:
				res2[c].append(i["Departement"])
				res[c] +=1
		else:
			res2[c] = [i["Departement"]]
			res[c] =1

	print(res)
	pass


	#a = sorted(res.items(), key=lambda x: x[1], reverse=True) 
	return True

def getNews():
	response = requests.get(api)

	with open("tmp.json","w") as f:
		f.write(response.text)




	rr = json.load(codecs.open('tmp.json', 'r', 'utf-8-sig'))

	a = getListParr(rr)

	getListDept(rr)
	 


	tt = []
	start_t =f"""#election22 🕊\n--Top Parrainages {datetime.today().strftime('%m/%d')}--\n\n"""
	for i in a[:5]:
		#print(i)
		start_t += f"{i[0]} : {i[1]} \n"
	
	tt.append(start_t)
	print("nb parti",len(a[5:])//5)
	print(len(a),42%5)
	for z in range(len(a[5:])//5):
		tw = ""
		for i in a[5*(z+1):5*(z+2)]:
			tw += f"{i[0]} : {i[1]} \n"
		tt.append(tw)


	return tt
	
	
if __name__ == "__main__":
	t = getNews()
	