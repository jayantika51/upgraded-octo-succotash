from tkinter import*
import requests
import json

root=Tk()
root.geometry("500x500")
root.overrideredirect(True)

api_requests = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=1781667086854123978237913ab90263" )
open_bbc_page = json.loads(api_request.content)


newsupdate=Label(root, text="BBC News Update",font=("Gill Sans MT",40,'bold'))
newsupdate.place(relx=0, rely=10, anchor=CENTER)

news1=Label(root, text="Title 1",font = ('arial',' 13',', bold'))
news1.place(relx=0, rely=8, anchor=LEFT)
news_desc1(root, text="Description", wraplength=500)
news_desc1.place(relx=0, rely=7, anchor=CENTER)

news2=Label(root, text="Title 2",font = ('arial',' 13',', bold'))
news2.place(relx=0, rely=5, anchor=LEFT)
news_desc2(root, text="Description", wraplength=500)
news_desc2.place(relx=0, rely=4, anchor=CENTER)

news3=Label(root, text="Title 3",font = ('arial',' 13',', bold'))
news3.place(relx=0, rely=2, anchor=LEFT)
news3_desc3(root, text="Description", wraplength=500)
news3_desc3.place(relx=0, rely=1, anchor=CENTER)

news4=Label(root, text="Title 4",font = ('arial',' 13',', bold'))
news4.place(relx=0, rely=0.1, anchor=LEFT)
news_desc4(root, text="Description", wraplength=500)
news_desc4.place(relx=0, rely=0.2, anchor=CENTER)

news5=Label(root, text="Title5",font = ('arial',' 13',', bold'))
news5.place(relx=0, rely=0.4, anchor=LEFT)
news_desc5(root, text="Description", wraplength=500)
news_desc5.place(relx=0, rely=0.5, anchor=CENTER)

title1=open_bbc_page["articles"][0]["description"]
print(title1)

title2=open_bbc_page["articles"][1]["description"]
print(title2)

title3=open_bbc_page["articles"][2]["description"]
print(title3)

title4=open_bbc_page["articles"][3]["description"]
print(title4)

title5=open_bbc_page["articles"][4]["description"]
print(title5)

desc1=open_bbc_page["articles"][0]["description"]
print(title1)

desc2=open_bbc_page["articles"][1]["description"]
print(title2)

desc3=open_bbc_page["articles"][2]["description"]
print(title3)

desc4=open_bbc_page["articles"][3]["description"]
print(title4)

desc5=open_bbc_page["articles"][4]["description"]
print(title5)



root.mainloop()