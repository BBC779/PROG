from nicegui import ui

score = 0
points_per_click = 1
upgrade_cost = 10
upgrade_cost_2 = 100
upgrade_cost_3 = 1000
upgrade_cost_4 = 1000
upgrade_cost_5 = 1000
upgrade_cost_6 = 1000
upgrade_cost_7 = 1000

def click():
    global score
    score += points_per_click
    score_label.set_text(f'Score: {score}')

def buy_upgrade():
    global score, points_per_click, upgrade_cost
    if score >= upgrade_cost:
        score -= upgrade_cost
        points_per_click += 1
        upgrade_cost *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label.set_text(f'Upgrade (+1/click) Cost: {upgrade_cost}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_2():
    global score, points_per_click, upgrade_cost_2
    if score >= upgrade_cost_2:
        score -= upgrade_cost_2
        points_per_click += 10
        upgrade_cost_2 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_2.set_text(f'Upgrade (+10/click) Cost: {upgrade_cost_2}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_3():
    global score, points_per_click, upgrade_cost_3
    if score >= upgrade_cost_3:
        score -= upgrade_cost_3
        points_per_click += 100
        upgrade_cost_3 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_3.set_text(f'Upgrade (+100/click) Cost: {upgrade_cost_3}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_4():
    global score, points_per_click, upgrade_cost_4
    if score >= upgrade_cost_4:
        score -= upgrade_cost_4
        points_per_click += 1000
        upgrade_cost_4 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_4.set_text(f'Upgrade (+1000/click) Cost: {upgrade_cost_4}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_5():
    global score, points_per_click, upgrade_cost_5
    if score >= upgrade_cost_5:
        score -= upgrade_cost_5
        points_per_click += 10000
        upgrade_cost_5 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_5.set_text(f'Upgrade (+10000/click) Cost: {upgrade_cost_5}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_6():
    global score, points_per_click, upgrade_cost_6
    if score >= upgrade_cost_6:
        score -= upgrade_cost_6
        points_per_click += 100000
        upgrade_cost_6 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_6.set_text(f'Upgrade (+100000/click) Cost: {upgrade_cost_6}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_7():
    global score, points_per_click, upgrade_cost_7
    if score >= upgrade_cost_7:
        score -= upgrade_cost_7
        points_per_click += 1000000
        upgrade_cost_7 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_7.set_text(f'Upgrade (+1000000/click) Cost: {upgrade_cost_7}')
        ppc_label.set_text(f'Points per click: {points_per_click}')


score_label = ui.label('Score: 0')
ppc_label = ui.label('Points per click: 1')
upgrade_label = ui.label('Upgrade (+1/click) Cost: 10')
upgrade_label_2 = ui.label('Upgrade 2 (+10/click) Cost: 100')
upgrade_label_3 = ui.label('Upgrade 3 (+100/click) Cost: 1000')
upgrade_label_4 = ui.label('Upgrade 4 (+1000/click) Cost: 10000')
upgrade_label_5 = ui.label('Upgrade 5 (+10000/click) Cost: 100000')
upgrade_label_6 = ui.label('Upgrade 6 (+100000/click) Cost: 1000000')
upgrade_label_7 = ui.label('Upgrade 7 (+1000000/click) Cost: 10000000')

ui.button('CLICK', on_click=click).classes('text-lg').props("flat").style("color:White;")
ui.button('Buy Upgrade', on_click=buy_upgrade).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 2', on_click=buy_upgrade_2).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 3', on_click=buy_upgrade_3).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 4', on_click=buy_upgrade_4).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 5', on_click=buy_upgrade_5).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 6', on_click=buy_upgrade_6).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 7', on_click=buy_upgrade_7).classes('text-lg').props("flat").style("color:black;")

ui.run(native=True)