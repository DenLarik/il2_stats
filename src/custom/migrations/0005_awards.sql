UPDATE awards
SET img = 'awards/allies/guard.png'
WHERE id = 50;
UPDATE awards
SET img = 'awards/allies/hero_of_su.png'
WHERE func LIKE 'gold_star%';
UPDATE awards
SET img = 'awards/allies/hero_of_su.png'
WHERE func LIKE 'gold_star%';
UPDATE awards
SET img = 'awards/allies/order_lenina.png'
WHERE func LIKE 'order_of_lenin%';
UPDATE awards
SET img = 'awards/allies/order_red_banner.png'
WHERE func LIKE 'red_banner%';
UPDATE awards
SET img = 'awards/allies/order_red_banner.png'
WHERE func LIKE 'red_banner%';
UPDATE awards
SET img = 'awards/allies/order_war1.png'
WHERE func LIKE 'order_of_patriotic_war_1st_class';
UPDATE awards
SET img = 'awards/allies/order_war2.png'
WHERE func LIKE 'order_of_patriotic_war_2nd_class';
UPDATE awards
SET img = 'awards/allies/order_red_star.png'
WHERE func LIKE 'red_star';
UPDATE awards
SET img = 'awards/allies/order_glory1.png'
WHERE func LIKE 'order_of_glory_1st_class';
UPDATE awards
SET img = 'awards/allies/order_glory1.png'
WHERE func LIKE 'order_of_glory_2nd_class';
UPDATE awards
SET img = 'awards/allies/order_glory1.png'
WHERE func LIKE 'order_of_glory_3rd_class';
UPDATE awards
SET img = 'awards/allies/medal_bravery.png'
WHERE func LIKE 'medal_for_bravery';
UPDATE awards
SET img = 'awards/allies/medal_zbz.png'
WHERE func LIKE 'medal_for_battle_merit';
UPDATE awards
SET img = 'awards/allies/medal_victory.png'
WHERE func LIKE 'medal_for_victory';
--
UPDATE awards
SET img      = 'awards/axis/guard.png',
    title    = 'Почётный лётный знак',
    title_de = 'Flieger-Erinnerungsabzeichen',
    title_en = 'Flieger-Erinnerungsabzeichen',
    title_fr = 'Flieger-Erinnerungsabzeichen',
    "desc"     = 'Почётный лётный знак (нем. Flieger-Erinnerungsabzeichen) — немецкая награда в виде нагрудного знака, которой награждались отставные и продолжающие службу летчики, участники Первой мировой войны или прослужившие в Люфтваффе не менее 15 лет или получившие ранение в ходе боевых действий.\nЛучший скавд',
    desc_de  = 'Das Flieger-Erinnerungsabzeichen (auch: Preußisches Fliegerdienst-Erinnerungsabzeichen) wurde am 27. Januar 1914 durch Kaiser und König Wilhelm II. gestiftet. Ausgezeichnet werden sollten Offiziere, Unteroffiziere und Mannschaften, die im Falle einer Mobilmachung nicht mehr berücksichtigt und nicht mehr für den Einsatz vorgesehen waren. Nach dem Krieg erhielten ehemalige Flugzeugführer das Erinnerungsabzeichen.\nTop squad',
    desc_en  = 'Das Flieger-Erinnerungsabzeichen (auch: Preußisches Fliegerdienst-Erinnerungsabzeichen) wurde am 27. Januar 1914 durch Kaiser und König Wilhelm II. gestiftet. Ausgezeichnet werden sollten Offiziere, Unteroffiziere und Mannschaften, die im Falle einer Mobilmachung nicht mehr berücksichtigt und nicht mehr für den Einsatz vorgesehen waren. Nach dem Krieg erhielten ehemalige Flugzeugführer das Erinnerungsabzeichen.\nTop squad',
    desc_fr  = 'Das Flieger-Erinnerungsabzeichen (auch: Preußisches Fliegerdienst-Erinnerungsabzeichen) wurde am 27. Januar 1914 durch Kaiser und König Wilhelm II. gestiftet. Ausgezeichnet werden sollten Offiziere, Unteroffiziere und Mannschaften, die im Falle einer Mobilmachung nicht mehr berücksichtigt und nicht mehr für den Einsatz vorgesehen waren. Nach dem Krieg erhielten ehemalige Flugzeugführer das Erinnerungsabzeichen.\nTop squad'
WHERE func LIKE 'luftwaffe_badge';
UPDATE awards
SET img = 'awards/axis/401.png'
WHERE id = 401;
UPDATE awards
SET img = 'awards/axis/402.png'
WHERE id = 402;
UPDATE awards
SET img = 'awards/axis/403.png'
WHERE id = 403;
UPDATE awards
SET img = 'awards/axis/404.png'
WHERE id = 404;
UPDATE awards
SET img = 'awards/axis/405.png'
WHERE id = 405;
UPDATE awards
SET img = 'awards/axis/406.png'
WHERE id = 406;
UPDATE awards
SET img  = 'awards/axis/411.png',
    type = 'mission'
WHERE id = 411;
UPDATE awards
SET img = 'awards/axis/412.png'
WHERE id = 412;
UPDATE awards
SET img = 'awards/axis/421.png'
WHERE id = 421;
UPDATE awards
SET img = 'awards/axis/422.png'
WHERE id = 422;
UPDATE awards
SET img = 'awards/axis/423.png'
WHERE id = 423;
UPDATE awards
SET img = 'awards/axis/424.png'
WHERE id = 424;
UPDATE awards
SET img = 'awards/axis/425.png'
WHERE id = 425;
UPDATE awards
SET img = 'awards/axis/491.png'
WHERE id = 491;
UPDATE awards
SET img = 'awards/axis/492.png'
WHERE id = 492;
UPDATE awards
SET img = 'awards/axis/493.png'
WHERE id = 493;
UPDATE awards
SET img = 'awards/axis/494.png'
WHERE id = 494;
UPDATE awards
SET img = 'awards/axis/501.png'
WHERE id = 501;
UPDATE awards
SET img = 'awards/axis/502.png'
WHERE id = 502;
UPDATE awards
SET img      = 'awards/axis/503.png',
    title    = 'Flugzeugführerabzeichen',
    title_en = 'Flugzeugführerabzeichen',
    title_de = 'Flugzeugführerabzeichen',
    title_fr = 'Flugzeugführerabzeichen',
    title_ru = 'Квалификационный нагрудный знак люфтваффе «Пилот»',
    "desc"   = 'Flugzeugführerabzeichen bezeichnet die Ehren- oder Tätigkeitsabzeichen der Luftstreitkräfte, die einen Flugzeugführer (ggf. ehrenhalber) auszeichnet.',
    desc_en  = 'Flugzeugführerabzeichen bezeichnet die Ehren- oder Tätigkeitsabzeichen der Luftstreitkräfte, die einen Flugzeugführer (ggf. ehrenhalber) auszeichnet.',
    desc_de  = 'Flugzeugführerabzeichen bezeichnet die Ehren- oder Tätigkeitsabzeichen der Luftstreitkräfte, die einen Flugzeugführer (ggf. ehrenhalber) auszeichnet.',
    desc_fr  = 'Flugzeugführerabzeichen bezeichnet die Ehren- oder Tätigkeitsabzeichen der Luftstreitkräfte, die einen Flugzeugführer (ggf. ehrenhalber) auszeichnet.',
    desc_ru  = 'Награждались летчики (пилоты) авиационных школ успешно окончившие курсы по обучению (около 100—140 часов налёта за 6-9 месяцев обучения)\nСтрик больше или равен 2, набрать не менее 200 очков'
WHERE id = 503;
UPDATE awards
SET img = 'awards/axis/531.png'
WHERE id = 531;