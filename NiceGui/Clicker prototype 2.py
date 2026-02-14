from nicegui import ui

score = 0
points_per_click = 1
points_per_second = 0

UPGRADES_DATA = {
    1: {'name': 'Cursor (+1/click)', 'base_cost': 10, 'ppc_increase': 1, 'current_cost': 10, 'ui_label': None, 'ui_button': None},
    2: {'name': 'Grandma (+10/click)', 'base_cost': 100, 'ppc_increase': 10, 'current_cost': 100, 'ui_label': None, 'ui_button': None},
    3: {'name': 'Farm (+100/click)', 'base_cost': 1000, 'ppc_increase': 100, 'current_cost': 1000, 'ui_label': None, 'ui_button': None},
    4: {'name': 'Mine (+1k/click)', 'base_cost': 10000, 'ppc_increase': 1000, 'current_cost': 10000, 'ui_label': None, 'ui_button': None},
    5: {'name': 'Factory (+10k/click)', 'base_cost': 100000, 'ppc_increase': 10000, 'current_cost': 100000, 'ui_label': None, 'ui_button': None},
    6: {'name': 'Bank (+100k/click)', 'base_cost': 1000000, 'ppc_increase': 100000, 'current_cost': 1000000, 'ui_label': None, 'ui_button': None},
    7: {'name': 'Temple (+1m/click)', 'base_cost': 10000000, 'ppc_increase': 1000000, 'current_cost': 10000000, 'ui_label': None, 'ui_button': None},
    8: {'name': 'Wizard Tower (+10m/click)', 'base_cost': 100000000, 'ppc_increase': 10000000, 'current_cost': 100000000, 'ui_label': None, 'ui_button': None},
    9: {'name': 'Shipment (+100m/click)', 'base_cost': 1000000000, 'ppc_increase': 100000000, 'current_cost': 1000000000, 'ui_label': None, 'ui_button': None},
    10: {'name': 'Alchemy Lab (+1b/click)', 'base_cost': 10000000000, 'ppc_increase': 1000000000, 'current_cost': 10000000000, 'ui_label': None, 'ui_button': None},
    11: {'name': 'Portal (+10b/click)', 'base_cost': 100000000000, 'ppc_increase': 10000000000, 'current_cost': 100000000000, 'ui_label': None, 'ui_button': None},
    12: {'name': 'Time Machine (+100b/click)', 'base_cost': 1000000000000, 'ppc_increase': 100000000000, 'current_cost': 1000000000000, 'ui_label': None, 'ui_button': None},
    13: {'name': 'Antimatter Condenser (+1t/click)', 'base_cost': 10000000000000, 'ppc_increase': 1000000000000, 'current_cost': 10000000000000, 'ui_label': None, 'ui_button': None},
    14: {'name': 'Prism (+10t/click)', 'base_cost': 100000000000000, 'ppc_increase': 10000000000000, 'current_cost': 100000000000000, 'ui_label': None, 'ui_button': None},
    15: {'name': 'Chrono Scepter (+100t/click)', 'base_cost': 1000000000000000, 'ppc_increase': 100000000000000, 'current_cost': 1000000000000000, 'ui_label': None, 'ui_button': None},
}

def format_number(n):
    if n >= 1e15: return f'{n/1e15:.1f}q'
    if n >= 1e12: return f'{n/1e12:.1f}t'
    if n >= 1e9: return f'{n/1e9:.1f}b'
    if n >= 1e6: return f'{n/1e6:.1f}m'
    if n >= 1e3: return f'{n/1e3:.1f}k'
    return str(n)

score_label = None
ppc_label = None

def update_ui_elements():
    global score
    score_label.set_text(f'Score: {format_number(score)}')
    ppc_label.set_text(f'Points per click: {format_number(points_per_click)}')
    
    for uid in UPGRADES_DATA:
        upgrade = UPGRADES_DATA[uid]
        can_afford = score >= upgrade['current_cost']
        upgrade['ui_label'].set_text(f'{upgrade["name"]} Cost: {format_number(upgrade["current_cost"])}')
        upgrade['ui_button'].props(f'color={"positive" if can_afford else "dark"}')
        upgrade['ui_button'].disable() if not can_afford else upgrade['ui_button'].enable()

def click():
    global score
    score += points_per_click
    update_ui_elements()

def buy_upgrade_handler(upgrade_id):
    global score, points_per_click
    upgrade = UPGRADES_DATA[upgrade_id]
    
    if score >= upgrade['current_cost']:
        score -= upgrade['current_cost']
        points_per_click += upgrade['ppc_increase']
        upgrade['current_cost'] *= 2 
        ui.notify(f"Purchased {upgrade['name']}!", type='positive')
        update_ui_elements()
    else:
        ui.notify("Not enough score!", type='negative')

ui.page_title('NiceGUI Clicker Game')
ui.dark_mode().enable()

with ui.row().classes('w-full h-screen p-4 gap-4 bg-gray-900 text-white'):

    with ui.column().classes('w-72 gap-3 h-full overflow-y-auto pr-2'):
        ui.label('Upgrades Market').classes('text-xl font-bold sticky top-0 bg-gray-900 py-2 z-10')

        for uid in UPGRADES_DATA:
            upgrade = UPGRADES_DATA[uid]
            with ui.card().classes('w-full bg-gray-700 hover:bg-gray-600 cursor-pointer transition-colors').props('flat bordered'):
                with ui.column().classes('p-3'):
                    upgrade['ui_label'] = ui.label(f'{upgrade["name"]} Cost: {format_number(upgrade["current_cost"])}').classes('text-sm')
                    upgrade['ui_button'] = ui.button('BUY', on_click=lambda id=uid: buy_upgrade_handler(id)) \
                                             .classes('w-full mt-2')

    with ui.column().classes('flex-grow items-center justify-center gap-6'):
        ui.button('CLICK ME!', on_click=click) \
          .classes('text-2xl w-64 h-64 rounded-full shadow-2xl hover:scale-105 transform transition duration-150') \
          .props('color=primary size=xl')

    with ui.column().classes('w-64 gap-3'):
        ui.label('Game Stats').classes('text-xl font-bold mb-2')
        
        with ui.card().classes('w-full p-4 bg-gray-700'):
            score_label = ui.label('Score: 0').classes('text-3xl font-mono')
        
        with ui.card().classes('w-full p-4 bg-gray-700'):
            ppc_label = ui.label('Points per click: 1').classes('text-lg')

update_ui_elements()

ui.run()