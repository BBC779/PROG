from nicegui import ui
import math

score = 0
points_per_click = 1
rebirth_points = 0
rebirth_multiplier = 1.0
REBIRTH_BASE_REQUIREMENT = 5_000_000
clicks_per_second = 0

score_label = None
ppc_label = None
rebirth_label = None
multiplier_label = None
cps_label = None
rebirth_button = None

UPGRADES_DATA = {}
AUTO_CLICKERS = {}

for i in range(1, 21):
    UPGRADES_DATA[i] = {
        'name': f'Clicker {i}',
        'base_cost': 10 * (5 ** (i - 1)),
        'ppc_increase': 1 * (10 ** (i - 1))
    }

for i in range(1, 21):
    AUTO_CLICKERS[100 + i] = {
        'name': f'Auto Clicker {i}',
        'base_cost': 500 * (6 ** (i - 1)),
        'cps': 5 * (10 ** (i - 1))
    }

for u in {**UPGRADES_DATA, **AUTO_CLICKERS}.values():
    u['current_cost'] = u['base_cost']
    u['ui_label'] = None
    u['ui_button'] = None

def format_number(n):
    if n >= 1e15: return f'{n/1e15:.1f}q'
    if n >= 1e12: return f'{n/1e12:.1f}t'
    if n >= 1e9: return f'{n/1e9:.1f}b'
    if n >= 1e6: return f'{n/1e6:.1f}m'
    if n >= 1e3: return f'{n/1e3:.1f}k'
    return str(int(n))

def rebirth_requirement():
    return REBIRTH_BASE_REQUIREMENT * (2.5 ** rebirth_points)

def update_ui():
    if not rebirth_button:
        return

    score_label.set_text(f'Score: {format_number(score)}')
    ppc_label.set_text(f'Points per click: {format_number(points_per_click)}')
    cps_label.set_text(f'Clicks per second: {format_number(clicks_per_second)}')
    rebirth_label.set_text(f'Rebirth Points: {rebirth_points}')
    multiplier_label.set_text(f'Multiplier: x{rebirth_multiplier:.2f}')

    requirement = rebirth_requirement()
    rebirth_button.set_text(f"REBIRTH ({format_number(requirement)})")

    if score >= requirement:
        rebirth_button.enable()
    else:
        rebirth_button.disable()

    for u in {**UPGRADES_DATA, **AUTO_CLICKERS}.values():
        u['ui_label'].set_text(
            f"{u['name']} - Cost: {format_number(u['current_cost'])}"
        )
        if score >= u['current_cost']:
            u['ui_button'].enable()
        else:
            u['ui_button'].disable()

def click():
    global score
    score += points_per_click * rebirth_multiplier
    update_ui()

def auto_click():
    global score
    score += clicks_per_second * rebirth_multiplier
    update_ui()

ui.timer(1.0, auto_click)

def buy_upgrade(uid):
    global score, points_per_click, clicks_per_second

    all_upgrades = {**UPGRADES_DATA, **AUTO_CLICKERS}
    u = all_upgrades[uid]

    if score >= u['current_cost']:
        score -= u['current_cost']

        if uid in UPGRADES_DATA:
            points_per_click += u['ppc_increase']
        else:
            clicks_per_second += u['cps']

        u['current_cost'] *= 2
        update_ui()

def rebirth():
    global score, points_per_click, rebirth_points
    global rebirth_multiplier, clicks_per_second

    requirement = rebirth_requirement()
    if score < requirement:
        return

    gained = math.floor(score / requirement)

    rebirth_points += gained
    rebirth_multiplier = 1 + rebirth_points * 0.5

    score = 0
    points_per_click = 1
    clicks_per_second = 0

    for u in {**UPGRADES_DATA, **AUTO_CLICKERS}.values():
        u['current_cost'] = u['base_cost']

    update_ui()

ui.add_head_html("""
<style>
body { margin: 0; }
</style>
""")

ui.page_title("Rebirth Clicker")
ui.dark_mode().enable()

with ui.row().classes(
    'w-screen h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-black text-white p-6 gap-6 overflow-hidden'
):

    with ui.column().classes('w-96 h-full overflow-y-auto gap-3 pr-2'):
        ui.label("Click Upgrades").classes('text-2xl font-bold text-cyan-400')

        for uid, u in UPGRADES_DATA.items():
            with ui.card().classes('bg-gray-900/70 p-3'):
                u['ui_label'] = ui.label()
                u['ui_button'] = ui.button(
                    "BUY",
                    on_click=lambda id=uid: buy_upgrade(id)
                ).classes('w-full')

        ui.separator()
        ui.label("Auto Clickers").classes('text-2xl font-bold text-green-400')

        for uid, u in AUTO_CLICKERS.items():
            with ui.card().classes('bg-gray-900/70 p-3'):
                u['ui_label'] = ui.label()
                u['ui_button'] = ui.button(
                    "BUY",
                    on_click=lambda id=uid: buy_upgrade(id)
                ).classes('w-full')

    with ui.column().classes('flex-grow items-center justify-center gap-6'):
        ui.button(
            "CLICK",
            on_click=click
        ).classes(
            'text-3xl w-72 h-72 rounded-full '
            'bg-gradient-to-br from-cyan-400 to-blue-600 '
            'shadow-2xl hover:scale-105 transition duration-150'
        )

    with ui.column().classes('w-80 gap-4'):
        ui.label("Stats").classes('text-2xl font-bold text-pink-400')

        score_label = ui.label().classes('text-3xl')
        ppc_label = ui.label()
        cps_label = ui.label()
        rebirth_label = ui.label()
        multiplier_label = ui.label()

        rebirth_button = ui.button(
            "REBIRTH",
            on_click=rebirth
        ).classes('w-full text-xl mt-4')

update_ui()
ui.run()
