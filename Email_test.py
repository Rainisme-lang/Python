#寄送 Email 的程式
#準備訊息物件設定
import email.message
msg = email.message.EmailMessage()
msg["From"] = "m3xu6rain@gmail.com"
msg["To"] = "m3xu6rain@gmail.com"
msg["Subject"] = "嗨嗨,雨璃仔"

#寄送純文字的內容
msg.set_content("來騷擾看看")

#寄送較多樣式的內容(html)
msg.add_alternative("<h3>優惠券</h3>滿五百送一百", subtype = "html")

#連線到 SMTP Server,驗證寄件人身分並發送郵件
import smtplib
#到網路上搜尋 gmail smtp server 或是 yahoo smtp server
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("m3xu6rain@gmail.com","aaa22066559")
server.send_message(msg)
server.close()