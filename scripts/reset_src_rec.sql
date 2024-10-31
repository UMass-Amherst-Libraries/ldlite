DROP TABLE IF EXISTS source_record.records_lb;

CREATE TABLE source_record.records_lb AS
    SELECT __id,
           id::uuid,
           state,
           matched_id::uuid,
           external_ids_holder__instance_id::uuid AS external_id,
           external_ids_holder__instance_hrid AS external_hrid
        FROM source_record.records__t;

CREATE INDEX ON source_record.records_lb (__id);

CREATE INDEX ON source_record.records_lb (id);

CREATE INDEX ON source_record.records_lb (state);

CREATE INDEX ON source_record.records_lb (matched_id);

CREATE INDEX ON source_record.records_lb (external_id);

CREATE INDEX ON source_record.records_lb (external_hrid);

DROP TABLE IF EXISTS source_record.marc_records_lb;

CREATE TABLE source_record.marc_records_lb AS
    SELECT __id,
           id::uuid,
           parsed_record__content AS content
        FROM source_record.records__t;

CREATE INDEX ON source_record.marc_records_lb (__id);

CREATE INDEX ON source_record.marc_records_lb (id);

CREATE INDEX ON source_record.marc_records_lb USING gin (content gin_trgm_ops);
