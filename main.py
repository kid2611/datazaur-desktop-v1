import os
username = 'pablo'
password = 'wsad1221'

print(os.environ.get("BEARER_TOKEN"))

'''
if __name__ == "__main__":

    datazaur = DataZaur(sys.argv)
    datazaur.setStyle('fusion')
    datazaur.setStyleSheet(GLOBAL_STYLE)
    datazaur.login(username, password)
    ui = FrontZaur(username, datazaur)
    ui.setStyleSheet(GLOBAL_STYLE)
    ui.show()

    sys.exit(datazaur.exec_())
'''