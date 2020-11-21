-- Guards & Luftwaffe Badge
update rewards set award_id = 50 where award_id = (select id from awards where func = 'guards');
update awards set id = 50 where func = 'guards';
update rewards set award_id = 350 where award_id = (select id from awards where func = 'luftwaffe_badge');
update awards set id = 350 where func = 'luftwaffe_badge';

------------------------
---- Soviet
------------------------

-- Gold Star
update rewards set award_id = 101 where award_id = (select id from awards where func = 'gold_star');
update awards set id = 101 where func = 'gold_star';
update rewards set award_id = 103 where award_id = (select id from awards where func = 'gold_star_2nd');
update awards set id = 103 where func = 'gold_star_2nd';
update rewards set award_id = 105 where award_id = (select id from awards where func = 'gold_star_3rd');
update awards set id = 105 where func = 'gold_star_3rd';
update rewards set award_id = 107 where award_id = (select id from awards where func = 'gold_star_3rd_ground');
update awards set id = 107 where func = 'gold_star_3rd_ground';

-- Lenin
update rewards set award_id = 111 where award_id = (select id from awards where func = 'order_of_lenin');
update awards set id = 111 where func = 'order_of_lenin';
update rewards set award_id = 113 where award_id = (select id from awards where func = 'order_of_lenin_2nd');
update awards set id = 113 where func = 'order_of_lenin_2nd';

-- Red Banner
update rewards set award_id = 121  where award_id = (select id from awards where func = 'red_banner');
update awards set id = 121 where func = 'red_banner';
update rewards set award_id = 123 where award_id = (select id from awards where func = 'red_banner_2nd');
update awards set id = 123 where func = 'red_banner_2nd';
update rewards set award_id = 125 where award_id = (select id from awards where func = 'red_banner_3rd');
update awards set id = 125 where func = 'red_banner_3rd';
update rewards set award_id = 127 where award_id = (select id from awards where func = 'red_banner_4th');
update awards set id = 127 where func = 'red_banner_4th';
update rewards set award_id = 129 where award_id = (select id from awards where func = 'red_banner_5th');
update awards set id = 129 where func = 'red_banner_5th';

-- Patriotic War
update rewards set award_id = 172 where award_id = (select id from awards where func = 'order_of_patriotic_war_1st_class');
update awards set id = 172 where func = 'order_of_patriotic_war_1st_class';
update rewards set award_id = 174 where award_id = (select id from awards where func = 'order_of_patriotic_war_2nd_class');
update awards set id = 174 where func = 'order_of_patriotic_war_2nd_class';

-- Red Star
update rewards set award_id = 182 where award_id = (select id from awards where func = 'red_star');
update awards set id = 182 where func = 'red_star';

-- Glory
update rewards set award_id = 191 where award_id = (select id from awards where func = 'order_of_glory_1st_class');
update awards set id = 191 where func = 'order_of_glory_1st_class';
update rewards set award_id = 193 where award_id = (select id from awards where func = 'order_of_glory_2nd_class');
update awards set id = 193 where func = 'order_of_glory_2nd_class';
update rewards set award_id = 195 where award_id = (select id from awards where func = 'order_of_glory_3rd_class');
update awards set id = 195 where func = 'order_of_glory_3rd_class';

-- Medals
update rewards set award_id = 201 where award_id = (select id from awards where func = 'medal_for_bravery');
update awards set id = 201 where func = 'medal_for_bravery';
update rewards set award_id = 203 where award_id = (select id from awards where func = 'medal_for_battle_merit');
update awards set id = 203 where func = 'medal_for_battle_merit';
update rewards set award_id = 231 where award_id = (select id from awards where func = 'medal_for_victory');
update awards set id = 231 where func = 'medal_for_victory';

------------------------
---- German
------------------------

-- Knight's Cross
update rewards set award_id = 1112 where award_id = (select id from awards where func = 'knights_cross_leaves_swords_diamonds');
update awards set id=1112 where func = 'knights_cross_leaves_swords_diamonds';
update rewards set award_id = 1113  where award_id = (select id from awards where func = 'knights_cross_leaves_swords');
update awards set id=1113 where func = 'knights_cross_leaves_swords';
update rewards set award_id = 1114  where award_id = (select id from awards where func = 'knights_cross_leaves');
update awards set id=1114 where func = 'knights_cross_leaves';
update rewards set award_id = 1115  where award_id = (select id from awards where func = 'knights_cross');
update awards set id=1115 where func = 'knights_cross';
update rewards set award_id = 401 where award_id = (select id from awards where func = 'knights_cross_leaves_swords_diamonds_gold');
update awards set id=401 where func = 'knights_cross_leaves_swords_diamonds_gold';
update rewards set award_id = 402 where award_id = (select id from awards where func = 'knights_cross_leaves_swords_diamonds_gold_ground');
update awards set id=402 where func = 'knights_cross_leaves_swords_diamonds_gold_ground';
update rewards set award_id = 403 where award_id = (select id from awards where func = 'knights_cross_leaves_swords_diamonds');
update awards set id=403 where func = 'knights_cross_leaves_swords_diamonds';
update rewards set award_id = 404  where award_id = (select id from awards where func = 'knights_cross_leaves_swords');
update awards set id=404 where func = 'knights_cross_leaves_swords';
update rewards set award_id = 405  where award_id = (select id from awards where func = 'knights_cross_leaves');
update awards set id=405 where func = 'knights_cross_leaves';
update rewards set award_id = 406  where award_id = (select id from awards where func = 'knights_cross');
update awards set id=406 where func = 'knights_cross';

-- Iron Cross
update rewards set award_id = 411 where award_id = (select id from awards where func = 'iron_cross_1st_class');
update awards set id = 411 where func = 'iron_cross_1st_class';
update rewards set award_id = 412 where award_id = (select id from awards where func = 'iron_cross_2nd_class');
update awards set id = 412 where func = 'iron_cross_2nd_class';

-- German Cross
update rewards set award_id = 1111  where award_id = (select id from awards where func = 'knights_cross_fabric_silver');
update awards set id=1111, func = 'german_cross_silver_cloth' where func = 'knights_cross_fabric_silver';
update rewards set award_id = 1112  where award_id = (select id from awards where func = 'knights_cross_fabric_gold');
update awards set id=1112, func = 'german_cross_gold_cloth' where func = 'knights_cross_fabric_gold';
update rewards set award_id = 1113  where award_id = (select id from awards where func = 'knights_cross_silver');
update awards set id=1113, func = 'german_cross_silver' where func = 'knights_cross_silver';
update rewards set award_id = 1114  where award_id = (select id from awards where func = 'knights_cross_gold');
update awards set id=1114, func = 'german_cross_gold' where func = 'knights_cross_gold';
update rewards set award_id = 1115  where award_id = (select id from awards where func = 'knights_cross_diamonds');
update awards set id=1115, func = 'german_cross_diamonds' where func = 'knights_cross_diamonds';
update rewards set award_id = 421 where award_id = (select id from awards where func = 'german_cross_diamonds');
update awards set id = 421 where func = 'german_cross_diamonds';
update rewards set award_id = 422 where award_id = (select id from awards where func = 'german_cross_gold');
update awards set id = 422 where func = 'german_cross_gold';
update rewards set award_id = 423 where award_id = (select id from awards where func = 'german_cross_silver');
update awards set id = 423 where func = 'german_cross_silver';
update rewards set award_id = 424 where award_id = (select id from awards where func = 'german_cross_gold_cloth');
update awards set id = 424 where func = 'german_cross_gold_cloth';
update rewards set award_id = 425 where award_id = (select id from awards where func = 'german_cross_silver_cloth');
update awards set id = 425 where func = 'german_cross_silver_cloth';

-- War Merit Cross
update rewards set award_id = 491 where award_id = (select id from awards where func = 'knights_war_merit_cross_swords');
update awards set id = 491 where func = 'knights_war_merit_cross_swords';
update rewards set award_id = 492 where award_id = (select id from awards where func = 'knights_war_merit_cross');
update awards set id = 492 where func = 'knights_war_merit_cross';
update rewards set award_id = 493 where award_id = (select id from awards where func = 'war_merit_cross_1st_class');
update awards set id = 493 where func = 'war_merit_cross_1st_class';
update rewards set award_id = 494 where award_id = (select id from awards where func = 'war_merit_cross_2nd_class');
update awards set id = 494 where func = 'war_merit_cross_2nd_class';

-- Medals
update rewards set award_id = 501 where award_id = (select id from awards where func = 'wehrmacht_long_service_gold');
update awards set id = 501 where func = 'wehrmacht_long_service_gold';
update rewards set award_id = 502 where award_id = (select id from awards where func = 'wehrmacht_long_service_silver');
update awards set id = 502 where func = 'wehrmacht_long_service_silver';
update rewards set award_id = 503 where award_id = (select id from awards where func = 'aeronautical_medal');
update awards set id = 503 where func = 'aeronautical_medal';
update rewards set award_id = 531 where award_id = (select id from awards where func = 'medal_eastern_front');
update awards set id = 531 where func = 'medal_eastern_front';
