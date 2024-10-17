CREATE TABLE IF NOT EXISTS task.user
(
    user_id integer NOT NULL DEFAULT nextval('api.api_user_user_id_seq'::regclass),
    user_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    email character varying(100) COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modified_at timestamp with time zone,
    CONSTRAINT api_user_pkey PRIMARY KEY (user_id)
)

CREATE TABLE IF NOT EXISTS task.task
(
    task_id serial PRIMARY KEY,
    title character varying(60) NOT NULL,
    description character varying(256) NOT NULL,
    due_date timestamp with time zone,
    priority character varying(10),
    status character varying(10),
    CONSTRAINT user_id FOREIGN KEY (user_id)
    REFERENCES task.user (user_id) MATCH SIMPLE
     ON UPDATE NO ACTION
     ON DELETE NO ACTION

)

CREATE TABLE IF NOT EXISTS task.user_profile
(

    profile_id serial serial PRIMARY KEY,
    user_id integer,
    bio character varying(100),
    location character varying(100),
    language character varying(20),
    CONSTRAINT user_id FOREIGN KEY (user_id)
    REFERENCES task.user (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION

)

CREATE TABLE IF NOT EXISTS task.file_details
(

    file_id serial PRIMARY KEY,
    file_name character varying(100),
    task_id integer,
    CONSTRAINT task_id FOREIGN KEY (task_id)
    REFERENCES task.task (task_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION

)