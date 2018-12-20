drop table if exists users;
drop table if exists groups;
drop table if exists teachers;
drop table if exists students;
create table users (
  id integer primary key autoincrement,
  username text not null unique,
  email text not null unique,
  registration_uid text not null unique,
  password_hash text not null,
  name text not null,
  surname text not null,
  second_name  text not null,
  status text not null,
  phone text not null,
  city text not null,
  description text not null
);
create table teachers (
  id integer primary key autoincrement,
  user_id integer unique,
  foreign key (user_id) references users(id)
);
create table groups (
  id integer primary key autoincrement,
  name text not null,
  grade text not null
);
create table students (
  id integer primary key autoincrement,
  group_id integer unique,
  user_id integer unique,
  year integer not null,
  degree text not null,
  education_form text not null,
  education_basis text not null,
  foreign key (user_id) references users(id)
  foreign key (group_id) references groups(id)
);