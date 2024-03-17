#Made by CoYoTe' Clan*
import PySimpleGUI as sg
from re import findall
from os import path
from webbrowser import open as openurl

currentdir = path.dirname(os.path.realpath(__file__))
file_path = path.join(currentdir, "mm_accounts.cfg")
file_path = "mm_accounts.cfg" #For Android 

def compress_numbers(string):
    numbers = list(map(int, findall(r'\d+', string)))
    numbers.sort()
    compressed = []
    start = numbers[0]
    end = numbers[0]
    for num in numbers:
        if num == 9999:
            return "*"
    
    for num in numbers[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                compressed.append(str(start))
            else:
                compressed.append(f"{start}-{end}")
            start = num
            end = num
    
    if start == end:
        compressed.append(str(start))
    else:
        compressed.append(f"{start}-{end}")
    
    return ':'.join(compressed)

def about_window():
    colm = [ [sg.Text("A simple tool made\n for configuring\n MiscMod commands groups.", justification="c")],
             [sg.Button('Discord', key="dsc")],
             [sg.Button('Github', key="ghb"), sg.Image("logo.png", expand_x=True)],
             [sg.Button('Website', key="site")],
             [sg.Text("       CoYoTe' Clan* © 2024", justification='c')] ]
    layout2 = [  [sg.Column(colm)] ]
    window2 = sg.Window(title="About", icon='icon.ico', element_justification='c', layout=layout2, modal=True, keep_on_top=True, size=(500, 500))
    
    while True:
        event, values = window2.read()
        if event == sg.WIN_CLOSED:
            break
        
        if event == 'dsc':
            openurl("https://dsc.gg/coyoteclan")
            window2.close()
            break
        if event == 'ghb':
            openurl("https://github.com/coyoteclan")
            window2.close()
            break
        if event == 'site':
            openurl("https://coyote.rf.gd")
            window2.close()
            break

sg.theme('Dark Green 5')
groups = []
default_groups = "^1Owner^7 ^3Co-Owner^7 ^4Admin^7"
users = []
default_users = "user1 user2 user3"
users_pass = ""

menu_def = [ ['File', ['Exit']], ['Help', ['About']] ]

column4 = [  [sg.Text('Set Permissions', font=("Helvetica", 12, "bold"))],
             [sg.Checkbox("All", key="9999")],
             [sg.Text('General Commands', font=("Helvetica", 10))],
            [sg.Checkbox("rename", key="5"), sg.Checkbox("logout", key="6"), sg.Checkbox("say", key="7"),
             sg.Checkbox("saym", key="8"), sg.Checkbox("sayo", key="9"), sg.Checkbox("kick", key="10")],
            [sg.Checkbox("reload", key="11"), sg.Checkbox("restart", key="12"), sg.Checkbox("endmap", key="13"),
             sg.Checkbox("map", key="14"), sg.Checkbox("status", key="15"), sg.Checkbox("mute", key="16")],
            [sg.Checkbox("unmute", key="17"), sg.Checkbox("warn", key="18"), sg.Checkbox("kill", key="19"),
             sg.Checkbox("weapon", key="20"), sg.Checkbox("heal", key="21"), sg.Checkbox("invisible", key="22")],
            [sg.Checkbox("ban", key="23"), sg.Checkbox("unban", key="24"), sg.Checkbox("pm", key="25"),
             sg.Checkbox("re", key="26"), sg.Checkbox("who", key="27")],
             [sg.Text('Fun Commands', font=("Helvetica", 10))],
            [sg.Checkbox("drop", key="28"), sg.Checkbox("spank", key="29"), sg.Checkbox("slap", key="30"), sg.Checkbox("blind", key="31"), sg.Checkbox("runover", key="32")],
            [sg.Checkbox("squash", key="33"), sg.Checkbox("rape", key="34"), sg.Checkbox("toilet", key="35"), sg.Checkbox("explode", key="36"), sg.Checkbox("mortar", key="38") ],
            [sg.Checkbox("matrix", key="39"), sg.Checkbox("burn", key="40"), sg.Checkbox("cow", key="41"), sg.Checkbox("disarm", key="42"), sg.Checkbox("freeze", key="65") ],
            [sg.Checkbox("move", key="66"), sg.Checkbox("teleport", key="62") ],
            [sg.Text('War Commands', font=("Helvetica", 10))],
            [sg.Checkbox('os', key="43"), sg.Checkbox('aw', key="44"), sg.Checkbox('omp', key="45"), sg.Checkbox('rifles', key="46"), sg.Checkbox('health', key="47"), sg.Checkbox('grenade', key="48")],
            [sg.Checkbox('pistols', key="49"), sg.Checkbox('1sk', key="50"), sg.Checkbox('roundlength', key="51")],
            [sg.Checkbox('psk', key="52"), sg.Checkbox('belmenu', key="53"), sg.Checkbox('swapteams', key="64"), sg.Checkbox('meleekill', key="61")],
            [sg.Text('More Commands', font=("Helvetica", 10))],
            [sg.Checkbox('rs', key="56"), sg.Checkbox('optimize', key="57"), sg.Checkbox('pcvar', key="58"), sg.Checkbox('respawn', key="59"), sg.Checkbox('wmap', key="60")],
            [sg.Checkbox('teambalance', key="63"), sg.Checkbox('scvar', key="67"), sg.Checkbox('bansearch', key="68"), sg.Checkbox('banlist', key="69")],
            [sg.Checkbox('reportlist', key="70"), sg.Checkbox('namechange', key="71")],
            [sg.Text('Extra Permissions', font=("Helvetica", 10))],
            [sg.InputText(key="extras", size=20, tooltip="Specify any extra permissions if you use custom commands. Otherwise, leave this empty.")],
            [sg.Button('Save Group', tooltip="Do it!")] ]
column3 = [  [sg.Text('Set Password', font=("Helvetica", 12, "bold"))],
            [sg.Combo([], enable_events=True, size=18, readonly=False, key="displayGroup"), sg.Combo([], enable_events=True, size=18, readonly=False, key="usersMenu")],
                [sg.Text('Enter Password Here', font=("Helvetica", 8))],
                [sg.InputText(key="password", tooltip="Enter password for each user one by one in the selected group and click Add. Once done, click Done and then save the group. Then do the same for other groups and users.", do_not_clear=False)],
                [sg.Button('Add', key="add", tooltip="Add this user's password."), sg.Button('Done', key="done2", tooltip="All users done for this group. Set Permissions and then click Save Group.", disabled=True)] ]

column2 = [  [sg.Text('Add Users', font=("Helvetica", 12, "bold"))],
            [sg.InputText(key="users_input", default_text=default_users, tooltip="Enter all the usernames here, seperated by spaces.")],
            [sg.Button('Ok', tooltip="Done!")] ]

#column = [sg.Text("Add Groups seperated by spaces")]
column1 = [  [sg.Text('Add Groups', font=("Helvetica", 12, "bold"))],
            [sg.InputText(key="groups_input", default_text=default_groups, tooltip="Enter all the groups here, seperated by spaces.")],
            [sg.Button('Next', tooltip="Let's Go!")] ]
layout = [  [sg.Menu(menu_def)],
            [sg.Column(column1, key="1stcol")],
            [sg.Column(column2, visible=False, key="2")],
            [sg.Column(column3, visible=False, key="3")],
            [sg.Column(column4, visible=False, key="4", scrollable=True)] ]
window = sg.Window(title="MiscMod Account Config Gen", icon="icon.ico", layout=layout, size=(760, 1000))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Exit':
        break
    if event == 'About':
        about_window()

    if event == 'Next':
        groups_input = values["groups_input"].split(" ")
        groups.extend(groups_input)
        mm_groups = ";".join(groups)
        data = f"scr_mm_groups \"{mm_groups}\"\n"
        with open(file_path, 'w') as f:
            f.write(data)
        window['Next'].update(visible=False)
        window['groups_input'].update(disabled=True)
        window['2'].update(visible=True)
        window.refresh()

    if event == 'Ok':
        users_input = values["users_input"].split(" ")
        users.extend(users_input)
        window['Ok'].update(visible=False)
        window['users_input'].update(disabled=True)
        window['3'].update(visible=True)
        window['displayGroup'].update(values=groups)
        window['displayGroup'].update(disabled=False)
        window['usersMenu'].update(values=users)
        window['1stcol'].update(visible=False)
        window['1stcol'].Widget.master.pack_forget()
        window.refresh()

    if event == 'add':
        users_pass += f"{values['usersMenu']}:{values['password']} "
        window['done2'].update(disabled=False)
        window.refresh()

    if event == 'done2':
        window['4'].update(visible=True)
        window['password'].update(disabled=True)
        window['add'].update(disabled=True)
        window['done2'].update(disabled=True)
        window.refresh()

    if event == 'Save Group':
        selected_group = values["displayGroup"]
        selected_perms = [key for key, value in values.items() if value and isinstance(window[key], sg.Checkbox)]
        perms = f":".join(selected_perms)
        perms = compress_numbers(perms)
        if perms != "*":
            perms += f":{values['extras']}"

        string = f"scr_mm_users_{selected_group} \"{users_pass.strip()}\"\nscr_mm_perms_{selected_group} \"{perms}\"\n"

        with open(file_path, 'a') as f:
            f.write(string)

        users_pass = f"" #Reset after writing current group to cfg
        string = f""
        perms = f""
        window['4'].update(visible=False)
        for key in values.keys():
            elem = window[key]
            if isinstance(elem, sg.Checkbox):
                elem.update(False)
        window['add'].update(disabled=False)
        window['password'].update(disabled=False)
        window['done2'].update(disabled=False)
        window.refresh()