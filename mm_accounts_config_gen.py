#Made by CoYoTe' Clan*
import PySimpleGUI as sg

sg.theme('Dark Green 5')
groups = []
users = []
users_pass = f""
column4 = [  [sg.Text('Set Permissions', font=("Helvetica", 12, "bold"))],
             [sg.Text('General Commands', font=("Helvetica", 12))],
            [sg.Checkbox("rename", key="5"), sg.Checkbox("logout", key="6"), sg.Checkbox("say", key="7"),
             sg.Checkbox("saym", key="8"), sg.Checkbox("sayo", key="9"), sg.Checkbox("kick", key="10")],
            [sg.Checkbox("reload", key="11"), sg.Checkbox("restart", key="12"), sg.Checkbox("endmap", key="13"),
             sg.Checkbox("map", key="14"), sg.Checkbox("status", key="15"), sg.Checkbox("mute", key="16")],
            [sg.Checkbox("unmute", key="17"), sg.Checkbox("warn", key="18"), sg.Checkbox("kill", key="19"),
             sg.Checkbox("weapon", key="20"), sg.Checkbox("heal", key="21"), sg.Checkbox("invisible", key="22")],
            [sg.Checkbox("ban", key="23"), sg.Checkbox("unban", key="24"), sg.Checkbox("pm", key="25"),
             sg.Checkbox("re", key="26"), sg.Checkbox("who", key="27")],
             [sg.Text('Fun Commands', font=("Helvetica", 12))],
            [sg.Checkbox("drop", key="28"), sg.Checkbox("spank", key="29"), ]]
column3 = [  [sg.Text('Set Password', font=("Helvetica", 12, "bold"))],
            [sg.Combo([], enable_events=True, expand_x=True, readonly=False, key="displayGroup"), sg.Combo([], enable_events=True, readonly=False, key="usersMenu")],
                [sg.Text('Enter Password Here', font=("Helvetica", 12))],
                [sg.InputText(key="password")],
                [sg.Button('Add')],
                [sg.Button('Save', visible=False)] ]

column2 = [  [sg.Text('Add Users', font=("Helvetica", 12, "bold"))],
            [sg.Text('Enter space seperated names', font=("Helvetica", 8))],
            [sg.InputText(key="users_input")],
            [sg.Button('Ok')] ]

#column = [sg.Text("Add Groups seperated by spaces")]
column1 = [  [sg.Text('Add Groups', font=("Helvetica", 12, "bold"))],
            [sg.Text('seperate using spaces', font=("Helvetica", 8)), sg.InputText(key="groups_input")],
            [sg.Button('Next')] ]
layout = [  [sg.Column(column1)],
            [sg.Column(column2, visible=False, key="2")],
            [sg.Column(column3, visible=False, key="3")],
            [sg.Column(column4, visible=True, key="4")] ]
window = sg.Window(title="MiscMod Account Config Gen", layout=layout, size=(650, 600))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Next':
        #window.ding(display_number = 0)
        groups_input = values["groups_input"].split(" ")
        groups.extend(groups_input)
        mm_groups = ";".join(groups)
        data = f"scr_mm_groups \"{mm_groups}\"\n"
        with open("mm_accounts.cfg", 'w') as f:
            f.write(data)
        window['Next'].update(visible=False)
        window['2'].update(visible=True)
        window.refresh()
        #addUsers(groups)
        #break
    if event == 'Ok':
        users_input = values["users_input"].split(" ")
        users.extend(users_input)
        window['Ok'].update(visible=False)
        window['3'].update(visible=True)
        window['displayGroup'].update(values=groups)
        window['displayGroup'].update(disabled=False)
        window['usersMenu'].update(values=users)
        window.refresh()
    if event == 'Add':
        pass_input = values["password"]
        selected_user = values["usersMenu"]
        users_pass += f" {selected_user}:{pass_input}"
        window['Save'].update(visible=True)
    if event == 'Save':
        with open("mm_accounts.cfg", 'a') as f:
            selected_group = values["displayGroup"]
            string = f"scr_mm_users_{selected_group} \"{users_pass}\"\n"
            f.write(string)
            users_pass = f""#Reset the string after writing current group to cfg
            string = f""
