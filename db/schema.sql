-- AquaTwin AT-MORT-001 — esquema MVP
-- PostgreSQL

CREATE TABLE sites (
  site_id UUID PRIMARY KEY,
  name TEXT NOT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE cages (
  cage_id UUID PRIMARY KEY,
  site_id UUID NOT NULL REFERENCES sites(site_id),
  name TEXT NOT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE cohorts (
  cohort_id UUID PRIMARY KEY,
  cage_id UUID NOT NULL REFERENCES cages(cage_id),
  species TEXT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE
);

CREATE TABLE observations (
  observation_id UUID PRIMARY KEY,
  cage_id UUID NOT NULL REFERENCES cages(cage_id),
  cohort_id UUID REFERENCES cohorts(cohort_id),
  observed_at TIMESTAMPTZ NOT NULL,
  variable_code TEXT NOT NULL,
  value DOUBLE PRECISION NOT NULL,
  unit TEXT NOT NULL,
  quality_flag TEXT NOT NULL DEFAULT 'UNASSESSED',
  source_id TEXT NOT NULL,
  ingested_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX observations_cage_time_idx ON observations(cage_id, observed_at);

CREATE TABLE production_daily (
  cage_id UUID NOT NULL REFERENCES cages(cage_id),
  cohort_id UUID NOT NULL REFERENCES cohorts(cohort_id),
  day DATE NOT NULL,
  fish_count INTEGER,
  mean_weight_g DOUBLE PRECISION,
  biomass_kg DOUBLE PRECISION,
  feed_kg DOUBLE PRECISION,
  appetite_index DOUBLE PRECISION,
  PRIMARY KEY (cage_id, cohort_id, day)
);

CREATE TABLE mortality_daily (
  cage_id UUID NOT NULL REFERENCES cages(cage_id),
  cohort_id UUID NOT NULL REFERENCES cohorts(cohort_id),
  day DATE NOT NULL,
  mortality_n INTEGER NOT NULL CHECK (mortality_n >= 0),
  mortality_pct DOUBLE PRECISION,
  cause_code TEXT NOT NULL DEFAULT 'UNKNOWN',
  PRIMARY KEY (cage_id, cohort_id, day, cause_code)
);

CREATE TABLE health_events (
  event_id UUID PRIMARY KEY,
  cage_id UUID NOT NULL REFERENCES cages(cage_id),
  cohort_id UUID REFERENCES cohorts(cohort_id),
  occurred_at TIMESTAMPTZ NOT NULL,
  suspected_diagnosis TEXT,
  confirmed_diagnosis TEXT,
  diagnostic_method TEXT,
  pathogen TEXT,
  severity TEXT,
  treatment TEXT,
  professional_reviewed BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE predictions (
  prediction_id UUID PRIMARY KEY,
  cage_id UUID NOT NULL REFERENCES cages(cage_id),
  cohort_id UUID REFERENCES cohorts(cohort_id),
  predicted_at TIMESTAMPTZ NOT NULL,
  horizon_hours INTEGER NOT NULL,
  risk_score DOUBLE PRECISION NOT NULL CHECK (risk_score BETWEEN 0 AND 1),
  confidence DOUBLE PRECISION CHECK (confidence BETWEEN 0 AND 1),
  data_quality_score DOUBLE PRECISION CHECK (data_quality_score BETWEEN 0 AND 1),
  model_id TEXT NOT NULL,
  model_version TEXT NOT NULL,
  feature_version TEXT NOT NULL,
  explanation JSONB,
  input_hash TEXT NOT NULL
);

CREATE TABLE data_provenance (
  provenance_id UUID PRIMARY KEY,
  record_type TEXT NOT NULL,
  record_id UUID NOT NULL,
  source_type TEXT NOT NULL,
  source_name TEXT NOT NULL,
  source_reference TEXT,
  measurement_method TEXT,
  instrument TEXT,
  calibration_status TEXT,
  verification_status TEXT NOT NULL DEFAULT 'UNVERIFIED',
  transformation TEXT,
  software_version TEXT,
  recorded_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
