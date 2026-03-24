import pickle
def Create():
    
	f=open("PASSENGERS.DAT", "wb")

	PNR=input("PNR No:")
	PName=input("Name: ")
	BRDSTN=input("Boarding at: ")
	DESTN=input("Destination: ")
	FARE=float(input("Fare: "))
    rec=[PNR,PName,BRDSTN,DESTN,FARE]
	pickle.dump(rec,f)
	f.close()
    
    
def SearchDestn(D):
    f=open("PASSENGERS.DAT", "rb")
    count=0
    try:
        while True:
            rec=pickle.load(f)
            if rec[3]==D:
                print(rec)
                count+=1
        print("Total records are": count)
    except EOFError:
        print("EOF reached")
        f.close()
    
#Question No. 36 of 2025 Question Paper (Binary File related)
#binary fine mein 2 type ke functions aate hai ek write krne ke liye aur ek read krne ke liye write krne ke liye dump function use krte hai aur read krne ke liye load function use krte hain
#binary file mein upar Create function write krne ke liye hai jabki SearchDestn read krne ke liye hai
#poora program ke pattern ko as it is samjho bas apko functions ke name, kya input lena hai user se, file ke name dhyan se dekhna hai question mein wahi use karne hai baki poora program as it is learn kr lo
#line number 22 mein condition change ho skti hai read karte time like hamein Destination match karna hai ki kis record ka destination D hai aur destination hamare record mein third index par hai then woh match karna hai yeh thoda bas record ka index dhyan se dekhna hai apne condition ke time otherwise poora program easy hai
#binary file program mein pickle module import karna na bhule
