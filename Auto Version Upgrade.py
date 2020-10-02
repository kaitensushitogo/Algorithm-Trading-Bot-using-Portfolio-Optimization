# 번개 자동 버전 처리 스크립트
from pywinauto import application, timings
import os, time

# 실전투자 여부
REAL_TRADING = False

app = application.Application()
app.start('C:/KiwoomFlash3/bin/nkministarter.exe')

title = "번개3 Login"
dlg = timings.wait_until_passes(30, 0.5, lambda: app.window(title=title))

id_ctrl = dlg.Edit0
id_ctrl.set_focus()
id_ctrl.type_keys('/Your Account ID/')

pass_ctrl = dlg.Edit2
pass_ctrl.set_focus()
pass_ctrl.type_keys('/Your Password/')

btn_ctrl = dlg.Button0
btn_ctrl.click()

time.sleep(1)

dlg2 = timings.wait_until_passes(20, 0.5, lambda: app.window(title='번개3'))
btn_ctrl2 = dlg2.Button1
btn_ctrl2.click()

time.sleep(20)
os.system("taskkill /im nkmini.exe /f")