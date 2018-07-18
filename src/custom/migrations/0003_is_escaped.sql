ALTER TABLE sorties ADD COLUMN is_escaped boolean;
UPDATE sorties SET is_escaped = false;
ALTER TABLE sorties ALTER COLUMN is_escaped SET NOT NULL;