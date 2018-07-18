-- Table: profiles_stats

-- DROP TABLE profiles_stats;

CREATE TABLE profiles_stats
(
  profile_id integer NOT NULL,
  ip character varying(15) NOT NULL,
  connection_date timestamp with time zone NOT NULL,
  type integer NOT NULL,
  CONSTRAINT profiles_stats_pkey PRIMARY KEY (profile_id, ip, type, connection_date)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE profiles_stats
  OWNER TO il2_stats;

-- Index: profiles_stats_profile_id_a5fc26ed_like

--DROP INDEX profiles_stats_profile_id_a5fc26ed_like;

CREATE INDEX profiles_stats_profile_id_a5fc26ed_like
  ON profiles_stats
  USING btree
  (profile_id);

