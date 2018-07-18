-- Table: ranks

-- DROP TABLE ranks;

CREATE TABLE ranks
(
  id integer NOT NULL,
  allied_rank character varying(20) NOT NULL,
  axis_rank character varying(20) NOT NULL,
  min_flight_hours integer NOT NULL,
  min_rating bigint NOT NULL,
  min_rating_position integer,
  
  CONSTRAINT ranks_pkey PRIMARY KEY (id),
  CONSTRAINT ranks_allied_rank UNIQUE (allied_rank),
  CONSTRAINT ranks_axis_rank UNIQUE (allied_rank)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE ranks
  OWNER TO il2_stats;

INSERT INTO ranks(id, allied_rank, axis_rank, min_rating, min_flight_hours, min_rating_position)
VALUES(0, '', '', -1, -1, 9999);
INSERT INTO ranks(id, allied_rank, axis_rank, min_rating, min_flight_hours, min_rating_position)
VALUES(1, 'Sergeant', 'Unteroffizier', 0, 0, 9999);
INSERT INTO ranks(id, allied_rank, axis_rank, min_rating, min_flight_hours, min_rating_position)
VALUES(2, 'Snr. Sergeant', 'Unterfeldwebel', 50000, 2, 9999);
INSERT INTO ranks(id, allied_rank, axis_rank, min_rating, min_flight_hours, min_rating_position)
VALUES(3, 'Sergeant Maj.', 'Feldwebel', 100000, 4, 9999);
INSERT INTO ranks(id, allied_rank, axis_rank, min_rating, min_flight_hours, min_rating_position)
VALUES(4, 'Jnr. Lieutenant', 'Oberfeldwebel', 500000, 8, 9999);
INSERT INTO ranks(id, allied_rank, axis_rank, min_rating, min_flight_hours, min_rating_position)
VALUES(5, 'Lieutenant', 'Leutnant', 1000000, 10, 9999);
INSERT INTO ranks(id, allied_rank, axis_rank, min_rating, min_flight_hours, min_rating_position)
VALUES(6, 'Snr. Lieutenant', 'Oberleutnant', 2000000, 12, 9999);
INSERT INTO ranks(id, allied_rank, axis_rank, min_rating, min_flight_hours, min_rating_position)
VALUES(7, 'Captain', 'Hauptmann', 5000000, 16, 9999);
INSERT INTO ranks(id, allied_rank, axis_rank, min_rating, min_flight_hours, min_rating_position)
VALUES(8, 'Major', 'Major', 10000000, 24, 100);
INSERT INTO ranks(id, allied_rank, axis_rank, min_rating, min_flight_hours, min_rating_position)
VALUES(9, 'Lt. Colonel', 'Oberstleutnant', 10000000, 32, 50);
INSERT INTO ranks(id, allied_rank, axis_rank, min_rating, min_flight_hours, min_rating_position)
VALUES(10, 'Colonel', 'Oberst', 10000000, 40, 20);
INSERT INTO ranks(id, allied_rank, axis_rank, min_rating, min_flight_hours, min_rating_position)
VALUES(11, 'Maj. General', 'Generalmajor', 10000000, 48, 20);

ALTER TABLE players ADD COLUMN rank_id integer;
UPDATE players SET rank_id = 0;
ALTER TABLE players ALTER COLUMN rank_id SET NOT NULL;
ALTER TABLE players ADD CONSTRAINT players_fk_rank_id FOREIGN KEY (rank_id)
      REFERENCES ranks (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

