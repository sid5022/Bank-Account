
import pandas as pd
class Accounts:
	def __init__(self,name,ac_no,ac_type,bal):
		self.name = name
		self.ac_no = ac_no
		self.ac_type = ac_type
		self.bal = bal
		self.acs = [35074678527,20098671545,62364231428]
		self.hist = [["Start",self.ac_no,"----","----","----",self.bal]]

	def summary(self):
		ac = pd.DataFrame([[self.name,self.ac_no,self.ac_type,self.bal]],
			     columns = [["Name","A/c Number","A/c Type","Balance"]],
			     index = [" "])
		print("\n",ac,"\n")

	def debit(self,orgd,wd,dr):
		self.orgd = orgd
		self.wd = wd
		self.dr = dr
		self.bal -= self.dr
		self.hist.insert(0,[self.orgd,self.wd,
				"Payment gateway",self.dr,"----",self.bal])

	def credit(self,orgc,wc,cr):
		self.orgc = orgc
		self.wc = wc
		self.cr = cr
		self.bal += self.cr
		self.hist.insert(0,[self.orgc,self.wc,
				"A/c credit","----",self.cr,self.bal])

	def salary(self):
		self.sal = 230000
		self.bal += self.sal
		self.hist.insert(0,["Intel","www.intel.com",
				"Bulk posting","----",self.sal,self.bal])

	def tax(self):
		self.tx = 9500
		self.bal -= self.tx
		self.hist.insert(0,["Govt. of India","Income Tax",
				"TAX",self.tx,"----",self.bal])

	def bill(self): 
		self.bl = 20000
		self.bal -= self.bl
		self.hist.insert(0,["WBSEDCL","Electric bill",
				"UPI",self.bl,"----",self.bal])

	def Transfer(self):
		print("Hello Mr. "+self.name+"!")
		i = 3
		while i > 0:
			print(str(i)+" attempts left!!")
			num = int(input("Enter A/c number of recipient: "))
			if num in self.acs:
				break
			i = i-1
		if num in self.acs:
			amount = int(input("Enter amount: "))
		self.bal -= amount
		c[self.acs.index(num)].bal += amount
		self.hist.insert(0,[c[self.acs.index(num)].name,
				num,"A/c transfer",amount,"----",self.bal])
		c[self.acs.index(num)].hist.insert(0,[self.name,
				self.ac_no,"A/c transfer",
				"----",amount,c[self.acs.index(num)].bal])

	def history(self):
		col = ["Organisation","A/c info","Description",
				"Debit","Credit","Balance"]
		H = pd.DataFrame(self.hist, columns = col,
						index = [" "]*len(self.hist))
		print("Transaction History of Mr. "+self.name)
		print(H,"\n")

sid = Accounts("Siddhartha Sarkar",35074678527,"Salary",960730)
sou = Accounts("Sourav Sarkar",20098671545,"Savings",536520)
ram = Accounts("Ram Chandra",62364231428,"Current",302560)
c = [sid,sou,ram]

sid.salary()
sid.tax()
sid.bill()
sid.credit("IITKGP","www.iitkgp.ac.in",56000)
sid.Transfer()
sid.debit("Amazon","www.amazon.com",15560)
sid.debit("IRCTC","www.irctc.co.in",6540)
sou.debit("LIC","www.lic.in",3500)
sou.debit("Myntra","www.myntra.com",7600)
sou.credit("R/D","Self",15975)
sou.Transfer()
sid.debit("Myntra","www.myntra.com",3550)
print("\n")
sou.history()
sid.history()
