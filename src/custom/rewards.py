from mission_report.constants import Coalition
from mission_report.statuses import LifeStatus, BotLifeStatus, SortieStatus

"""
examples:

# Tour awards
# available parameters stats/models.py/class Player


# streak 100 or more
def fighter_ace(player):
    return player.streak_max >= 100


# total air kills 20 or more
def example_2(player):
    if player.ak_total >= 20:
        return True


# 20 air kills and 200 ground kills
def example_3(player):
    return player.ak_total >= 20 and player.gk_total >= 200


# Sortie awards
# available parameters stats/models.py/class Sortie


# 5 air kills in one sortie
def fighter_hero(sortie):
    return sortie.ak_total >= 5


# Mission awards
# available parameters stats/models.py/class PlayerMission


# 10 air kills in one mission
def mission_fighter_hero(player_mission):
    return player_mission.ak_total >= 15

"""


# streak 100 or more
def fighter_ace(player):
    return player.streak_max >= 100


# 5 air kills in one sortie
def fighter_hero(sortie):
    return sortie.ak_total >= 5


# 15 air kills in one mission
def mission_hero(player_mission):
    return player_mission.ak_total >= 15


# 15 air kills in one virtual life
def vlife_hero(vlife):
    return vlife.ak_total >= 25


"""
#           Награды Советского Союза
"""


# Знак "Гвардия":
# - лучший сквад тура
def guards(player):
    if player.coal_pref == Coalition.Allies and player.squad:
        if (player.squad.get_position_by_field() == 1
                and (player.get_rating_reward_count('guards') != player.squad.num_members
                     or not player.is_rewarded('guards'))):
            player.delete_rating_reward('guards')
            player.delete_rating_reward('luftwaffe_badge')
            player.squad.reward_squad('guards')


#
#           Высшее отличие
#
# Трижды Герой Советского Союза:
# - лучший стрик сбитых
def gold_star_3rd(player):
    if player.coal_pref == Coalition.Allies and player.is_top_streak() and not player.is_rewarded('gold_star_3rd'):
        player.delete_rating_reward('gold_star_3rd')
        if player.is_rewarded('gold_star_2nd') and not player.is_rewarded('gold_star_3rd_ground'):
            return True
    elif not player.is_top_streak() and player.is_rewarded('gold_star_3rd'):
        player.delete_rating_reward('gold_star_3rd')


# Трижды Герой Советского Союза:
# - лучший стрик по нц
def gold_star_3rd_ground(player):
    if (player.coal_pref == Coalition.Allies and player.is_top_ground_streak()
            and not player.is_rewarded('gold_star_3rd_ground')):
        player.delete_rating_reward('gold_star_3rd_ground')
        if player.is_rewarded('gold_star_2nd') and not player.is_rewarded('gold_star_3rd'):
            return True
    elif not player.is_top_ground_streak() and player.is_rewarded('gold_star_3rd_ground'):
        player.delete_rating_reward('gold_star_3rd_ground')


# Дважды Герой Советского Союза:
# - сбить 7 самолетов противника за вылет
#    или
# - уничтожить 3 самолета и 10 единиц наземки за вылет
#
# - стрик 50 сбитых самолетов и стрик из 30 боевых вылетов
#    или
# - стрик 450 уничтоженных нц для бобра и стрик из 20 боевых вылетов
#    или
# - 100 уничтоженных нц для штурма и стрик из 10 боевых вылетов
def gold_star_2nd(sortie):
    if sortie.player.coal_pref == Coalition.Allies and sortie.player.is_rewarded('gold_star'):
        if sortie.score > 0 and (sortie.ak_total >= 7 or (sortie.ak_total >= 3 and sortie.gk_total >= 10)):
            return True
        elif (sortie.score > 0
              and (sortie.player.streak_current >= 50 and sortie.player.sorties_streak_current >= 30)):
            return True
        elif (sortie.player.get_fav_aircraft_type() == 'aircraft_heavy'
              and sortie.player.streak_ground_current >= 450
              and sortie.player.sorties_streak_current >= 20):
            return True
        elif (sortie.player.get_fav_aircraft_type() == 'aircraft_medium'
              and sortie.player.streak_ground_current >= 100
              and sortie.player.sorties_streak_current >= 10):
            return True


# Герой Советского Союза:
# - сбить 5 самолетов противника за вылет
#    или
# - уничтожить 2 самолета и 10 единиц наземки за вылет
#
# - стрик 15 сбитых самолетов и стрик из 15 боевых вылетов
#    или
# - стрик 250 уничтоженных нц для бобра и стрик из 10 боевых вылетов
#    или
# - 50 уничтоженных нц для штурма и стрик из 5 боевых вылетов
def gold_star(sortie):
    if sortie.player.coal_pref == Coalition.Allies:
        if sortie.score > 0 and (sortie.ak_total >= 5 or (sortie.ak_total >= 2 and sortie.gk_total >= 10)):
            return True
        elif sortie.player.streak_current >= 15 and sortie.player.sorties_streak_current >= 15:
            return True
        elif sortie.player.get_fav_aircraft_type() == 'aircraft_heavy' and sortie.player.streak_ground_current >= 250 and sortie.player.sorties_streak_current >= 10:
            return True
        elif sortie.player.get_fav_aircraft_type() == 'aircraft_medium' and sortie.player.streak_ground_current >= 50 and sortie.player.sorties_streak_current >= 5:
            return True


"""
# Ордена СССР
"""


# Орден Ленина - 2-й:
# - сбить 6 самолета противника за вылет
#    или
# - уничтожить 8 танков за вылет
#    или
# - сбить 3 самолета и 5 единиц наземки за вылет
#
# - стрик 20 сбитых самолетов
#    или
# - стрик 350 уничтоженных нц для бобра
#    или
# - 75 уничтоженных нц для штурма
def order_of_lenin_2nd(sortie):
    if sortie.player.coal_pref == Coalition.Allies and sortie.player.is_rewarded('order_of_lenin'):
        if sortie.ak_total >= 6 or sortie.tanks_total >= 8:
            return True
        elif sortie.ak_total >= 3 and sortie.gk_total >= 5:
            return True
        elif sortie.player.streak_current >= 20:
            return True
        elif sortie.player.get_fav_aircraft_type() == 'aircraft_heavy' and sortie.player.streak_ground_current >= 350:
            return True
        elif sortie.player.get_fav_aircraft_type() == 'aircraft_medium' and sortie.player.streak_ground_current >= 75:
            return True


# Орден Ленина:
# - сбить 4 самолета противника за вылет
#    или
# - уничтожить 6 танков за вылет
#    или
# - сбить 1 самолет и уничтожить не менее 5 нц набрав не менее 600 очков (для боброштурмов)
# - или
# - стрик 10 сбитых самолетов
#    или
# - стрик 150 уничтоженных нц для бобра
#    или
# - 40 уничтоженных нц для штурма
def order_of_lenin(sortie):
    if sortie.player.coal_pref == Coalition.Allies and sortie.player.is_officer():
        if sortie.ak_total >= 4 or sortie.tanks_total >= 6:
            return True
        elif (sortie.score >= 600 and (sortie.ak_total >= 1 and sortie.gk_total >= 5)
              and (sortie.aircraft.cls == 'aircraft_heavy' or sortie.aircraft.cls == 'aircraft_medium')):
            return True
        elif sortie.player.streak_current >= 10:
            return True
        elif sortie.player.get_fav_aircraft_type() == 'aircraft_heavy' and sortie.player.streak_ground_current >= 150:
            return True
        elif sortie.player.get_fav_aircraft_type() == 'aircraft_medium' and sortie.player.streak_ground_current >= 40:
            return True


# Орден Красного Знамени 5й:
# - 250 боевых вылетов
def red_banner_5th(player):
    if player.coal_pref == Coalition.Allies and player.is_rewarded('red_banner_4th'):
        if player.get_combat_sorties() >= 250:
            return True


# Орден Красного Знамени 4й:
# - 200 боевых вылетов
def red_banner_4th(player):
    if player.coal_pref == Coalition.Allies and player.is_rewarded('red_banner_3rd'):
        if player.get_combat_sorties() >= 200:
            return True


# Орден Красного Знамени 3й:
# - 150 боевых вылетов
def red_banner_3rd(player):
    if player.coal_pref == Coalition.Allies and player.is_rewarded('red_banner_2nd'):
        if player.get_combat_sorties() >= 150:
            return True


# Орден Красного Знамени 2й:
# - 100 боевых вылетов
def red_banner_2nd(player):
    if player.coal_pref == Coalition.Allies and player.is_rewarded('red_banner'):
        if player.get_combat_sorties() >= 100:
            return True


# Орден Красного Знамени 1й:
# - 50 боевых вылетов
def red_banner(player):
    if player.coal_pref == Coalition.Allies:
        if player.get_combat_sorties() >= 50:
            return True


# Орден Красной Звезды:
# - на закрытой карте набрать не менее 1000 очков
# - совершить не менее 3-х боевых вылетов
def red_star(player_mission):
    if (player_mission.player.coal_pref == Coalition.Allies
            and player_mission.mission.winning_coalition == Coalition.Allies):
        return player_mission.get_mission_combat_sorties() >= 3 and player_mission.score >= 1000


# Орден Отечественной войны 1-й степени:
# - участие в закрытии 50 карт
def order_of_patriotic_war_1st_class(player):
    if player.coal_pref == Coalition.Allies and player.is_rewarded('order_of_patriotic_war_2nd_class'):
        return player.get_successful_missions() >= 50


# Орден Отечественной войны 2-й степени:
# - участие в закрытии 25 карт
def order_of_patriotic_war_2nd_class(player):
    if player.coal_pref == Coalition.Allies:
        return player.get_successful_missions() >= 25


# Орден Славы I степени:
# - уничтожить не менее 3-х тяжелых танков или 6 средних или 8 танков за боевой вылет
# - уничтожить не мене 5 самолетов или 3 ударных за вылет
# - уничтожить не менее 3-х кораблей
def order_of_glory_1st_class(sortie):
    if sortie.player.coal_pref == Coalition.Allies and sortie.player.is_rewarded('order_of_glory_2rd_class'):
        if sortie.score > 0:
            if (sortie.killboard_pve.get('tank_heavy', 0) >= 3
                    or sortie.killboard_pve.get('tank_medium', 0) >= 6
                    or sortie.tanks_total >= 8):
                return True
            elif (sortie.ak_total >= 5 or (
                    (sortie.killboard_pve.get('aircraft_medium', 0) +
                     sortie.killboard_pve.get('aircraft_heavy', 0)) >= 3)):
                return True
            elif sortie.killboard_pve.get('ship', 0) >= 3:
                return True


# Орден Славы II степени:
# - уничтожить не менее 2-х кораблей или 4 танков за боевой вылет
# - или сбить 2 ударника
# - или сбить 3 самолёта, один из них ударный
def order_of_glory_2nd_class(sortie):
    if sortie.player.coal_pref == Coalition.Allies and sortie.player.is_rewarded('order_of_glory_3rd_class'):
        if sortie.score > 0:
            if sortie.killboard_pve.get('ship', 0) >= 2 or sortie.tanks_total >= 4:
                return True
            elif (sortie.killboard_pve.get('aircraft_medium', 0) + sortie.killboard_pve.get('aircraft_heavy', 0)) >= 2:
                return True
            elif (sortie.ak_total >= 3
                  and (sortie.killboard_pve.get('aircraft_medium', 0)
                       + sortie.killboard_pve.get('aircraft_heavy', 0)) >= 1):
                return True


# Орден Славы III степени:
# - сбить 1 самолет или 1 танк за боевой вылет
def order_of_glory_3rd_class(sortie):
    if (sortie.player.coal_pref == Coalition.Allies
            and not sortie.player.is_officer()):
        if sortie.score > 0 and (sortie.ak_total >= 1 or sortie.tanks_total):
            return True


"""        
#       Медали СССР
"""


# Медаль "За отвагу":
# - боевой вылет
# - посадка на аэродроме
# - ранение более 25% или повреждение самолета более 40%
def medal_for_bravery(sortie):
    if sortie.player.coal_pref == Coalition.Allies:
        return (sortie.score > 0 and sortie.status == SortieStatus.landed
                and ((sortie.aircraft_status == LifeStatus.damaged and sortie.damage > 40)
                     or (sortie.bot_status == BotLifeStatus.wounded and sortie.wound > 25)))


# Медаль "За боевые заслуги":
# - стрик не менее 10 боевых вылетов
# - набрать не менее 3000 очков
def medal_for_battle_merit(player):
    if player.coal_pref == Coalition.Allies:
        return player.sorties_streak_current >= 10 and player.score_streak_current >= 3000


# Медаль "За победу над Германией":
# - участник команды, победившей в прошлом туре
# - 100 боевых вылетов в прошлом туре
def medal_for_victory(player):
    if player.coal_pref == Coalition.Allies and not player.is_rewarded('medal_for_victory'):
        prev_player = player.get_prev_player()
        if (prev_player and prev_player.coal_pref == player.coal_pref
                and prev_player.tour.winning_coalition == prev_player.coal_pref):
            return prev_player.get_combat_sorties() >= 50


"""
# Награды Фашисткой Германии
"""


# Знак "Пилот Люфтваффе":
# - лучший сквад тура
def luftwaffe_badge(player):
    if player.coal_pref == Coalition.Axis and player.squad:
        if (player.squad.get_position_by_field() == 1
                and (player.get_rating_reward_count('luftwaffe_badge') != player.squad.num_members
                     or not player.is_rewarded('luftwaffe_badge'))):
            player.delete_rating_reward('guards')
            player.delete_rating_reward('luftwaffe_badge')
            player.squad.reward_squad('luftwaffe_badge')


# Рыцарский крест с мечами и дубовыми листьями  - условия как у второго Ордена Ленина
def knights_cross_leaves_swords(sortie):
    result = False
    if sortie.player.is_rewarded('knights_cross_leaves'):
        if sortie.score > 0 and (sortie.ak_total >= 6 or sortie.tanks_total >= 8):
            result = True
        elif sortie.score > 0 and (sortie.ak_total >= 3 and sortie.gk_total >= 5):
            result = True
        elif sortie.player.streak_current >= 20:
            result = True
        elif sortie.player.get_fav_aircraft_type() == 'aircraft_heavy' and sortie.player.streak_ground_current >= 350:
            result = True
        elif sortie.player.get_fav_aircraft_type() == 'aircraft_medium' and sortie.player.streak_ground_current >= 75:
            result = True
    if result:
        sortie.player.delete_reward('knights_cross_leaves')
        return result


# Рыцарский крест с мечами, дубовыми листьями и бриллиантами - условия как у дважды Героя Советского Союза
def knights_cross_leaves_swords_diamonds(sortie):
    result = False
    if (not sortie.player.is_rewarded('knights_cross_leaves_swords_diamonds')
            and sortie.player.is_rewarded('knights_cross_leaves_swords')):
        if sortie.score > 0 and (sortie.ak_total >= 7 or (sortie.ak_total >= 3 and sortie.gk_total >= 10)):
            result = True
        elif sortie.player.streak_current >= 50 and sortie.player.sorties_streak_current >= 30:
            result = True
        elif (sortie.player.get_fav_aircraft_type() == 'aircraft_heavy'
              and sortie.player.streak_ground_current >= 450
              and sortie.player.sorties_streak_current >= 20):
            result = True
        elif (sortie.player.get_fav_aircraft_type() == 'aircraft_medium'
              and sortie.player.streak_ground_current >= 100
              and sortie.player.sorties_streak_current >= 10):
            result = True
    if result:
        sortie.player.delete_reward('knights_cross_leaves_swords')
        return result


# Рыцарский крест с мечами, золотыми дубовыми листьями и бриллиантами - условия как у трижды Героя Советского Союза
def knights_cross_leaves_swords_diamonds_gold(player):
    if player.is_top_streak() and not player.is_rewarded(
            'knights_cross_leaves_swords_diamonds_gold') and player.coal_pref == Coalition.Axis:
        player.update_rating_reward('knights_cross_leaves_swords_diamonds_gold', 'knights_cross_leaves_swords_diamonds')
        if player.is_rewarded('knights_cross_leaves_swords_diamonds') and not player.is_rewarded(
                'knights_cross_leaves_swords_diamonds_gold_ground'):
            player.update_reward('knights_cross_leaves_swords_diamonds', 'knights_cross_leaves_swords_diamonds_gold')
    elif not player.is_top_ground_streak() and player.is_rewarded('knights_cross_leaves_swords_diamonds_gold'):
        if player.is_rewarded('knights_cross_leaves_swords_diamonds'):
            player.delete_reward('knights_cross_leaves_swords_diamonds_gold')
        else:
            player.update_reward('knights_cross_leaves_swords_diamonds_gold', 'knights_cross_leaves_swords_diamonds')


# Рыцарский крест с мечами, золотыми дубовыми листьями и бриллиантами - условия как у трижды Героя Советского Союза
def knights_cross_leaves_swords_diamonds_gold_ground(player):
    if player.is_top_ground_streak() and not player.is_rewarded(
            'knights_cross_leaves_swords_diamonds_gold_ground') and player.coal_pref == Coalition.Axis:
        player.update_rating_reward('knights_cross_leaves_swords_diamonds_gold_ground',
                                    'knights_cross_leaves_swords_diamonds')
        if player.is_rewarded('knights_cross_leaves_swords_diamonds') and not player.is_rewarded(
                'knights_cross_leaves_swords_diamonds_gold'):
            player.update_reward('knights_cross_leaves_swords_diamonds',
                                 'knights_cross_leaves_swords_diamonds_gold_ground')
    elif not player.is_top_ground_streak() and player.is_rewarded('knights_cross_leaves_swords_diamonds_gold_ground'):
        player.update_rating_reward('knights_cross_leaves_swords_diamonds_gold_ground',
                                    'knights_cross_leaves_swords_diamonds')


# Рыцарский крест с дубовыми листьями - условия как у ГСС-1
def knights_cross_leaves(sortie):
    result = False
    if sortie.player.coal_pref == Coalition.Axis and sortie.player.is_rewarded('knights_cross'):
        if sortie.score > 0 and (sortie.ak_total >= 5 or (sortie.ak_total >= 2 and sortie.gk_total >= 10)):
            result = True
        elif sortie.player.streak_current >= 15 and sortie.player.sorties_streak_current >= 15:
            result = True
        elif (sortie.player.get_fav_aircraft_type() == 'aircraft_heavy'
              and sortie.player.streak_ground_current >= 250
              and sortie.player.sorties_streak_current >= 10):
            result = True
        elif (sortie.player.get_fav_aircraft_type() == 'aircraft_medium'
              and sortie.player.streak_ground_current >= 50
              and sortie.player.sorties_streak_current >= 5):
            result = True
    if result:
        sortie.player.delete_reward('knights_cross')
        return result


# Рыцарский крест
def knights_cross(sortie):
    if (sortie.player.coal_pref == Coalition.Axis and (
            sortie.player.is_rewarded('iron_cross_1'))
            or sortie.player.is_rewarded('military_merit_silver')):
        if sortie.score > 0 and (sortie.ak_total >= 5 or (sortie.ak_total >= 2 and sortie.gk_total >= 10)):
            return True
        elif sortie.player.streak_current >= 10 and sortie.player.sorties_streak_current >= 5:
            return True
        elif (sortie.player.get_fav_aircraft_type() == 'aircraft_heavy'
              and sortie.player.streak_ground_current >= 150
              and sortie.player.sorties_streak_current >= 5):
            return True
        elif (sortie.player.get_fav_aircraft_type() == 'aircraft_medium'
              and sortie.player.streak_ground_current >= 30
              and sortie.player.sorties_streak_current >= 5):
            return True


# Германский крест в золоте
def deutsch_cross_gold(player):
    if (player.coal_pref == Coalition.Axis and (player.is_rewarded('iron_cross_1')
                                                or player.is_rewarded('military_merit_silver'))):
        if player.get_combat_sorties() >= 50:
            return True


# Почетный кубок:
# - сбить 4 самолета противника за вылет
#    или
# - уничтожить 6 танков за вылет
#    или
# - сбить 1 самолет и уничтожить не менее 5 нц набрав не менее 600 очков (для боброштурмов)
# - или
# - стрик 10 сбитых самолетов
#    или
# - стрик 150 уничтоженных нц для бобра
#    или
# - 40 уничтоженных нц для штурма
def luftwaffe_cup(sortie):
    if sortie.player.coal_pref == Coalition.Axis and sortie.player.is_officer():
        if sortie.ak_total >= 4 or sortie.tanks_total >= 6:
            return True
        elif (sortie.score >= 600 and (sortie.ak_total >= 1 and sortie.gk_total >= 5)
              and (sortie.aircraft.cls == 'aircraft_heavy' or sortie.aircraft.cls == 'aircraft_medium')):
            return True
        elif sortie.player.streak_current >= 10:
            return True
        elif sortie.player.get_fav_aircraft_type() == 'aircraft_heavy' and sortie.player.streak_ground_current >= 150:
            return True
        elif sortie.player.get_fav_aircraft_type() == 'aircraft_medium' and sortie.player.streak_ground_current >= 40:
            return True


#   Железный крест
# Железный крест 1-го класса
def iron_cross_1(player_mission):
    if (player_mission.player.coal_pref == Coalition.Axis
            and player_mission.mission.winning_coalition == Coalition.Axis
            and player_mission.player.is_rewarded('iron_cross_2')):
        if player_mission.get_mission_combat_sorties() >= 3 and player_mission.score >= 1000:
            if player_mission.player.streak_current >= 10:
                return True
            elif (player_mission.player.get_fav_aircraft_type() == 'aircraft_medium'
                  and player_mission.player.sorties_streak_current >= 20):
                return True
            elif (player_mission.player.get_fav_aircraft_type() == 'aircraft_heavy'
                  and player_mission.player.sorties_streak_current >= 10):
                return True


# Железный крест 2-го класса
def iron_cross_2(player_mission):
    if player_mission.player.coal_pref == Coalition.Axis and player_mission.mission.winning_coalition == Coalition.Axis:
        if (player_mission.killboard_pve.get('ship', 0) >= 2 or
                (player_mission.killboard_pvp.get('tank_light', 0) +
                 player_mission.killboard_pvp.get('tank_medium', 0) +
                 player_mission.killboard_pvp.get('tank_heavy', 0)) >= 4):
            return True
        elif (player_mission.killboard_pvp.get('aircraft_medium', 0) +
              player_mission.killboard_pvp.get('aircraft_heavy', 0)) >= 2:
            return True
        elif ((player_mission.killboard_pvp.get('aircraft_light', 0) +
               player_mission.killboard_pvp.get('aircraft_medium', 0) +
               player_mission.killboard_pvp.get('aircraft_heavy', 0)) >= 3
              and (player_mission.killboard_pvp.get('aircraft_medium', 0)
                   + player_mission.killboard_pvp.get('aircraft_heavy', 0)) >= 1):
            return True


# Рыцарский крест Креста военных заслуг с мечами:
# - уничтожить не менее 3-х тяжелых танков или 6 средних или 8 танков за боевой вылет
# - уничтожить не мене 5 самолетов или 3 ударных за вылет
# - уничтожить не менее 3-х кораблей
def military_merit_knight(sortie):
    if sortie.player.coal_pref == Coalition.Axis and sortie.player.is_rewarded('military_merit_silver'):
        if sortie.score > 0:
            if (sortie.killboard_pve.get('tank_heavy', 0) >= 3
                    or sortie.killboard_pve.get('tank_medium', 0) >= 6
                    or sortie.tanks_total >= 8):
                return True
            elif (sortie.ak_total >= 5 or (
                    (sortie.killboard_pve.get('aircraft_medium', 0) +
                     sortie.killboard_pve.get('aircraft_heavy', 0)) >= 3)):
                return True
            elif sortie.killboard_pve.get('ship', 0) >= 3:
                return True


# Крест военных заслуг с мечами в (посеребренный):
# - быть награжденным Крестом военных заслуг с мечами в бронзе
# - уничтожить:
# 2 корабля
# или 4 танка
# или сбить 3 самолёта
def military_merit_silver(sortie):
    if sortie.player.coal_pref == Coalition.Axis and sortie.player.is_rewarded('military_merit_bronze'):
        if sortie.score > 0:
            if sortie.killboard_pve.get('ship', 0) >= 2 or sortie.tanks_total >= 4:
                return True
            elif sortie.ak_total >= 3:
                return True


#  Крест военных заслуг с мечами в бронзе:
# - стрик не менее 10 боевых вылетов
# - набрать не менее 3000 очков
def military_merit_bronze(sortie):
    if sortie.player.coal_pref == Coalition.Axis:
        return sortie.player.sorties_streak_current >= 10 and sortie.player.score_streak_current >= 3000


# Знак пилота
# набрано более 200 очков
# и стрик не менее 2 боевых вылетов
def pilot_badge(player_mission):
    if player_mission.player.coal_pref == Coalition.Axis:
        if player_mission.player.score_streak_current >= 200 and player_mission.player.sorties_streak_current >= 2:
            return True


# Медаль «За зимнюю кампанию на Востоке 1941/42»
def medal_previous_tour(player):
    if player.coal_pref == Coalition.Axis and not player.is_rewarded('medal_previous_tour'):
        prev_player = player.get_prev_player()
        if (prev_player and prev_player.coal_pref == player.coal_pref
                and prev_player.tour.winning_coalition == prev_player.coal_pref):
            return prev_player.get_combat_sorties() >= 50


# Старые награды
#   Железный крест
# Железный крест 1-го класса
def iron_cross_1st_class(player_mission):
    return False


# Железный крест 2-го класса - условия как у Красной Звезды
def iron_cross_2nd_class(player_mission):
    return False


# Знак пилота
def aeronautical_medal(player):
    return False


# Медаль "За зимнюю кампанию на Востоке 1941/42" - условия как у медали "За победу над Германией"
def medal_eastern_front(player):
    return False


# Крест "За верную службу в вермахте" в серебре - условия как у Отечественной войны 2-й степени
def wehrmacht_long_service_silver(player):
    return False


# Крест "За верную службу в вермахте" в золоте - условия как у Отечественной войны 1-й степени
def wehrmacht_long_service_gold(player):
    return False


# Крест «За военные заслуги» 2-й степени:
# - уничтожить 20 единиц любой наземки за вылет
def war_merit_cross_2nd_class(sortie):
    return False


# Крест «За военные заслуги» 1-й степени:
# - уничтожить 4 танков за вылет
def war_merit_cross_1st_class(sortie):
    return False


# Рыцарский крест «За военные заслуги»:
# - уничтожить 50 единиц любой наземки за вылет
def knights_war_merit_cross(sortie):
    return False


# Рыцарский крест «За военные заслуги» с мечами:
# - уничтожить 6 танков за вылет
def knights_war_merit_cross_swords(sortie):
    return False


# Германский крест в серебре тканевый - условия как у Ордена Красного Знамени 1го
def german_cross_silver_cloth(player):
    return False


# Германский крест в золоте тканевый - условия как у Ордена Красного Знамени 2го
def german_cross_gold_cloth(player):
    return False


# Германский крест в серебре - условия как у Ордена Красного Знамени 3го
def german_cross_silver(player):
    return False


# Германский крест в золоте - условия как у Ордена Красного Знамени 4го
def german_cross_gold(player):
    return False


# Германский крест в золоте с бриллиантами - условия как у Ордена Красного Знамени 5го
def german_cross_diamonds(player):
    return False
