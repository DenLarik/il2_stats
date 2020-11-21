-- Table: current_mission

-- DROP TABLE current_mission;

CREATE TABLE current_mission
(
  name character varying(128) NOT NULL,
  duration integer NOT NULL,
  CONSTRAINT current_mission_pkey PRIMARY KEY (name)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE current_mission
  OWNER TO il2_stats;

-- Index: current_mission_name_a5fc26ed_like

-- DROP INDEX current_mission_name_a5fc26ed_like;

CREATE INDEX current_mission_name_a5fc26ed_like
  ON current_mission
  USING btree
  (name COLLATE pg_catalog."default" varchar_pattern_ops);

