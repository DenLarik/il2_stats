DELETE FROM rewards WHERE date >'2018-11-01';
INSERT INTO public.awards(
	id, func, type, img, title_en, title_ru, title_de, "desc", desc_ru)
	VALUES (1500, 'medal_previous_tour', 'tour', 'awards/axis/1500.png', 'Medal "For the winter campaign of 1941-42 in the East"','Медаль «За зимнюю кампанию на Востоке 1941/42»', 'Medaille "Winterschlacht im Osten 1941/42" ', 'Win previous tour with at least 50 combat sorties', 'Отображается у участника команды победителя прошлого тура при наличии в прошлом туре 50 боевых вылетов'),
	(1490,'pilot_badge','mission','awards/axis/1490.png','Pilot''s Luftwaffe qualification badge','Квалификационный нагрудный знак люфтваффе «Пилот»','Flugzeugführerabzeichen','Scored over 200 points
and streak at least 2 sorties','Набрано более 200 очков
и стрик не менее 2 боевых вылетов'),
(1480,'military_merit_bronze','sortie','awards/axis/1480.png','Kriegsverdienstkreuz','Крест за военные заслуги 2 степени с мечами','Kriegsverdienstkreuz','streak at least 10 sorties
score at least 3000 points','стрик не менее 10 боевых вылетов
набрать не менее 3000 очков'),
(1470,'military_merit_silver','sortie','awards/axis/1470.png','Kriegsverdienstkreuz','Крест за военные заслуги 1 степени с мечами','Kriegsverdienstkreuz','return from combat sortie
more than 25% injured or more than 40% damage to aircraft','вернуться с боевого вылета с
ранением более 25% или повреждением самолета более 40%'),
(1460,'military_merit_knight','sortie','awards/axis/1460.png','Kriegsverdienstkreuz','Рыцарский крест Креста военных заслуг с мечами','Kriegsverdienstkreuz','destroy at least 3 heavy tanks or 6 medium or 8 tanks for a combat mission
destroy at least 5 aircraft or 3 strike aircraft for departure
destroy at least 3 ships','уничтожить не менее 3-х тяжелых танков или 6 средних или 8 танков за боевой вылет
уничтожить не мене 5 самолетов или 3 ударных за вылет
уничтожить не менее 3-х кораблей'),
(1450,'iron_cross_2','mission','awards/axis/1450.png','Eisernes Kreuz','Железный крест 2-го класса','Eisernes Kreuz','destroy at least 2 ships or 4 tanks for a combat mission
or shoot down 2 shock planes
or shoot down 3 aircraft, one of them is a strike aircraft','уничтожить не менее 2-х кораблей или 4 танков за боевой вылет
или сбить 2 ударных самолета
или сбить 3 самолёта, один из них ударный самолет'),
(1440,'iron_cross_1','mission','awards/axis/1440.png','Eisernes Kreuz','Железный крест 1-го класса','Eisernes Kreuz','destroy at least 3 heavy tanks or 6 medium or 8 tanks for a combat mission
destroy at least 5 aircraft or 3 strike aircraft for departure
destroy at least 3 ships','уничтожить не менее 3-х тяжелых танков или 6 средних или 8 танков за боевой вылет
уничтожить не мене 5 самолетов или 3 ударных за вылет
уничтожить не менее 3-х кораблей'),
(1430,'luftwaffe_cup','sortie','awards/axis/1430.png','Ehrenpokal für besondere Leistung im Luftkrieg','Почëтный Кубок Люфтваффе','Ehrenpokal für besondere Leistung im Luftkrieg','shoot down 4 enemy aircraft for departure
or destroy 6 tanks for departure
or shoot down 1 plane and destroy at least 5 ground targets by typing at least 600 points
or streak 10 downed aircraft
or streak 150 destroyed targets for a bomber
or 40 destroyed targets for attack aircraft','сбить 4 самолета противника за вылет
или уничтожить 6 танков за вылет
или сбить 1 самолет и уничтожить не менее 5 наземных целей набрав не менее 600 очков
или стрик 10 сбитых самолетов
или стрик 150 уничтоженных целей для бомбардировщика
или 40 уничтоженных целей для штурмовика'),
(1420,'deutsch_cross_gold','tour','awards/axis/1420.png','Der Kriegsorden des Deutschen Kreuzesg','Германский крест в золоте','Der Kriegsorden des Deutschen Kreuzes','make at least 100 sorties','соверишить не менее 100 боевых вылетов');