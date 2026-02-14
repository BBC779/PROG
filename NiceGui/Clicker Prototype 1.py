from nicegui import ui

score = 0
points_per_click = 1
upgrade_cost = 10
upgrade_cost_2 = 100
upgrade_cost_3 = 1000
upgrade_cost_4 = 10000
upgrade_cost_5 = 100000
upgrade_cost_6 = 1000000
upgrade_cost_7 = 10000000
upgrade_cost_8 = 100000000
upgrade_cost_9 = 1000000000
upgrade_cost_10 = 10000000000
upgrade_cost_11 = 100000000000
upgrade_cost_12 = 1000000000000
upgrade_cost_13 = 10000000000000
upgrade_cost_14 = 100000000000000
upgrade_cost_15 = 1000000000000000

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

def buy_upgrade_8():
    global score, points_per_click, upgrade_cost_8
    if score >= upgrade_cost_8:
        score -= upgrade_cost_8
        points_per_click += 10000000
        upgrade_cost_8 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_8.set_text(f'Upgrade (+10000000/click) Cost: {upgrade_cost_8}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_9():
    global score, points_per_click, upgrade_cost_9
    if score >= upgrade_cost_9:
        score -= upgrade_cost_9
        points_per_click += 100000000
        upgrade_cost_9 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_9.set_text(f'Upgrade (+100000000/click) Cost: {upgrade_cost_9}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_10():
    global score, points_per_click, upgrade_cost_10
    if score >= upgrade_cost_10:
        score -= upgrade_cost_10
        points_per_click += 1000000000
        upgrade_cost_10 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_10.set_text(f'Upgrade (+1000000000/click) Cost: {upgrade_cost_10}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_11():
    global score, points_per_click, upgrade_cost_11
    if score >= upgrade_cost_11:
        score -= upgrade_cost_11
        points_per_click += 10000000000
        upgrade_cost_11 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_11.set_text(f'Upgrade (+10000000000/click) Cost: {upgrade_cost_11}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_12():
    global score, points_per_click, upgrade_cost_12
    if score >= upgrade_cost_12:
        score -= upgrade_cost_12
        points_per_click += 100000000000
        upgrade_cost_12 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_12.set_text(f'Upgrade (+100000000000/click) Cost: {upgrade_cost_12}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_13():
    global score, points_per_click, upgrade_cost_13
    if score >= upgrade_cost_13:
        score -= upgrade_cost_13
        points_per_click += 1000000000000
        upgrade_cost_13 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_13.set_text(f'Upgrade (+1000000000000/click) Cost: {upgrade_cost_13}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_14():
    global score, points_per_click, upgrade_cost_14
    if score >= upgrade_cost_14:
        score -= upgrade_cost_14
        points_per_click += 10000000000000
        upgrade_cost_14 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_14.set_text(f'Upgrade (+10000000000000/click) Cost: {upgrade_cost_14}')
        ppc_label.set_text(f'Points per click: {points_per_click}')

def buy_upgrade_15():
    global score, points_per_click, upgrade_cost_15
    if score >= upgrade_cost_15:
        score -= upgrade_cost_15
        points_per_click += 100000000000000
        upgrade_cost_15 *= 2
        score_label.set_text(f'Score: {score}')
        upgrade_label_15.set_text(f'Upgrade (+100000000000000/click) Cost: {upgrade_cost_15}')
        ppc_label.set_text(f'Points per click: {points_per_click}')


score_label = ui.label('Score: 0')
ppc_label = ui.label('Points per click: 1')
upgrade_label = ui.label('Upgrade (+1/click) Cost: 10')
upgrade_label_2 = ui.label('Upgrade 2 (+10/click) Cost: 100')
upgrade_label_3 = ui.label('Upgrade 3 (+100/click) Cost: 1k')
upgrade_label_4 = ui.label('Upgrade 4 (+1k/click) Cost: 10k')
upgrade_label_5 = ui.label('Upgrade 5 (+10k/click) Cost: 100k')
upgrade_label_6 = ui.label('Upgrade 6 (+100k/click) Cost: 1m')
upgrade_label_7 = ui.label('Upgrade 7 (+1m/click) Cost: 10m')
upgrade_label_8 = ui.label('Upgrade 8 (+10m/click) Cost: 100m')
upgrade_label_9 = ui.label('Upgrade 9 (+100m/click) Cost: 1b')
upgrade_label_10 = ui.label('Upgrade 10 (+1b/click) Cost: 10b')
upgrade_label_11 = ui.label('Upgrade 10 (+10b/click) Cost: 100b')
upgrade_label_12 = ui.label('Upgrade 11 (+100b/click) Cost: 1t')
upgrade_label_13 = ui.label('Upgrade 12 (+1t/click) Cost: 10t')
upgrade_label_14 = ui.label('Upgrade 13 (+10t/click) Cost: 100t')
upgrade_label_15 = ui.label('Upgrade 14 (+100t/click) Cost: 1q')

ui.button('CLICK', on_click=click).classes('text-lg').props("flat").style("color:White;")
ui.button('Buy Upgrade', on_click=buy_upgrade).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 2', on_click=buy_upgrade_2).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 3', on_click=buy_upgrade_3).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 4', on_click=buy_upgrade_4).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 5', on_click=buy_upgrade_5).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 6', on_click=buy_upgrade_6).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 7', on_click=buy_upgrade_7).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 8', on_click=buy_upgrade_7).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 9', on_click=buy_upgrade_7).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 10', on_click=buy_upgrade_7).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 11', on_click=buy_upgrade_7).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 12', on_click=buy_upgrade_7).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 13', on_click=buy_upgrade_7).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 14', on_click=buy_upgrade_7).classes('text-lg').props("flat").style("color:black;")
ui.button('Buy Upgrade 15', on_click=buy_upgrade_7).classes('text-lg').props("flat").style("color:black;")

ui.run(native=True)